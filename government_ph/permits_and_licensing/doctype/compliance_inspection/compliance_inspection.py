# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ComplianceInspection(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		actual_visit: DF.Date | None
		amended_from: DF.Link | None
		business_name: DF.Data | None
		business_owner: DF.Data | None
		business_permit_application: DF.Link | None
		departmentoffice: DF.Link | None
		inspected_by: DF.Link | None
		inspector_full_name: DF.Data | None
		long_text_zpbp: DF.LongText | None
		naming_series: DF.Literal[".YYYY.-CI-.#####"]
		rating: DF.Literal["", "Compliant", "Non-Compliant", "Partially Compliant", "Not Applicable (N/A)"]
		scheduled_visit: DF.Date | None
	# end: auto-generated types
	pass
