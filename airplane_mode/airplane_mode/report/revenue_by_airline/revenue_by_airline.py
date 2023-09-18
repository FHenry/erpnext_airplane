# Copyright (c) 2023, scopen.fr and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.query_builder.functions import IfNull, Sum


def execute(filters=None):
	columns = get_columns()
	data = get_data()
	chart_data = prepare_chart_data(data)
	report_summary = get_report_sumary(data)

	return columns, data, None, chart_data, report_summary


def get_columns():
	columns = [
		{
			"label": _("Airline"),
			"fieldname": "airline",
			"fieldtype": "Link",
			"options": "Airline",
			"width": 160,
		},
		{
			"label": _("Revenue"),
			"fieldname": "total_income",
			"fieldtype": "Currency",
			"options": "EUR",
			"width": 130,
			"convertible": "rate",
		},
	]

	return columns


def get_data():
	ticket = frappe.qb.DocType("Airplane Ticket")
	flight = frappe.qb.DocType("Airplane Flight")
	plane = frappe.qb.DocType("Airplane")
	airline = frappe.qb.DocType("Airline")

	query = (
		frappe.qb.from_(airline)
		.left_join(plane)
		.on(airline.name == plane.airline)
		.left_join(flight)
		.on(flight.airplane == plane.name)
		.left_join(ticket)
		.on(ticket.flight == flight.name)
		.select(
			airline.name.as_("airline"),
			IfNull(Sum(ticket.total_amount), 0).as_("total_income"),
		)
		.groupby(plane.airline)
	)

	return query.run(as_dict=True)


def prepare_chart_data(data):
	labels = []
	amount = []
	for row in data:
		labels.append(row.airline)
		amount.append(row.total_income)

	return {
		"data": {"labels": labels, "datasets": [{"values": amount}]},
		"type": "donut",
		"height": 300,
	}


def get_report_sumary(data):
	total_income = 0
	for row in data:
		total_income += float(row.total_income)

	return [
		{
			"value": total_income,
			"label": _("Total Revenue"),
			"indicator": "Green" if total_income > 0 else "Red",
			"datatype": "Currency",
			"currency": "EUR",
		},
	]
