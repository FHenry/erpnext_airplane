# Copyright (c) 2023, scopen.fr and contributors
# For license information, please see license.txt

from random import choice, randint

import frappe
from frappe import _
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_insert(self):
		# <random-integer><random-capital-alphabet-from-A-to-E>
		self.seat = str(randint(1, 99)) + choice(["A", "B", "C", "D", "E", "F"])

	def validate(self):
		self.total_amount = 0
		extisting_addon_type = []
		to_keep_addon = []

		for addon in self.add_ons:
			if addon.item not in extisting_addon_type:
				extisting_addon_type.append(addon.item)
				to_keep_addon.append(addon)
				self.total_amount += addon.amount
			else:
				addon.delete()

		self.total_amount += self.flight_price

		self.update({"add_ons": to_keep_addon})

	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw(_("Cannot submit ticket with status different from Boarded"))
