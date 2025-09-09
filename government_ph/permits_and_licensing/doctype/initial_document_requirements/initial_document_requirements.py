# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class InitialDocumentRequirements(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		approved_by: DF.Link | None
		approved_date: DF.Datetime | None
		document_name: DF.Link | None
		file: DF.Attach | None
		file_attached_by: DF.Link | None
		file_attachment_date: DF.Datetime | None
		file_resubmitted_by: DF.Link | None
		file_resubmitted_date: DF.Datetime | None
		notesremarks: DF.SmallText | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		rejected_by: DF.Link | None
		rejected_date: DF.Datetime | None
		required: DF.Check
		resubmitted_file: DF.Attach | None
		status: DF.Literal["Awaiting Submission", "Pending Review", "Approved", "Rejected", "For Resubmission"]
	# end: auto-generated types
	pass
