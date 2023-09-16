# Copyright (c) 2023, scopen.fr and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AirplaneFlight(Document):
	def on_submit(self):
		self.status = "Complete"
