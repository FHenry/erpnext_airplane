# Copyright (c) 2023, scopen.fr and contributors
# For license information, please see license.txt

from random import choice, randint

import frappe
from frappe import _
from frappe.model.document import Document


class AirplaneTicket(Document):
	def before_insert(self):
		# <random-integer><random-capital-alphabet-from-A-to-E>
		# self.seat = str(randint(1, 99)) + choice(["A", "B", "C", "D", "E", "F"])

		seats_booked = []
		# find other ticket from the same plane
		for ticket in frappe.get_all(self.doctype, filters={"flight": self.flight}):
			if ticket.seat:
				seats_booked.append(ticket.seat)

		find_available_seat = False
		plane_place = 50
		try_find_place = 1
		while find_available_seat is False:
			self.seat = str(randint(1, 99)) + choice(["A", "B", "C", "D", "E", "F"])
			if self.seat not in seats_booked:
				find_available_seat = True

			try_find_place += 1

			if try_find_place >= plane_place:
				frappe.throw("No More seat available on this flight")

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

		self.total_amount += int(self.flight_price)

		self.update({"add_ons": to_keep_addon})

	def on_submit(self):
		if self.status != "Boarded":
			frappe.throw(_("Cannot submit ticket with status different from Boarded"))
