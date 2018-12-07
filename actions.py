from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_laterals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionProductSearch(Action):
	def name(self):
		return 'action_Product_search'

	def run(self,dispatcher,tracker,domain):
		import requests

		# Sample Basic Auth Url with login values as username and password
		user = "ogwugo_service"
		passwd = "g578276dsffdba"
		product_name = tracker.get_slot('Product')
		url = "https://ogwugo.net/api/v2/machine/resources/product/search/by/name?q={product_name}"

		# Make a request to the endpoint using the correct auth values
		auth_values = (user, passwd)
		response = requests.get(url, auth=auth_values)

		# Convert JSON to dict and print
		print(response.json())

	

		# get top 5 product names and their prices


class ActionUserSearch(Action):
	def name(self):
		return 'action_User_search'


		# get user phone number and address 
		# return Telephone
		# return Address


class ActionStoreSearch(Action):
	def name(self):
		return 'action_User_search'

	def run(self,dispatcher,tracker,domain):
		import requests

		# Sample Basic Auth Url with login values as username and password
		user = "ogwugo_service"
		passwd = "g578276dsffdba"
		product_name = tracker.get_slot('Product')
		store_name = tracker.get_slot('Store')
		url = "https://ogwugo.net/api/v2/machine/resources/product/search/by/name?q={product_name}"

		# Make a request to the endpoint using the correct auth values
		auth_values = (user, passwd)
		response = requests.get(url, auth=auth_values)

		# Convert JSON to dict and print
		print(response.json())


		# narrow the search space to items sold by that store
		return 'ActionStoreSearch'
	

run action_product_search(Action)
