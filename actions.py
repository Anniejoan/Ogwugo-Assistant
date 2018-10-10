from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_laterals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class ActionProductSearch(Action):
	def name(self):
		return 'action_Product_search'

	

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



		# narrow the search space to items sold by that store


