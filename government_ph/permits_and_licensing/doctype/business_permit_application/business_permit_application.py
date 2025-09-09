# Copyright (c) 2025, SERVIO Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from frappe.utils import nowdate


class BusinessPermitApplication(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF
		from government_ph.government_ph.doctype.ancillary_requirements_table.ancillary_requirements_table import AncillaryRequirementsTable
		from government_ph.government_ph.doctype.measure_and_pax_details.measure_and_pax_details import MeasureandPaxDetails
		from government_ph.permits_and_licensing.doctype.business_tax_payment.business_tax_payment import BusinessTaxPayment
		from government_ph.permits_and_licensing.doctype.business_tax_table.business_tax_table import BusinessTaxTable
		from government_ph.permits_and_licensing.doctype.initial_document_requirements.initial_document_requirements import InitialDocumentRequirements
		from government_ph.permits_and_licensing.doctype.line_of_business_detail.line_of_business_detail import LineofBusinessDetail

		amended_from: DF.Link | None
		amount_received_by: DF.Link | None
		amount_received_by_full_name: DF.Data | None
		ancillary_verifications: DF.Table[AncillaryRequirementsTable]
		ancilliary_documents_template: DF.Link | None
		approved_by: DF.Link | None
		are_you_enjoying_tax_incentive_from_any_government_entity: DF.Literal["", "Yes", "No"]
		assessed_by: DF.Link | None
		barangay: DF.Link
		birthday: DF.Date
		building_name: DF.Data | None
		business_area: DF.Data
		business_barangay: DF.Link
		business_building_name: DF.Data | None
		business_city: DF.Link
		business_email_address: DF.Data | None
		business_house_no: DF.Data | None
		business_identification_number: DF.Data | None
		business_mobile_no: DF.Data | None
		business_name: DF.Data
		business_postal_code: DF.Link
		business_province: DF.Link
		business_region: DF.Link
		business_street: DF.Data | None
		business_subdivision: DF.Data | None
		business_tax: DF.Table[BusinessTaxTable]
		business_tax_assessment_template: DF.Link | None
		business_tax_payment: DF.Table[BusinessTaxPayment]
		business_telephone_no: DF.Data | None
		business_unit_no: DF.Data | None
		cda_date_of_registration: DF.Date | None
		cda_registration_no: DF.Data | None
		city: DF.Link
		contact_number: DF.Data
		contact_person_email_address: DF.Data | None
		ctc_no: DF.Data | None
		date_of_application: DF.Datetime | None
		dti_date_of_registration: DF.Date | None
		dti_registration_no: DF.Data | None
		email_address: DF.Data
		existing_business: DF.Link | None
		extension_name: DF.Data | None
		first_name: DF.Data
		full_name: DF.Data
		house_number: DF.Data | None
		initial_document_requirement: DF.Table[InitialDocumentRequirements]
		initial_requirement_documents_template: DF.Link | None
		is_the_place_of_business_rented: DF.Literal["", "Yes", "No"]
		is_the_registrant_the_business_owner: DF.Check
		last_name: DF.Data
		lessor_barangay: DF.Link | None
		lessor_building_name: DF.Data | None
		lessor_city: DF.Link | None
		lessor_contact_no: DF.Data | None
		lessor_email_address: DF.Data | None
		lessor_house_no: DF.Data | None
		lessor_postal_code: DF.Link | None
		lessor_province: DF.Link | None
		lessor_region: DF.Link | None
		lessor_street: DF.Data | None
		lessor_subdivision: DF.Data | None
		lessor_unit_no: DF.Data | None
		lessors_full_name: DF.Data | None
		line_of_business: DF.Table[LineofBusinessDetail]
		measure_and_pax_details: DF.Table[MeasureandPaxDetails]
		middle_name: DF.Data | None
		mobile_number: DF.Data
		monthly_rental: DF.Currency
		no_of_employees_in_establishment: DF.Data
		no_of_employees_residing_in_lgu: DF.Data
		no_of_female_employees_in_establishment: DF.Data | None
		no_of_male_employees_in_establishment: DF.Data | None
		payment_frequency: DF.Literal["Annually", "Bi-Annually", "Quarterly"]
		period_covered: DF.Data | None
		please_specify_the_entity: DF.Data | None
		postal_code: DF.Link
		property_index_number: DF.Data | None
		province: DF.Link
		region: DF.Link
		registrant_full_name: DF.Data | None
		rejected_by: DF.Link | None
		rejected_time: DF.Datetime | None
		rejection_reason: DF.SmallText | None
		relationship: DF.Data
		same_as_home_address: DF.Check
		sec_date_of_registration: DF.Date | None
		sec_registration_no: DF.Data | None
		sex: DF.Link
		street: DF.Data | None
		subdivision: DF.Data | None
		tax_identification_no: DF.Data
		telephone_number: DF.Data | None
		total_amount_due: DF.Currency
		total_due: DF.Currency
		total_paid_amount: DF.Currency
		trade_name: DF.Data | None
		type_of_application: DF.Literal["", "New", "Renewal", "Others"]
		type_of_business: DF.Literal["", "Single Proprietorship", "One Person Corporation", "Partnership", "Corporation", "Cooperative"]
		unit_no: DF.Data | None
	# end: auto-generated types
	def on_submit(self):
		if not self.date_of_application:
			self.date_of_application = nowdate()
			# ignore user permissions when writing directly
			self.flags.ignore_permissions = True
			self.db_update()
