## Data.json is a .json file that contains the data for the Named Entity Recognition and Intent Classification tasks.

This data is in the form of annotated sentences labelled according to the intent they represent, along with the entities identified.


example:
	{
        "text": "I want to order a plate of vegetable soup with swallow and 2 pieces of fish. Deliver to 39 Western Avenue GRA. Call 08032867986 for more information.",
        "intent": "Order",
        "entities": [
          {
            "start": 18,
            "end": 54,
            "value": "plate of vegetable soup with swallow",
            "entity": "Product - food"
          },
          {
            "start": 61,
            "end": 75,
            "value": "pieces of fish",
            "entity": "Product - food"
          },
          {
            "start": 88,
            "end": 109,
            "value": "39 Western Avenue GRA",
            "entity": "location"
          },
          {
            "start": 116,
            "end": 127,
            "value": "08032867986",
            "entity": "Telephone"
          }
        ]
      },
      {



From the above we can see that 
## The text or sentence labelled is:
 "I want to order a plate of vegetable soup with swallow and 2 pieces of fish. Deliver to 39 Western Avenue GRA. Call 08032867986 for more information."

## Intent was classified as "Order"

## Entities recognized are:
- "plate of vegetable soup with swallow" recognized as Product - food
- "pieces of fish" recognized as "Product - food"
- "39 Western Avenue GRA" recognized as "39 Western Avenue GRA"
- "08032867986" recognized as Telephone