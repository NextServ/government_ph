// Copyright (c) 2025, SERVIO Technologies and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Business Permit Application", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Business Permit Application", {
	refresh: function (frm) {
		// Setup cascading queries for Applicant, Business, Lessor
		setup_location_queries(frm, ""); // Applicant (no prefix)
		setup_location_queries(frm, "business_");
		setup_location_queries(frm, "lessor_");
	},

	// Trigger clear functions dynamically
	region: function (frm) {
		setup_location_queries(frm, "", ["province", "city", "barangay"]);
	},
	province: function (frm) {
		setup_location_queries(frm, "", ["city", "barangay"]);
	},
	city: function (frm) {
		setup_location_queries(frm, "", ["barangay"]);
	},

	// Business Information
	same_as_home_address: function(frm) {
        // Check if the same_as_home_address checkbox is enabled
        if (frm.doc.same_as_home_address) {
            // Copy home address fields to business address fields
            frm.set_value('business_region', frm.doc.region);
            frm.set_value('business_province', frm.doc.province);
            frm.set_value('business_city', frm.doc.city);
            frm.set_value('business_barangay', frm.doc.barangay);
            frm.set_value('business_postal_code', frm.doc.postal_code);

            frm.set_value('business_house_no', frm.doc.house_number);
            frm.set_value('business_unit_no', frm.doc.unit_no);
            frm.set_value('business_building_name', frm.doc.building_name);
            frm.set_value('business_street', frm.doc.street);
            frm.set_value('business_subdivision', frm.doc.subdivision);
        }
    },

	business_region: function (frm) {
		if (frm.doc.same_as_home_address) return
		setup_location_queries(frm, "business_", ["province", "city", "barangay"]);
	},
	business_province: function (frm) {
		if (frm.doc.same_as_home_address) return
		setup_location_queries(frm, "business_", ["city", "barangay"]);
	},
	business_city: function (frm) {
		if (frm.doc.same_as_home_address) return
		setup_location_queries(frm, "business_", ["barangay"]);
	},

	lessor_region: function (frm) {
		setup_location_queries(frm, "lessor_", ["province", "city", "barangay"]);
	},
	lessor_province: function (frm) {
		setup_location_queries(frm, "lessor_", ["city", "barangay"]);
	},
	lessor_city: function (frm) {
		setup_location_queries(frm, "lessor_", ["barangay"]);
	},

	before_workflow_action: function (frm) {
		if (frm.selected_workflow_action === "Reject") {
			frappe.prompt(
				[
					{
						fieldtype: "Small Text",
						reqd: true,
						fieldname: "rejection_reason",
						label: __("Reason for Rejection"),
					},
				],
				function (values) {
					frappe.call({
						method: "frappe.client.set_value",
						args: {
							doctype: frm.doctype,
							name: frm.docname,
							fieldname: "rejection_reason",
							value: values.rejection_reason,
						},
						callback: function (response) {
							if (response && !response.exc) {
								frm.reload_doc(); // Refresh the form
								frappe.msgprint(__("Rejection reason saved."));
							} else {
								frappe.msgprint(
									__("Failed to save rejection reason. Please try again.")
								);
							}
						},
					});
				},
				__("Reason for Rejection"),
				__("Submit")
			);
			frappe.validated = false;
		}
	},
	type_of_application: function (frm) {
		// Trigger helper when type_of_application changes
		toggle_line_of_business_fields(frm);
	},
	ancilliary_documents_template: function (frm) {
		if (frm.doc.ancilliary_documents_template) {
			frappe.db
				.get_doc("Ancillary Documents Template", frm.doc.ancilliary_documents_template)
				.then((doc) => {
					// Clear existing rows
					frm.clear_table("ancillary_verifications");

					// Loop through template's child table (link_dazm)
					(doc.link_dazm || []).forEach((d) => {
						let row = frm.add_child("ancillary_verifications");
						row.document_title = d.document_title;
						row.assigned_departmentoffice = d.assigned_departmentoffice;
						row.assigned_role = d.assigned_role;
						row.status = d.status;
						row.notesremarks = d.notesremarks;
						row.clearance_no = d.clearance_no;
						row.valid_from = d.valid_from;
						row.valid_until = d.valid_until;
						row.create_compliance_inspection = d.create_compliance_inspection;
					});

					frm.refresh_field("ancillary_verifications");
				});
		} else {
			// If template is cleared, wipe the table
			frm.clear_table("ancillary_verifications");
			frm.refresh_field("ancillary_verifications");
		}
	},
	initial_requirement_documents_template: function (frm) {
		if (frm.doc.initial_requirement_documents_template) {
			frappe.db
				.get_doc(
					"Initial Requirement Documents Template",
					frm.doc.initial_requirement_documents_template
				)
				.then((doc) => {
					// Clear existing rows
					frm.clear_table("initial_document_requirement");

					// Loop through template's child table (initial_requirement_checklist)
					(doc.initial_requirement_checklist || []).forEach((d) => {
						let row = frm.add_child("initial_document_requirement");
						row.document_name = d.document_name;
						row.required = d.required;
						row.status = d.status;
						row.notesremarks = d.notesremarks;
						row.file_attached_by = d.file_attached_by;
						row.file_resubmitted_by = d.file_resubmitted_by;
					});

					frm.refresh_field("initial_document_requirement");
				});
		} else {
			// If template is cleared, wipe the table
			frm.clear_table("initial_document_requirement");
			frm.refresh_field("initial_document_requirement");
		}
	},
});

// ---------------- Helper Functions ----------------

// Setup query filters for region → province → city → barangay
function setup_location_queries(frm, prefix, to_clear) {
	frm.set_query(prefix + "province", function () {
		return {
			filters: { region: frm.doc[prefix + "region"] },
		};
	});
	frm.set_query(prefix + "city", function () {
		return {
			filters: { province: frm.doc[prefix + "province"] },
		};
	});
	frm.set_query(prefix + "barangay", function () {
		return {
			filters: { city: frm.doc[prefix + "city"] },
		};
	});

	if(to_clear){
		to_clear.forEach(field => {
			frm.set_value(prefix + field, '')
		})
	}
}

function toggle_line_of_business_fields(frm) {
	let hide_fields = frm.doc.type_of_application === "New";

	// Hide in form editor (child row popup)
	frm.fields_dict.line_of_business.grid.toggle_display("essential", !hide_fields);
	frm.fields_dict.line_of_business.grid.toggle_display("non_essential", !hide_fields);

	// Hide in grid/list view
	frm.fields_dict.line_of_business.grid.update_docfield_property(
		"essential",
		"in_list_view",
		!hide_fields
	);
	frm.fields_dict.line_of_business.grid.update_docfield_property(
		"non_essential",
		"in_list_view",
		!hide_fields
	);

	// Refresh grid to apply
	frm.fields_dict.line_of_business.grid.refresh();
}

frappe.ui.form.on("Business Tax Table", {
	amount_due: function (frm, cdt, cdn) {
		calculate_total_business_tax(cdt, cdn, frm);
		calculate_total_due(frm);
	},
	penaltysurcharge: function (frm, cdt, cdn) {
		calculate_total_business_tax(cdt, cdn, frm);
		calculate_total_due(frm);
	},
});

function calculate_total_business_tax(cdt, cdn, frm) {
	let row = locals[cdt][cdn];
	row.total = (row.amount_due || 0) + (row.penaltysurcharge || 0);
	frm.refresh_field("business_tax");
}

function calculate_total_due(frm) {
	let total_due = 0;

	(frm.doc.business_tax || []).forEach((row) => {
		total_due += row.total || 0;
	});

	frm.set_value("total_due", total_due);
}
