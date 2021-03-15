from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

import logging
import json
import smtplib

from email.message import EmailMessage
#from rasa.constants import DEFAULT_DATA_PATH
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, SlotSet, Restarted

from zomatopy import Zomato
import asyncio
import time
import os

DEFAULT_DATA_PATH = 'data'
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("__name__")
user_key = "8bdae08cb39d9ff1b6f60d8762314efd"
config = {"user_key": user_key}
_zomato = Zomato(config)


""" Custom action to fetch list of restaurants
"""
class ActionSearchRestaurants(Action):
    def name(self):
        return "action_restaurant_search"

    async def run(self, dispatcher, tracker, domain):
        response_message = ""
        email_message = ""
        search_validity = "valid"

        budget = tracker.get_slot("budget")
        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")

        
        if not location:
            search_validity = "invalid"
        else:
            """
				retrieve location details
			"""
            response = _zomato.get_location(location)
            location_details = {}

            if response is not None:
                response_json = json.loads(response)
                if response_json["status"] == "success":
                    """
						fetch location details and store 'city_id'
					"""
                    location_details = response_json["location_suggestions"][0]
                    city_id = location_details["city_id"]
                    city_name = location_details["city_name"]

                    """
                        Validate if the location details is of the requested location
                    """
                    if location.lower() == city_name.lower():

                        """
                            fetch all cuisines available in the location
                        """
                        response_cuisine = _zomato.get_cuisines(city_id)
                      
                        cuisine_list = response_cuisine.values()
                        if cuisine is not None:
                            if cuisine in response_cuisine.values():
                                cuisine_list = [cuisine]
                        restaurants_found = await self.search_restaurant(dispatcher,
                            budget,location, location_details, cuisine_list
                        )
                        if len(restaurants_found) > 0:					
                            number_of_records = 10
                            restaurant_filtered_budget = restaurants_found
                            if len(restaurant_filtered_budget) < 10:
                                number_of_records = len(restaurant_filtered_budget)
                            if number_of_records <10:
                                if number_of_records<=5:
                                    response_message = "I have found "+ str(number_of_records) + " results for the search. Displaying the results\n"
                                else:
                                    response_message = "I have found " + str(number_of_records) + " results for the search. Displaying top 5 results\n"
                                email_message = "I have found " + str(number_of_records) + " results for your restaurant search search criteria\n"
                            else:
                                response_message = "Displaying top 5 results\n"
                                email_message = "Please find below top " + str(number_of_records) + " results for the restaurant search\n"
                            for index in range(0, number_of_records):
                                restaurant = restaurant_filtered_budget[index]
                                if index < 5:
                                    response_message = (
                                        str(response_message)
                                        + str("\n   ")
                                        + str(index + 1)
                                        + ". "
                                        + str(restaurant["name"])
                                        + " in "
                                        + str(restaurant["address"]) 
                                        + " has been rated "
                                        + str(restaurant["rating"])
                                        + " out of 5"
                                        + str("\n")
                                    )

                                email_message = (
                                    str(email_message)
                                    + str("\n   ")
                                    + str(index + 1)
                                    + ". "
                                    + str(restaurant["name"])
                                    + " in "
                                    + str(restaurant["address"]) 
                                    + " has been rated "
                                    + str(restaurant["rating"])
                                    + " out of 5. "
                                    + "Average cost for 2 : "
                                    + str(restaurant["avg_cost_for_2"])
                                    + str("\n")
                                )

                        else:
                            search_validity = "invalid"
                    else:
                        search_validity = "invalid"
                else:
                    search_validity = "invalid"                            
            else:
                search_validity = "invalid"

        if search_validity == "valid":
            dispatcher.utter_message(response_message)
        return [SlotSet("search_validity", search_validity), SlotSet("email_message", email_message)]


    async def search_restaurant(
        self,dispatcher,budget, location="", location_details={}, cuisine_list=[]
    ) -> list:
        restaurants_found = []

        """
			Search restaurants
		"""
        start = 0
        latitude=location_details["latitude"]
        longitude=location_details["longitude"]
        cuisines= ','.join(cuisine_list)
        rangeMin = 0
        rangeMax = 999999
       
        if budget == "Lesser than Rs. 300":
            rangeMax = 299
        elif budget == "Rs. 300 to 700":
            rangeMin = 300
            rangeMax = 700
        elif budget == "More than Rs. 700":
            rangeMin = 701
        else:
            """
                Default budget
            """
            rangeMin = 0
            rangeMax = 9999

        # Search for 100 restaurants initially to filter based on budget. As for few corner cases. we do not get results within first 20 restaurants
        # Zomato API has limitation of providing only upto 100 results per query and we can filter budget within query
        fut_resp1 = self.search_restaurant_results(dispatcher, latitude, longitude, cuisines, 0)
        fut_resp2 = self.search_restaurant_results(dispatcher, latitude, longitude, cuisines, 20)
        fut_resp3 = self.search_restaurant_results(dispatcher, latitude, longitude, cuisines, 40)
        fut_resp4 = self.search_restaurant_results(dispatcher, latitude, longitude, cuisines, 60)
        fut_resp5 = self.search_restaurant_results(dispatcher, latitude, longitude, cuisines, 80)


        resp1, resp2, resp3,resp4, resp5 = await asyncio.gather(fut_resp1, fut_resp2, fut_resp3,fut_resp4, fut_resp5)
        responses = [resp1, resp2, resp3,resp4, resp5]

        for response in responses:


            if response is not None:
                response_json = json.loads(response)
                if response_json["results_found"] > 0:
                    for restaurant in response_json["restaurants"]:
                        avg_cost = int(restaurant["restaurant"]["average_cost_for_two"])
                        if avg_cost >= rangeMin and avg_cost <= rangeMax :
                            restaurants_found.append(
                                {
                                    "name": restaurant["restaurant"]["name"],
                                    "address": restaurant["restaurant"]["location"]["address"],
                                    "avg_cost_for_2": restaurant["restaurant"]["average_cost_for_two"],
                                    "rating": restaurant["restaurant"]["user_rating"]["aggregate_rating"],
                                }
                            )

                        if(len(restaurants_found)>10):
                            break

            if (len(restaurants_found)>10):
                break

        return restaurants_found

    async def filter_restaurant_by_budget(self, budget, restaurant_list) -> list:
        filtered_restaurant_list = []

        """
            Set the budget range based on input
        """
        rangeMin = 0
        rangeMax = 999999
       
        if budget == "Lesser than Rs. 300":
            rangeMax = 299
        elif budget == "Rs. 300 to 700":
            rangeMin = 300
            rangeMax = 700
        elif budget == "More than Rs. 700":
            rangeMin = 701
        else:
            """
                Default budget
            """
            rangeMin = 0
            rangeMax = 9999

        for restaurant in restaurant_list:
            avg_cost = int(restaurant["avg_cost_for_2"])

            if avg_cost >= rangeMin and avg_cost <= rangeMax:
                filtered_restaurant_list.append(restaurant)
            if len(filtered_restaurant_list)>10:
                break

        return filtered_restaurant_list

    async def search_restaurant_results(self, dispatcher,
        latitude,longitude , cuisines, start
    ) -> list :
            response = await _zomato.restaurant_search(
                self,
                latitude=latitude,
                longitude=longitude,
                cuisines= cuisines, limit = 20, start =start)
            return response


""" Custom action to validate input location
"""
class ActionValidateLocation(Action):
    def name(self):
        return "action_location_valid"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        location_validity = "valid"

        if not location:
            location_validity = "invalid"
        else:
            filepath = DEFAULT_DATA_PATH + "/cities.json"

            with open(filepath) as cities_file:

                data = json.load(cities_file)

                if data is not None:
                    tier1_cities = data["data"]["tier1"]
                    tier2_cities = data["data"]["tier2"]

                    tier1_cities_lower = [city.lower() for city in tier1_cities]
                    tier2_cities_lower = [city.lower() for city in tier2_cities]

                    location_validity = (
                        "invalid"
                        if location.lower() not in tier1_cities_lower
                        and location.lower() not in tier2_cities_lower
                        else "valid"
                    )
                else:
                    location_validity = "invalid"

        return [SlotSet("location_validity", location_validity)]


""" Custom action to validate input cuisine
"""
class ActionValidateCuisine(Action):
    def name(self):
        return "action_cuisine_valid"

    def run(self, dispatcher, tracker, domain):

        cuisine = tracker.get_slot("cuisine")
        cuisine_validity = "valid"

        if not cuisine:
            cuisine_validity = "invalid"
        else:
            supported_cuisines = [
                "american",
                "chinese",
                "italian",
                "mexican",
                "north indian",
                "south indian",
            ]

            cuisine_validity = (
                "invalid" if cuisine.lower() not in supported_cuisines else "valid"
            )

        return [SlotSet("cuisine_validity", cuisine_validity)]


class ActionRestarted(Action): 	
	def name(self):
		return 'action_restart'

	def run(self, dispatcher, tracker, domain):
		return[Restarted()] 


class ActionSlotReset(Action): 
	def name(self): 
		return 'action_slot_reset' 

	def run(self, dispatcher, tracker, domain): 
		return[AllSlotsReset()]


""" Custom action to send an email
"""
class ActionSendEmail(Action):

    def name(self):
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):

        location = tracker.get_slot("location")
        cuisine = tracker.get_slot("cuisine")
        email_id = tracker.get_slot("email")
        email_message = tracker.get_slot("email_message")
        
        """
            Parse email id
            Required to handle email id sent from SLACK connector
        """
        str_email_id = str(email_id)
        if str_email_id.startswith("mailto"):
            separator_index = str_email_id.index("|")
            if separator_index > -1:
                emails = str_email_id.split("|")
                email_id = emails[1]

        """
            Create an email message
        """
        message = EmailMessage()

        message.set_content(email_message)
        message['Subject'] = "Restaurant Bot | List of {0} Restaurants in {1}".format(cuisine, location)

        """
            Read SMTP configuration
        """
        smtp_config = {}
        filepath = DEFAULT_DATA_PATH + "/smtpconfig.txt"

        with open(filepath) as mail_file:
            for line in mail_file:
                name, var = line.partition("=")[::2]
                smtp_config[name.strip()] = var.strip()
		        
        """
            Send email to the user
        """
        try:
            s = smtplib.SMTP_SSL(host=smtp_config["smtpserver_host"], port=smtp_config["smtpserver_port"])
            s.login(smtp_config["username"], smtp_config["password"])
        
            message['From'] = smtp_config["from_email"]
            message['To'] = email_id
           
            s.send_message(message)
            s.quit()
        except Exception as e:
            print("failed to send an email")
            print(e)

        return [AllSlotsReset()]
