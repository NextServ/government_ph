# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class BusinessPermitApplication(Document):
	def on_submit(self):
		if not self.date_of_application:
			self.date_of_application = nowdate()
			# ignore user permissions when writing directly
			self.flags.ignore_permissions = True
			self.db_update()
