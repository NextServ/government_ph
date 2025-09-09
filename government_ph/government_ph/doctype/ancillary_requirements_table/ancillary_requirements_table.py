# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class AncillaryRequirementsTable(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		approved_by: DF.Link | None
		approved_date: DF.Datetime | None
		assigned_departmentoffice: DF.Data | None
		assigned_role: DF.Link | None
		clearance_no: DF.Data | None
		create_compliance_inspection: DF.Link | None
		document_title: DF.Link | None
		file: DF.Attach | None
		file_attached_by: DF.Link | None
		file_attachment_date: DF.Datetime | None
		full_name: DF.Data | None
		notesremarks: DF.SmallText | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		rejected_by: DF.Link | None
		rejected_date: DF.Datetime | None
		resubmitted_by: DF.Link | None
		resubmitted_date: DF.Datetime | None
		resubmitted_file: DF.Attach | None
		status: DF.Literal["Awaiting Submission", "For Inspection", "Pending Review", "Approved", "Rejected", "For Resubmission"]
		valid_from: DF.Date | None
		valid_until: DF.Date | None
	# end: auto-generated types
	pass
