## Stories.md is a markdown file that contains the data conversations that OgwugoAssistant learns from

The first few stories are handwritten using the RASA format while the rest will be generated using Online_Training session with the assistant.

This is an example story format.


* greet
   - utter_greet
* Order[Product-food = Jollof rice] [Product-food = meat]
   - slot{"Product": "Jollof rice","meat"}
   - utter_ask_details
* Details[Telephone = 08094753854] [Location = No 13 Chime Avenue, New Haven]
   - slot{"Location": "No 13 Chime Avenue, New Haven"}
   - slot{"Telephone": "08094753854"}
   - action_Product_search
* goodbye
   - utter_goodbye
   
   
   As we can see above, the text beginning with '*' represents the user logs 
   while those with '-' represents the OgwugoAssistant's actions.
   
   Each user log is classified according to its intent.
   The identified entities from the user log are in square brackets and OgwugoAssistant places these entities in their appropriate slots.
   Then it moves on to perform the next action which in this case is to ask for details since phone no. and address are missing.
   When it recieves the information details, it places the recognized entities in slots and performs the next required action.
   And the process continues.
   
   
   The more stories provided, the better OgwugoAssistant gets at handling these processes and gets better at choosing the right actions to respond with in each situation.