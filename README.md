# Ogwugo-Assistant
A conversational agent for the e-commerce site - Ogwugo 

Developed using the open source NLU tools Rasa NLU, Rasa Core and Spacy
## data.json file:
This contains data in the form of annotated messages with named entities and intents.

## models/..
This folder contains the models used for the NLU intent classification and entity extraction

## config_spacy.json
Contains the NLU pipeline

## nlu_model.py
This python file trains the NLU model using rasa

## shopassistant_domain.yml
Contains the slots, actions, entities and intents for OgwugoAssistant.
