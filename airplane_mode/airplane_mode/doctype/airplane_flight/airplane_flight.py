# Copyright (c) 2023, scopen.fr and contributors
# For license information, please see license.txt

from random import randint

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"
		for ticket in frappe.get_all(
			"Airplane Ticket", filters={"flight": self.name, "status": ["!=", "Boarded"]}
		):
			t = frappe.get_doc("Airplane Ticket", ticket.name)
			t.status = "Boarded"
			t.submit()

	def get_rendom_price(self):
		return randint(1, 9999)
