# Copyright (c) 2023, scopen.fr and contributors
# For license information, please see license.txt

from random import randint

from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Complete"

	def get_rendom_price(self):
		return randint(1, 9999)
