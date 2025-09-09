# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BusinessTaxAssessmentTemplate(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from government_ph.permits_and_licensing.doctype.business_tax_table.business_tax_table import BusinessTaxTable

		business_tax: DF.Table[BusinessTaxTable]
		company: DF.Link | None
		default: DF.Check
		disabled: DF.Check
		template_name: DF.Data
	# end: auto-generated types
	pass
