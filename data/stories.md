## story_001
* greet
 - utter_greet
## story_002
* greet
   - utter_greet
* Order[Product = Jollof rice]
   - slot{"Product": "Jollof rice"}
   - utter_ask_details
* Details[Telephone = 08094753854] [Location = No 13 Chime Avenue, New Haven]
   - slot{"location": "No 13 Chime Avenue, New Haven"}
   - slot{"Telephone": "08094753854"}
   - action_Product_search
* goodbye
   - utter_goodbye
## story_003
* greet
	- utter_greet
* Order[Product = plate of vegetable soup with swallow] [Product = Carlo rossi pink moscato]
	- slot{"Product": "plate of vegetable soup with swallow"} 
    - slot{"Product": "Carlo rossi pink moscato"}
	- utter_ask_details
* Details[Username = wilky24]
	- slot{"Username": "wilky24"}
	- action_Product_search
## story_004
* Order[Product = chicken hamburgers] [Store - Resturant = Golden toast]
    - slot{"Product": "chicken hamburgers"}
    - slot{"Store": "Golden toast"}
    - utter_ask_details
* Details[Telephone = 07061030875] [Location = 12 Ufuma street Achara layout]
   - slot{"location": "12 Ufuma street Achara layout"}
   - slot{"Telephone": "07061030875"}
   - action_Product_search
* goodbye
   - utter_goodbye
## story_005
* Order[Product = amala Ewedu and gbegiri] [Store - Resturant = Amala Embassy]
    - slot{"Product": "amala Ewedu and gbegiri"}
    - slot{"Store": "Amala Embassy"}
    - utter_ask_details
* Details[Username = gerald29th]
	- slot{"Username": "gerald29th"}
	- action_Product_search
## story_006
* Order[Product = hamburger] [Product = yogurt] [Telephone = 08153305653] [Location = University of Nigeria,Enugu campus]
 	- slot{"Product": "hamburger"}
  - slot{"Product": "yogurt"}
 	- slot{"location": "University of Nigeria,Enugu campus"}
  - slot{"Telephone": "08153305653"}
  - action_Product_search
## story_007
* Order[Product = swallow with bitter leaf soup] [Store - Resturant = Ogwugo Food] [Telephone = 07065111377] [Location = No 6 Nzimiro street new haven]
 	- slot{"Product": "swallow with bitter leaf soup"}
 	- slot{"Store": "Ogwugo Food"}
 	- slot{"location": "No 6 Nzimiro street new haven"}
  - slot{"Telephone": "07065111377"}
  - action_Product_search
## Generated Story -1909956514685070176
* None
* Order{"Product": "jollof rice"}
    - slot{"Product": ["jollof rice"]}
    - utter_ask_details
* Details{"Telephone": "08097383088", "location": "no 3 kanife close"}
    - slot{"Telephone": "08097383088"}
    - slot{"location": "no 3 kanife close"}
    - action_Product_search
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
    - action_Product_search
* goodbye
    - utter_goodbye

## Generated Story 5983349739934686023
* greet
    - utter_greet
* Order{"Product": "rice"}
    - slot{"Product": ["rice"]}
    - utter_ask_details
* Details{"Telephone": "08086991408", "location": "garden avenue"}
    - slot{"Telephone": "08086991408"}
    - slot{"location": "garden avenue"}
    - action_Product_search

## Generated Story -1039785702541867140
* greet
    - utter_greet
* Order{"Product": "hamburger"}
    - slot{"Product": ["hamburger"]}
    - utter_ask_details
* Details{"location": "Coal city garden block 20", "Telephone": "08065122550"}
    - slot{"Telephone": "08065122550"}
    - slot{"location": "Coal city garden block 20"}
    - action_Product_search
    - slot{"Product": ["hamburger"]}
* Order{"Product": "fish"}
    - slot{"Product": ["fish"]}
    - utter_ask_details
* Details{"Telephone": "09057683756"}
    - slot{"Telephone": "09057683756"}
    - action_Product_search
    - slot{"Product": ["fish"]}

## Generated Story 7671612219006255901
* greet
    - utter_greet
* Order{"Product": "goat meat"}
    - slot{"Product": ["fried rice", "goat meat"]}
    - utter_ask_details
* Details{"Username": "Tessy"}
    - slot{"Username": "Tessy"}
    - action_Product_search

## Generated Story -7489097257094579890
* Order{"Product": "pancakes"}
    - slot{"Product": ["pancakes"]}
    - utter_ask_details
* Details{"Telephone": "09078954376"}
    - slot{"Telephone": "09078954376"}
    - action_Product_search

## Generated Story 4390043510296839731
* Order{"Product": "water"}
    - slot{"Product": ["water"]}
    - utter_ask_details
* Details{"location": "no 4 coal city garden"}
    - slot{"location": "no 4 coal city garden"}
    - action_Product_search
* goodbye
    - utter_goodbye

## Generated Story -2164370274243428440
* greet
    - utter_greet
* Order{"Product": "jollof rice"}
    - slot{"Product": ["jollof rice"]}
    - utter_ask_details
* Details{"Telephone": "08140699847"}
    - slot{"Telephone": "08140699847"}
    - action_Product_search


