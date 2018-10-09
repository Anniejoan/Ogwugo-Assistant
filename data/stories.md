## story_001
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
## story_002
* greet
	- utter_greet
* Order[Product-food = plate of vegetable soup with swallow] [Product - drinks = Carlo rossi pink moscato]
	- slot{"Product": "plate of vegetable soup with swallow","Carlo rossi pink moscato"}
	- utter_ask_details
* Details[Username = wilky24]
	- slot{"Username"= "wilky24"}
	- action_User_search
	- action_Product_search
## story_003
* Order[Product-food = chicken hamburgers] [Store - Resturant = Golden toast]
    - slot{"Product": "chicken hamburgers"}
    - slot{"Store": "Golden toast"}
    - utter_ask_details
* Details[Telephone = 07061030875] [Location = 12 Ufuma street Achara layout]
   - slot{"Location": "12 Ufuma street Achara layout"}
   - slot{"Telephone": "07061030875"}
   - action_Store_search
   - action_Product_search
* goodbye
   - utter_goodbye
## story_004
* Order[Product-food = amala Ewedu and gbegiri] [Store - Resturant = Amala Embassy]
    - slot{"Product": "amala Ewedu and gbegiri"}
    - slot{"Store": "Amala Embassy"}
    - utter_ask_details
* Details[Username = gerald29th]
	- slot{"Username"= "gerald29th"}
	- action_User_search
	- action_Store_search
	- action_Product_search
## story__005
* Order[Product-food = hamburger] [Product - drinks = yogurt] [Telephone = 08153305653] [Location = University of Nigeria,Enugu campus]
 	- slot{"Product": "hamburger","yogurt"}
 	- slot{"Location": "University of Nigeria,Enugu campus"}
    - slot{"Telephone": "08153305653"}
    - action_Product_search
 ## story__006
* Order[Product-food = swallow with bitter leaf soup] [Store - Resturant = Ogwugo Food] [Telephone = 07065111377] [Location = No 6 Nzimiro street new haven]
 	- slot{"Product": "swallow with bitter leaf soup"}
 	- slot{"Store": "Ogwugo Food"}
 	- slot{"Location": "No 6 Nzimiro street new haven"}
    - slot{"Telephone": "07065111377"}
    - action_Store_search
    - action_Product_search

