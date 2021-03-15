<!-- markdownlint-disable -->

<!-- restart -->
## interactive_story_1
* goodbye
  - utter_bye
  - action_restart

## interactive_story_2
* deny
  - utter_bye
  - action_restart


<!-- greet, ask restaurant -->
## interactive_story_3
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_4
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
  - action_slot_reset
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_5
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset  
  - action_restart

## interactive_story_6
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_7
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_8
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

<!-- greet, location + cuisine-->
## interactive_story_9
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_10
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_11
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "Thai"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_12
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_13
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_slot_reset

<!-- no greet, location + cuisine -->
## interactive_story_14
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_bye
* thanks
  - utter_bye
  - action_restart

## interactive_story_15
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_16
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## interactive_story_17
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_18
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

<!-- queries with cuisine only -->

<!-- start with greet, followed by question -->
## interactive_story_19
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_20
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_21
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_22
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_23
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_24
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- no greet, start with cuisine -->
## interactive_story_25
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_26
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_27
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_28
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_29
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_30
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- queries with location only -->

<!-- start with greet, followed by question -->
## interactive_story_31
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_32
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_32_1
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "north indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_33
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_34
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

<!-- no greet, start with location -->
## interactive_story_35
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_36
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_37
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_38
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

<!-- cuisine + location, both invalid -->

<!-- greet, followed by question -->
## interactive_story_39
* greet
  - utter_greet
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity": "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_40
* greet
  - utter_greet
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- no greet -->
## interactive_story_41
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_42
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

<!-- invalid search -->
## interactive_story_43
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_44
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
  - action_slot_reset
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_45
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart
  
## interactive_story_46
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_47
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_48
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart
  
## interactive_story_49
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_50
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_51
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart
  
## interactive_story_52
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_53
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_54
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_55
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_56
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_57
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_58
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_59
* greet
  - utter_greet
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

## interactive_story_60
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "invalid", "email_message": ""}
  - utter_search_invalid
  - utter_bye
  - action_restart

<!-- chat-bot not helpful -->
## interactive_story_61
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_62
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart
  
## interactive_story_63
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_64
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_65
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_66
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_67
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_68
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* affirm
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_69
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_70
* greet
  - utter_greet
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_71
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_72
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_73
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_74
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

<!-- stop conversation with denial-->
## interactive_story_75
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_76
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_77
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_78
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_79
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_80
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* deny
  - utter_deny
  - utter_bye
  - action_restart

<!-- drop out of conversation with bye-->
## interactive_story_81
* greet
  - utter_greet
* goodbye
  - utter_bye
  - action_restart

## interactive_story_82
* restaurant_search
  - utter_ask_location
* goodbye
  - utter_bye
  - action_restart

## interactive_story_83
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* goodbye
  - utter_bye
  - action_restart

## interactive_story_84
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* goodbye
  - utter_bye
  - action_restart

## interactive_story_85
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* goodbye
  - utter_bye
  - action_restart

## interactive_story_86
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* goodbye
  - utter_bye
  - action_restart

## interactive_story_87
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* goodbye
  - utter_bye
  - action_restart

## interactive_story_88
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* goodbye
  - utter_bye
  - action_restart

## interactive_story_89
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* goodbye
  - utter_bye
  - action_restart

<!-- handling out of scope responses -->
## interactive_story_90
* greet
  - utter_greet
* out_of_scope
  - utter_out_of_scope
  - utter_bye
  - action_restart

## interactive_story_91
* restaurant_search
  - utter_ask_location
* out_of_scope
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## interactive_story_92
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## interactive_story_93
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## interactive_story_94
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_95
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* out_of_scope
  - utter_bye
  - action_restart

## interactive_story_96
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_97
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine":"mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## interactive_story_98
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_99
* restaurant_search{"location": "delhi"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## interactive_story_100
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_101
* restaurant_search{"location":"Kolkata", "cuisine":"mexican"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* out_of_scope
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## interactive_story_102
* greet
  - utter_greet
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_103
* restaurant_search{"cuisine":"indian","location":"Mysore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_104
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_105
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* out_of_scope
  - action_slot_reset
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location  
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_106
* greet
  - utter_greet
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity": "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* affirm
  - action_slot_reset
  - utter_ask_location
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity": "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity": "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_107
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine  
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_108
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_bye
  - action_restart

## interactive_story_109
* greet
  - utter_greet
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_110
* restaurant_search{"cuisine": "indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_location
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Bangalore"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_111
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_bye
  - action_restart

## interactive_story_112
* greet
  - utter_greet
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_113
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_114
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "Patna"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
* thanks
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_115
* greet
  - utter_greet
* restaurant_search{"location": "Vizag", "cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* restaurant_search{"location": "Vizag"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* deny
  - utter_did_that_help
* affirm
  - utter_happy
  - utter_bye
  - action_restart

## interactive_story_116
* restaurant_search{"location": "Delhi", "cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
  - action_slot_reset
* restaurant_search{"location": "Delhi"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "french"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_117
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_118
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_119
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_120
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* deny
  - utter_did_that_help
* deny
  - utter_deny
  - utter_bye
  - action_restart

## interactive_story_121
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_122
* restaurant_search{"location": "agra", "cuisine": "italian"}
  - action_location_valid
  - slot{"location_validity" : "valid"}  
  - action_cuisine_valid
  - slot{"cuisine_validity" : "invalid"}
  - utter_cuisine_invalid
  - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_123
* greet
  - utter_greet
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_124
* restaurant_search{"location": "agra", "cuisine": "italian"} 
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - action_location_valid
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - action_location_valid
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}  
  - utter_ask_details
* affirm
  - utter_ask_email
* ask_email{"email": "abc@abc.com"}
  - action_send_email
  - utter_confirm_email
  - utter_bye
  - action_restart

## interactive_story_125
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "700"}
    - utter_searching
  - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "Please find below top 10 results for the restaurant search\n\n   1. Shah Ghouse Hotel & Restaurant in 20-6-560 TO 563, SYED ALI CHABUTRA SHALIBANDA, Hyderabad, Telangana has been rated 4.4 out of 5. Average cost for 2 : 650\n\n   2. Meridian Cafe & Restaurant in 6-3-697/1, Officers Colony, Panjagutta Cross Road, Panjagutta, Hyderabad has been rated 4.4 out of 5. Average cost for 2 : 600\n\n   3. Imperial Multi Cuisine Restaurant in Opposite HP Petrol Pump, Saidabad X Roads, Malakpet, Hyderabad has been rated 4.3 out of 5. Average cost for 2 : 700\n\n   4. Lucky Restaurant in DRDL Cross Roads, Opposite Owaisi Hospital, Santosh Nagar, Near Saroor Nagar, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 600\n\n   5. Shah Ghouse Hotel & Restaurant in House 9-4-86/17, Salarjung Colony, Circle 10, Tolichowki, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 700\n\n   6. Mehfil Restaurant in Pillar 146, Inner Ring Road, Attapur, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 500\n\n   7. Bench Cafe & Restaurant in 4-1-969/7, Ahuja Estate, Abids Road, Abids, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 500\n\n   8. Ruby Restaurant in Saba Colony, Kummar Basthi, Chandrayangutta, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 300\n\n   9. Lucky Restaurant in Alkapuri X Road, Inner Ring Road, Sai Nagar, Nagole, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 600\n\n   10. Lazzat Restaurant in 17-3-186/4/C/1, Imambara, Yakutpura, Charminar, Hyderabad has been rated 4.1 out of 5. Average cost for 2 : 450\n"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "myname@gmail.com"}
    - slot{"email": "myname@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email
* affirm
    - utter_bye
    - action_restart
* goodbye
	- utter_bye
	
	
<!-- markdownlint-restore -->

## interactive_story_126
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "700"}
    - utter_searching
  - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "Please find below top 10 results for the restaurant search\n\n   1. Shah Ghouse Hotel & Restaurant in 20-6-560 TO 563, SYED ALI CHABUTRA SHALIBANDA, Hyderabad, Telangana has been rated 4.4 out of 5. Average cost for 2 : 650\n\n   2. Meridian Cafe & Restaurant in 6-3-697/1, Officers Colony, Panjagutta Cross Road, Panjagutta, Hyderabad has been rated 4.4 out of 5. Average cost for 2 : 600\n\n   3. Imperial Multi Cuisine Restaurant in Opposite HP Petrol Pump, Saidabad X Roads, Malakpet, Hyderabad has been rated 4.3 out of 5. Average cost for 2 : 700\n\n   4. Lucky Restaurant in DRDL Cross Roads, Opposite Owaisi Hospital, Santosh Nagar, Near Saroor Nagar, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 600\n\n   5. Shah Ghouse Hotel & Restaurant in House 9-4-86/17, Salarjung Colony, Circle 10, Tolichowki, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 700\n\n   6. Mehfil Restaurant in Pillar 146, Inner Ring Road, Attapur, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 500\n\n   7. Bench Cafe & Restaurant in 4-1-969/7, Ahuja Estate, Abids Road, Abids, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 500\n\n   8. Ruby Restaurant in Saba Colony, Kummar Basthi, Chandrayangutta, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 300\n\n   9. Lucky Restaurant in Alkapuri X Road, Inner Ring Road, Sai Nagar, Nagole, Hyderabad has been rated 4.2 out of 5. Average cost for 2 : 600\n\n   10. Lazzat Restaurant in 17-3-186/4/C/1, Imambara, Yakutpura, Charminar, Hyderabad has been rated 4.1 out of 5. Average cost for 2 : 450\n"}
    - utter_ask_details
* affirm
    - utter_ask_email
* ask_email{"email": "vitesh.nathani@gmail.com"}
    - slot{"email": "vitesh.nathani@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email
* affirm
    - utter_bye
    - action_restart

## interactive_story_127
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Mumbai"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
    - slot{"budget": "701"}
    - utter_searching
  - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "Please find below top 10 results for the restaurant search\n\n   1. Origami Japanese And Korean Restaurant in Ground Floor, Supreme Business Park, B Wing, Hiranandani Gardens, Powai, Mumbai has been rated 4.5 out of 5. Average cost for 2 : 2300\n\n   2. Britannia & Company Restaurant in Wakefield House, 11 Sprott Road, 16 Ballard Estate, Fort, Mumbai has been rated 4.4 out of 5. Average cost for 2 : 1000\n\n   3. Status Veg Restaurant in 208, Regent Chambers, Nariman Point, Mumbai has been rated 4.3 out of 5. Average cost for 2 : 800\n\n   4. The Bayview Restaurant - Marine Plaza in Hotel Marine Plaza, 29, Marine Drive, Churchgate, Mumbai has been rated 4.2 out of 5. Average cost for 2 : 2600\n\n   5. Ivy Restaurant And Banquets in Near Shopper's Stop, Amar Mahal, M G Road, Chembur, Mumbai has been rated 4.2 out of 5. Average cost for 2 : 1600\n\n   6. Mao Family Restaurant in 534/536, Dhobitalao, Lohar Chawl, Near Metro Theatre, Kalbadevi, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 800\n\n   7. Lucky Restaurant in Junction Of 9 SV Road & Hill Road, Hill Road, Bandra West, Mumbai has been rated 4.0 out of 5. Average cost for 2 : 1000\n\n   8. Faham Restaurant & Lounge in Building 23, Satkar Hotel Lane, Masjid Station Road, Near Zakaria Masjid, Mohammad Ali Road, Mumbai has been rated 4.0 out of 5. Average cost for 2 : 1100\n\n   9. Canto Restaurant & Banquet in Level P5, Club House, Peninsula Business Park, GK Marg, Lower Parel, Mumbai has been rated 4.0 out of 5. Average cost for 2 : 1300\n\n   10. Durga Restaurant And Bar in 279 B, Nalla Mansion, Opposite Railway Station, Matunga East, Mumbai has been rated 3.9 out of 5. Average cost for 2 : 800\n"}
    - utter_ask_details
* ask_email{"email": "viteshn@gmail.com"}
    - slot{"email": "viteshn@gmail.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email
* restaurant_search{"location": "Balaghat"}
    - slot{"location": "Balaghat"}
    - action_location_valid
    - slot{"location_validity": "invalid"}
    - utter_location_invalid
    - utter_ask_location_retry
* deny
    - utter_deny

* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_searching
  - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "I have found 1 results for your restaurant search search criteria\n\n   1. Yazdani Bakery & Restaurant in Fountain Akbar Ally, Saint Thomas Cathedral, Near Fort, Mumbai has been rated 4.3 out of 5. Average cost for 2 : 200\n"}
	- utter_ask_details
* deny
  - utter_bye

## interactive_story_128
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye


## interactive_story_129
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - action_location_valid
  - slot{"location": "mumbai"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email


## interactive_story_130
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "mbusmkwoid"}
  - slot{"location": "mbusmkwoid"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

  
## interactive_story_131
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "mbumkdjjo"}
  - slot{"location": "mbumkdjjo"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_132
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "rishikesh"}
  - slot{"location": "rishikesh"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "hyderabad"}
  - slot{"location": "hyderabad"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email
  
  
## interactive_story_133
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "haridwar"}
  - slot{"location": "haridwar"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "allahabad"}
  - slot{"location": "allahabad"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_134
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "surat"}
  - slot{"location": "surat"}
  - action_location_valid
  - slot{"location": "surat"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
  
## interactive_story_135
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "ooty"}
  - slot{"location": "ooty"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email

  
  
## interactive_story_136
* greet
  - utter_greet
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
## interactive_story_137
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "pune"}
  - slot{"location": "pune"}
  - action_location_valid
  - slot{"location": "pune"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
  
## interactive_story_138
* greet
  - utter_greet
* restaurant_search{"location": "manali"}
  - slot{"location": "manali"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "srinagar"}
  - slot{"location": "srinagar"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email

  
## interactive_story_139
* greet
  - utter_greet
* restaurant_search{"location": "pune"}
  - slot{"location": "pune"}
  - action_location_valid
  - slot{"location": "pune"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
## interactive_story_140
* greet
  - utter_greet
* restaurant_search{"location": "mbunvkdi"}
  - slot{"location": "mbunvkdi"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "mysore"}
  - slot{"location": "mysore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
  
## interactive_story_141
* greet
  - utter_greet
* restaurant_search{"location": "graaar"}
  - slot{"location": "graaar"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - slot{"location": "agra"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
## interactive_story_142
* greet
  - utter_greet
* restaurant_search{"location": "jaipur"}
  - slot{"location": "jaipur"}
  - action_location_valid
  - slot{"location": "jaipur"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_143
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
## interactive_story_144
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian", "location": "goa"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - slot{"location": "goa"}
  - action_location_valid
  - slot{"location": "goa"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
## interactive_story_145
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptnsneha"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - slot{"location": "ptnsneha"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "patna"}
  - slot{"location": "patna"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
## interactive_story_146
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "haridwar"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "haridwar"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "allahabad"}
  - slot{"location": "allahabad"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
## interactive_story_147
* greet
  - utter_greet
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_location_valid
  - slot{"location": "kolkata"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  

## interactive_story_148
* greet
  - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "ooty"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - slot{"location": "ooty"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "bengaluru"}
  - slot{"location": "bengaluru"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  
## interactive_story_149
* greet
  - utter_greet
* restaurant_search{"cuisine": "american", "location": "rohtak"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - slot{"location": "rohtak"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "chandigarh"}
  - slot{"location": "chandigarh"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
  
## interactive_story_150
* greet
  - utter_greet
* restaurant_search{"location": "hwusirinc"}
  - slot{"location": "hwusirinc"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "jammu"}
  - slot{"location": "jammu"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_151
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "gwalior"}
  - slot{"location": "gwalior"}
  - action_location_valid
  - slot{"location": "gwalior"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email

## interactive_story_152
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "filmkidiejf"}
  - slot{"location": "filmkidiejf"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "faridabad"}
  - slot{"location": "faridabad"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "mexican"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

  
## interactive_story_153
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email


## interactive_story_154
* greet
  - utter_greet
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - action_location_valid
  - slot{"location": "mumbai"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email
  - export

## interactive_story_155
* greet
  - utter_greet
* restaurant_search{"location": "ahmedabad"}
  - slot{"location": "ahmedabad"}
  - action_location_valid
  - slot{"location": "ahmedabad"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email


## interactive_story_156
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_location
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - action_location_valid
  - slot{"location": "bangalore"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email

## interactive_story_157
* greet
  - utter_greet
* restaurant_search{"cuisine": "mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "mexican"}
  - utter_ask_location
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - action_location_valid
  - slot{"location": "mumbai"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email
  - export

## interactive_story_158
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_location
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - action_location_valid
  - slot{"location": "bangalore"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email


## interactive_story_159
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_location
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_location_valid
  - slot{"location": "kolkata"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email


## interactive_story_160
* greet
  - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email

## interactive_story_161
* greet
  - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_162
* greet
  - utter_greet
* restaurant_search{"location": "chandigarh"}
  - slot{"location": "chandigarh"}
  - action_location_valid
  - slot{"location": "chandigarh"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_163
* greet
  - utter_greet
* restaurant_search{"location": "jaipur"}
  - slot{"location": "jaipur"}
  - action_location_valid
  - slot{"location": "jaipur"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye

## interactive_story_164
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptsnkela"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - slot{"location": "ptsnkela"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "pune"}
  - slot{"location": "pune"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email

## interactive_story_165
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart


## interactive_story_166
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - action_location_valid
  - slot{"location": "mumbai"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email


## interactive_story_167
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "mbusmkwoid"}
  - slot{"location": "mbusmkwoid"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

  
## interactive_story_168
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "mbumkdjjo"}
  - slot{"location": "mbumkdjjo"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_169
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "rishikesh"}
  - slot{"location": "rishikesh"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "hyderabad"}
  - slot{"location": "hyderabad"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email
  
  
## interactive_story_170
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "haridwar"}
  - slot{"location": "haridwar"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "allahabad"}
  - slot{"location": "allahabad"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_171
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "surat"}
  - slot{"location": "surat"}
  - action_location_valid
  - slot{"location": "surat"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
  
## interactive_story_172
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "ooty"}
  - slot{"location": "ooty"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email

  
  
## interactive_story_173
* greet
  - utter_greet
* restaurant_search{"location": "delhi"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
## interactive_story_174
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "pune"}
  - slot{"location": "pune"}
  - action_location_valid
  - slot{"location": "pune"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
  
## interactive_story_175
* greet
  - utter_greet
* restaurant_search{"location": "manali"}
  - slot{"location": "manali"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "srinagar"}
  - slot{"location": "srinagar"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email

  
## interactive_story_176
* greet
  - utter_greet
* restaurant_search{"location": "pune"}
  - slot{"location": "pune"}
  - action_location_valid
  - slot{"location": "pune"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
## interactive_story_177
* greet
  - utter_greet
* restaurant_search{"location": "mbunvkdi"}
  - slot{"location": "mbunvkdi"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "mysore"}
  - slot{"location": "mysore"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
  
## interactive_story_178
* greet
  - utter_greet
* restaurant_search{"location": "graaar"}
  - slot{"location": "graaar"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "agra"}
  - slot{"location": "agra"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
## interactive_story_179
* greet
  - utter_greet
* restaurant_search{"location": "jaipur"}
  - slot{"location": "jaipur"}
  - action_location_valid
  - slot{"location": "jaipur"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_180
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
## interactive_story_181
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian", "location": "goa"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - slot{"location": "goa"}
  - action_location_valid
  - slot{"location": "goa"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
## interactive_story_182
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptnsneha"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - slot{"location": "ptnsneha"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "patna"}
  - slot{"location": "patna"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
## interactive_story_183
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "haridwar"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "haridwar"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "allahabad"}
  - slot{"location": "allahabad"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
## interactive_story_184
* greet
  - utter_greet
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_location_valid
  - slot{"location": "kolkata"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  

## interactive_story_185
* greet
  - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "ooty"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - slot{"location": "ooty"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_ask_location_retry
* restaurant_search{"location": "bengaluru"}
  - slot{"location": "bengaluru"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart
  
## interactive_story_186
* greet
  - utter_greet
* restaurant_search{"cuisine": "american", "location": "rohtak"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - slot{"location": "rohtak"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "chandigarh"}
  - slot{"location": "chandigarh"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email
  
  
## interactive_story_187
* greet
  - utter_greet
* restaurant_search{"location": "hwusirinc"}
  - slot{"location": "hwusirinc"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "jammu"}
  - slot{"location": "jammu"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "south indian"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_188
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "gwalior"}
  - slot{"location": "gwalior"}
  - action_location_valid
  - slot{"location": "gwalior"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email

## interactive_story_189
* greet
  - utter_greet
* restaurant_search
  - utter_ask_location
* restaurant_search{"location": "filmkidiejf"}
  - slot{"location": "filmkidiejf"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "faridabad"}
  - slot{"location": "faridabad"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "mexican"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

  
## interactive_story_190
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email


## interactive_story_191
* greet
  - utter_greet
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - action_location_valid
  - slot{"location": "mumbai"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email
  - export

## interactive_story_192
* greet
  - utter_greet
* restaurant_search{"location": "ahmedabad"}
  - slot{"location": "ahmedabad"}
  - action_location_valid
  - slot{"location": "ahmedabad"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "american"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email


## interactive_story_193
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_location
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - action_location_valid
  - slot{"location": "bangalore"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
  - slot{"budget": "Lesser than Rs. 300"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email

## interactive_story_194
* greet
  - utter_greet
* restaurant_search{"cuisine": "mexican"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "mexican"}
  - utter_ask_location
* restaurant_search{"location": "mumbai"}
  - slot{"location": "mumbai"}
  - action_location_valid
  - slot{"location": "mumbai"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email
  - export

## interactive_story_195
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - utter_ask_location
* restaurant_search{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - action_location_valid
  - slot{"location": "bangalore"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email


## interactive_story_196
* greet
  - utter_greet
* restaurant_search{"cuisine": "chinese"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "chinese"}
  - utter_ask_location
* restaurant_search{"location": "kolkata"}
  - slot{"location": "kolkata"}
  - action_location_valid
  - slot{"location": "kolkata"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email


## interactive_story_197
* greet
  - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "my.newmail@mail.com"}
  - slot{"email": "my.newmail@mail.com"}
  - action_send_email
  - utter_confirm_email

## interactive_story_198
* greet
  - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - slot{"location": "delhi"}
  - action_location_valid
  - slot{"location": "delhi"}
  - slot{"location_validity" : "valid"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_199
* greet
  - utter_greet
* restaurant_search{"location": "chandigarh"}
  - slot{"location": "chandigarh"}
  - action_location_valid
  - slot{"location": "chandigarh"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_200
* greet
  - utter_greet
* restaurant_search{"location": "jaipur"}
  - slot{"location": "jaipur"}
  - action_location_valid
  - slot{"location": "jaipur"}
  - slot{"location_validity" : "valid"}
  - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "north indian"}
  - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
  - slot{"budget": "Rs. 300 to 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* deny
  - utter_bye
  - action_restart

## interactive_story_201
* greet
  - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptsnkela"}
  - action_cuisine_valid
  - slot{"cuisine_validity" : "valid"}
  - slot{"cuisine": "italian"}
  - slot{"location": "ptsnkela"}
  - action_location_valid
  - slot{"location": null}
  - slot{"location_validity" : "invalid"}
  - utter_location_invalid
  - utter_ask_location_retry
* restaurant_search{"location": "pune"}
  - slot{"location": "pune"}
  - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
  - slot{"budget": "More than Rs. 700"}
  - utter_searching
  - action_restaurant_search
  - slot{"search_validity" : "valid", "email_message": ""}
  - utter_ask_details

* affirm
  - utter_ask_email
* ask_email{"email": "meenu.gupta232@yahoo.co.in"}
  - slot{"email": "meenu.gupta232@yahoo.co.in"}
  - action_send_email
  - utter_confirm_email

## interactive_story_202
* goodbye
  - utter_bye
  - action_restart

## interactive_story_203
* deny
  - utter_bye
  - action_restart

## interactive_story_204
* goodbye
  - utter_bye
  - action_restart

## interactive_story_205
* deny
  - utter_bye
  - action_restart

## interactive_story_206
* goodbye
  - utter_bye
  - action_restart

## interactive_story_207
* deny
  - utter_bye
  - action_restart

## interactive_story_208
* goodbye
  - utter_bye
  - action_restart

## interactive_story_209
* deny
  - utter_bye
  - action_restart
  
## interactive_story_210
* restaurant_search{"cuisine": "Chinese", "location": "Allahabad"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Allahabad"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "I have found 6 results for your restaurant search search criteria\n\n   1. Rajpoot Bar & Restaurant in Main Chowk, Meergunj, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 800\n\n   2. Dynasty Restaurant - Imperial House in 46-A, Hastings Road, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 1000\n\n   3. Relish Restaurant- The Legend Hotel in The Legend Hotel, First Floor, 23 C, Thornhill Road, Civil Lines, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1100\n\n   4. Puneet Bar & Restaurant in 100, Vivekanand Marg, Meergunj, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1000\n\n   5. Khana Khazana Restaurant -Hotel Grand Continental in Hotel Grand Continental, SP Marg, Civil Lines, Allahabad has been rated 3.6 out of 5. Average cost for 2 : 1250\n\n   6. Atariya Restaurant in 1/H, Chakdondi Ambedkar Nagar, Naini, Allahabad has been rated 3.5 out of 5. Average cost for 2 : 850\n"}
    - utter_ask_details

* restaurant_search{"cuisine": "Chinese", "location": "Allahabad"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Allahabad"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "I have found 6 results for your restaurant search search criteria\n\n   1. Rajpoot Bar & Restaurant in Main Chowk, Meergunj, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 800\n\n   2. Dynasty Restaurant - Imperial House in 46-A, Hastings Road, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 1000\n\n   3. Relish Restaurant- The Legend Hotel in The Legend Hotel, First Floor, 23 C, Thornhill Road, Civil Lines, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1100\n\n   4. Puneet Bar & Restaurant in 100, Vivekanand Marg, Meergunj, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1000\n\n   5. Khana Khazana Restaurant -Hotel Grand Continental in Hotel Grand Continental, SP Marg, Civil Lines, Allahabad has been rated 3.6 out of 5. Average cost for 2 : 1250\n\n   6. Atariya Restaurant in 1/H, Chakdondi Ambedkar Nagar, Naini, Allahabad has been rated 3.5 out of 5. Average cost for 2 : 850\n"}
    - utter_ask_details
* ask_email{"email": "maili@mailinator.com"}
    - slot{"email": "maili@mailinator.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email

* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "Please find below top 10 results for the restaurant search\n\n   1. Tat-Wahh Veg Restaurant in Sakinaka, Mumbai has been rated 4.4 out of 5. Average cost for 2 : 300\n\n   2. Ganesh Palace Restaurant & Bar in 11 And 22, Shanti Nagar Rahivashi CHS, Opposite Giriraj Industrial Estate, Mahakali Caves Road, Shanti Nagar, Andheri East, Mahakali, Mumbai has been rated 4.3 out of 5. Average cost for 2 : 700\n\n   3. National Restaurant in 21 A, Guru Nanak Marg, Turner Road, Bandra Talao, Near Bandra West, Mumbai has been rated 4.2 out of 5. Average cost for 2 : 500\n\n   4. Navaratna Veg Restaurant in Hotel Navaratna,  Plot 10, Sector 17, Vashi, Navi Mumbai has been rated 4.2 out of 5. Average cost for 2 : 600\n\n   5. Ravindra Restaurant in C/1, Amit Apartments, Near Dena Bank, Dahisar East, Mumbai has been rated 4.2 out of 5. Average cost for 2 : 700\n\n   6. Satkar Restaurant in Shop 10, 11, 12, 13 And 14, Ground Floor, Mohan Mahal, Agra Road, Naupada, Thane West, Thane has been rated 4.2 out of 5. Average cost for 2 : 700\n\n   7. Afzal Restaurant in 9 A, Opposite Sai Niketan Building, Shivdas Champsi Marg, Mazgaon, Byculla, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 700\n\n   8. Sneha Restaurant in 7A, Plot 86, Ground Floor, Mahim Shiv Sagar, Cooperative Housing Society, Lady Jamshedji Road, Kapad Bazar, Mahim, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 300\n\n   9. Krishna Restaurant in 31, Mahatma Gandhi Vidya Marg, Government Colony, Bandra East, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 500\n\n   10. New Ajwa Family Restaurant in Shop 12, Benazir Welfare Association, Near Seven Hill Hospital, Marol Military Road, Marol, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 500\n"}
    - utter_ask_details
* ask_email{"email": "mail22@mailinator.com"}
    - slot{"email": "mail22@mailinator.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email

## interactive_story_211
* restaurant_search{"cuisine": "Chinese", "location": "Allahabad"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Allahabad"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "I have found 6 results for your restaurant search search criteria\n\n   1. Rajpoot Bar & Restaurant in Main Chowk, Meergunj, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 800\n\n   2. Dynasty Restaurant - Imperial House in 46-A, Hastings Road, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 1000\n\n   3. Relish Restaurant- The Legend Hotel in The Legend Hotel, First Floor, 23 C, Thornhill Road, Civil Lines, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1100\n\n   4. Puneet Bar & Restaurant in 100, Vivekanand Marg, Meergunj, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1000\n\n   5. Khana Khazana Restaurant -Hotel Grand Continental in Hotel Grand Continental, SP Marg, Civil Lines, Allahabad has been rated 3.6 out of 5. Average cost for 2 : 1250\n\n   6. Atariya Restaurant in 1/H, Chakdondi Ambedkar Nagar, Naini, Allahabad has been rated 3.5 out of 5. Average cost for 2 : 850\n"}
    - utter_ask_details

* restaurant_search{"cuisine": "Chinese", "location": "Allahabad"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Allahabad"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "I have found 6 results for your restaurant search search criteria\n\n   1. Rajpoot Bar & Restaurant in Main Chowk, Meergunj, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 800\n\n   2. Dynasty Restaurant - Imperial House in 46-A, Hastings Road, Allahabad has been rated 3.8 out of 5. Average cost for 2 : 1000\n\n   3. Relish Restaurant- The Legend Hotel in The Legend Hotel, First Floor, 23 C, Thornhill Road, Civil Lines, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1100\n\n   4. Puneet Bar & Restaurant in 100, Vivekanand Marg, Meergunj, Allahabad has been rated 3.7 out of 5. Average cost for 2 : 1000\n\n   5. Khana Khazana Restaurant -Hotel Grand Continental in Hotel Grand Continental, SP Marg, Civil Lines, Allahabad has been rated 3.6 out of 5. Average cost for 2 : 1250\n\n   6. Atariya Restaurant in 1/H, Chakdondi Ambedkar Nagar, Naini, Allahabad has been rated 3.5 out of 5. Average cost for 2 : 850\n"}
    - utter_ask_details
* ask_email{"email": "maili@mailinator.com"}
    - slot{"email": "maili@mailinator.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email

* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "Please find below top 10 results for the restaurant search\n\n   1. Tat-Wahh Veg Restaurant in Sakinaka, Mumbai has been rated 4.4 out of 5. Average cost for 2 : 300\n\n   2. Ganesh Palace Restaurant & Bar in 11 And 22, Shanti Nagar Rahivashi CHS, Opposite Giriraj Industrial Estate, Mahakali Caves Road, Shanti Nagar, Andheri East, Mahakali, Mumbai has been rated 4.3 out of 5. Average cost for 2 : 700\n\n   3. National Restaurant in 21 A, Guru Nanak Marg, Turner Road, Bandra Talao, Near Bandra West, Mumbai has been rated 4.2 out of 5. Average cost for 2 : 500\n\n   4. Navaratna Veg Restaurant in Hotel Navaratna,  Plot 10, Sector 17, Vashi, Navi Mumbai has been rated 4.2 out of 5. Average cost for 2 : 600\n\n   5. Ravindra Restaurant in C/1, Amit Apartments, Near Dena Bank, Dahisar East, Mumbai has been rated 4.2 out of 5. Average cost for 2 : 700\n\n   6. Satkar Restaurant in Shop 10, 11, 12, 13 And 14, Ground Floor, Mohan Mahal, Agra Road, Naupada, Thane West, Thane has been rated 4.2 out of 5. Average cost for 2 : 700\n\n   7. Afzal Restaurant in 9 A, Opposite Sai Niketan Building, Shivdas Champsi Marg, Mazgaon, Byculla, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 700\n\n   8. Sneha Restaurant in 7A, Plot 86, Ground Floor, Mahim Shiv Sagar, Cooperative Housing Society, Lady Jamshedji Road, Kapad Bazar, Mahim, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 300\n\n   9. Krishna Restaurant in 31, Mahatma Gandhi Vidya Marg, Government Colony, Bandra East, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 500\n\n   10. New Ajwa Family Restaurant in Shop 12, Benazir Welfare Association, Near Seven Hill Hospital, Marol Military Road, Marol, Mumbai has been rated 4.1 out of 5. Average cost for 2 : 500\n"}
    - utter_ask_details
* deny
  - utter_bye
  - action_restart
* greet
    - utter_greet
* restaurant_search{"location": "Delhi NCR"}
    - slot{"location": "Delhi NCR"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thain"}
    - slot{"cuisine": "Thain"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "invalid"}
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "russian"}
    - slot{"cuisine": "russian"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "invalid"}
    - utter_cuisine_invalid
    - utter_ask_cuisine_retry
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "More than Rs. 700"}
    - slot{"budget": "More than Rs. 700"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "Please find below top 10 results for the restaurant search\n\n   1. Mahabelly in MA-A05, Ground Floor, Restaurant Block, DLF Avenue, Saket, New Delhi has been rated 4.5 out of 5. Average cost for 2 : 1300\n\n   2. Ji Memsaab - Indian Terrace Restaurant & Bar in Second Floor, Eros City Square Mall, Sector 49, Gurgaon has been rated 4.4 out of 5. Average cost for 2 : 1200\n\n   3. Fuji Japanese Restaurant in M-41/2, Speedbird House, Middle Circle, Connaught Place, New Delhi has been rated 4.3 out of 5. Average cost for 2 : 2000\n\n   4. Rigo Restaurant in 180, Tibetan Old Camp, Majnu ka Tila, New Delhi has been rated 4.3 out of 5. Average cost for 2 : 1000\n\n   5. Busan Korean Restaurant in 9B, Ground Floor, Block 10, New Aruna Nagar, Majnu Ka Tilla, New Delhi has been rated 4.3 out of 5. Average cost for 2 : 900\n\n   6. Binge Restaurant in C 25, Ground Floor, Stellar IT Park, Sector 62, Noida has been rated 4.3 out of 5. Average cost for 2 : 1200\n\n   7. Cafe DEM - Restaurant & Bar in GA-7 & 8, Metro Walk Mall, Rohini, New Delhi has been rated 4.3 out of 5. Average cost for 2 : 2000\n\n   8. QD's Restaurant in A-47, Guru Nanakpura, Near Nirman Vihar Metro Station, Laxmi Nagar, New Delhi has been rated 4.2 out of 5. Average cost for 2 : 1100\n\n   9. QD's Restaurant in I-1A, Lajpat Nagar 2, New Delhi has been rated 4.2 out of 5. Average cost for 2 : 1100\n\n   10. Khana Khazana Restaurant in TA 61, Tughlakabad Extention, Tughlakabad Institutional Area, New Delhi has been rated 4.2 out of 5. Average cost for 2 : 800\n"}
    - utter_ask_details
* deny
    - utter_did_that_help
* affirm
    - utter_happy
    - utter_bye
    - action_restart

* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - action_location_valid
    - slot{"location_validity": "valid"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_cuisine_valid
    - slot{"cuisine_validity": "valid"}
    - utter_ask_budget
* ask_budget{"budget": "Lesser than Rs. 300"}
    - slot{"budget": "Lesser than Rs. 300"}
    - utter_searching
    - action_restaurant_search
    - slot{"search_validity": "valid"}
    - slot{"email_message": "I have found 5 results for your restaurant search search criteria\n\n   1. Kulfiano in II D/5, Newtown, Action Area, City Centre 2, Chinar Park, Kolkata has been rated 4.3 out of 5. Average cost for 2 : 200\n\n   2. New Raj Restaurant in Meghnath Saha Sarani, Besisde 7.5 Rail Gate, New Barrackpore, Barasat, Kolkata has been rated 4.1 out of 5. Average cost for 2 : 250\n\n   3. Sip & Sandwich in Premisses 11F/11 Eco Space business Park, Action area- ll, New Town, Kolkata has been rated 4.1 out of 5. Average cost for 2 : 250\n\n   4. Saiqa Restaurant in 36, Beck Bagan Row, Lower Range, Park Circus Area, Kolkata has been rated 3.9 out of 5. Average cost for 2 : 200\n\n   5. The Happy Restaurant in MB-242, Mahishbathan, Rajarhat, Sector 5, Salt Lake, Kolkata has been rated 3.9 out of 5. Average cost for 2 : 250\n"}
    - utter_ask_details
* ask_email{"email": "maill@mailinator.com"}
    - slot{"email": "maill@mailinator.com"}
    - action_send_email
    - reset_slots
    - utter_confirm_email
