from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import requests
import json


class ActionProductSearch(Action):

	def name(self):
		return 'action_Product_search'

	def run(self, dispatcher, tracker, domain):
		# Sample Basic Auth Url with login values as username and password
		user = "ogwugo_service"
		passwd = "g578276dsffdba"
		product_name = tracker.get_slot('Product')
		url = "https://ogwugo.net/api/v2/machine/resources/product/search/by/name?q={product_name}"

		# Make a request to the endpoint using the correct auth values
		auth_values = (user, passwd)
		response = requests.get(url, auth=auth_values)

		# Convert JSON to dict and print

		product_dict = json.loads(response.content.decode())
		Products = product_dict['data']
		name_value = Products[0]['name']
		stock_status = Products[0]["in_stock"]
		store_value = Products[0]["store_name"]
		prodct_type = Products[0]["product_type"]

		if stock_status == 1:
			# reply = """" {} sold by {} is currently available for delivery.""".format(name_value, store_value)
			dispatcher.utter_message("""" {} sold by {} is currently available for delivery.""".format(name_value, store_value))
		else:
			# reply =  "" {name_value} sold by {store_value} is currently unavailable for delivery."
			dispatcher.utter_message(" {name_value} sold by {store_value} is currently available for delivery.")

		return [SlotSet('Product', product_name)]

		# get top 5 product names and their prices


#class ActionUserSearch(Action):
	#def name(self):
		#return 'action_user_search'

     #def run(self, dispatcher, tracker, domain):
		#Sample Basic Auth Url with login values as username and password
	  	#user = "ogwugo_service"
		#passwd = "g578276dsffdba"
		#user_name = tracker.get_slot('Username')
		#url = "https://ogwugo.net/api/v2/machine/resources/users/buyers?user_name={user_name]"
		#response = requests.get(url, auth=auth values)
		#user_dict = json.loads(response.content.decode())
		#User = user_dict['data']
		#Telephone = User["phone"]
		#location = User["addresses"]["address"]
	# get user phone number and address
		# return Telephone
		# return Address


#class ActionStoreSearch(Action):
	#def name(self):
	#	return 'action_store_search'

#	def run(self, dispatcher, tracker, domain):
#		import requests

		# Sample Basic Auth Url with login values as username and password
	#	user = "ogwugo_service"
	#	passwd = "g578276dsffdba"
	#	store_name = tracker.get_slot('Store')
	#	product_name = tracker.get_slot('Product')
	#	url = "https://ogwugo.net/api/v2/machine/resources/product/search/store/search/{store_name}/{product_name}"
#
		# Make a request to the endpoint using the correct auth values
#		response = requests.get(url, auth=auth_values)

		# Convert JSON to dict and print
#		print(response.json())


		# narrow the search space to items sold by that store
#		return 'ActionStoreS

