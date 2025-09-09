# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessTaxPayment(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		date_of_payment: DF.Date | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		payment_mode: DF.Link | None
		reference_numbercode: DF.Data | None
		type: DF.Literal["Cash", "Check", "Bank Transfer", "Debit Card", "Credit Card", "Prepaid Card", "E-Wallet", "Others"]
	# end: auto-generated types
	pass
