## story_001
* greet
   - utter_greet
* Order[Product = Jollof rice]
   - slot{"Product": "Jollof rice"}
   - utter_ask_details
* Details[Telephone = 08094753854] [Location = No 13 Chime Avenue, New Haven]
   - slot{"Location": "No 13 Chime Avenue, New Haven"}
   - slot{"Telephone": "08094753854"}
   - action.action_Product_search
* goodbye
   - utter_goodbye
## story_002
* greet
	- utter_greet
* Order[Product = plate of vegetable soup with swallow] [Product = Carlo rossi pink moscato]
	- slot{"Product": "plate of vegetable soup with swallow"} 
  - slot{"Product": "Carlo rossi pink moscato"}
	- utter_ask_details
* Details[Username = wilky24]
	- slot{"Username": "wilky24"}
	- action.action_Product_search
## story_003
* Order[Product = chicken hamburgers] [Store - Resturant = Golden toast]
    - slot{"Product": "chicken hamburgers"}
    - slot{"Store": "Golden toast"}
    - utter_ask_details
* Details[Telephone = 07061030875] [Location = 12 Ufuma street Achara layout]
   - slot{"Location": "12 Ufuma street Achara layout"}
   - slot{"Telephone": "07061030875"}
   - action.action_Product_search
* goodbye
   - utter_goodbye
## story_004
* Order[Product = amala Ewedu and gbegiri] [Store - Resturant = Amala Embassy]
    - slot{"Product": "amala Ewedu and gbegiri"}
    - slot{"Store": "Amala Embassy"}
    - utter_ask_details
* Details[Username = gerald29th]
	- slot{"Username": "gerald29th"}
	- action.action_Product_search
## story__005
* Order[Product = hamburger] [Product = yogurt] [Telephone = 08153305653] [Location = University of Nigeria,Enugu campus]
 	- slot{"Product": "hamburger"}
  - slot{"Product": "yogurt"}
 	- slot{"Location": "University of Nigeria,Enugu campus"}
  - slot{"Telephone": "08153305653"}
  - action.action_Product_search
 ## story__006
* Order[Product = swallow with bitter leaf soup] [Store - Resturant = Ogwugo Food] [Telephone = 07065111377] [Location = No 6 Nzimiro street new haven]
 	- slot{"Product": "swallow with bitter leaf soup"}
 	- slot{"Store": "Ogwugo Food"}
 	- slot{"Location": "No 6 Nzimiro street new haven"}
  - slot{"Telephone": "07065111377"}
  - action.action_Product_search
## Generated Story -1909956514685070176
* None
* Order{"Product": "jollof rice"}
    - slot{"Product": ["jollof rice"]}
    - utter_ask_details
* Details{"Telephone": "08097383088", "location": "no 3 kanife close"}
    - slot{"Telephone": "08097383088"}
    - slot{"location": "no 3 kanife close"}
    - action.action_Product_search
* goodbye
    - utter_goodbye
## Generated Story -4538375431537020688
* greet
    - utter_greet
* Order{"Product": "chicken"}
    - slot{"Product": ["rice and stew", "chicken"]}
    - utter_ask_details
* Details{"Username": "wilky24"}
    - slot{"Username": "wilky24"}
    - action.action_Product_search
* goodbye
    - utter_goodbye

