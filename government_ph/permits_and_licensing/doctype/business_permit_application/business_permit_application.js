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
		clear_location_fields(frm, "");
	},
	province: function (frm) {
		clear_location_fields(frm, "", ["city", "barangay"]);
	},
	city: function (frm) {
		clear_location_fields(frm, "", ["barangay"]);
	},

	business_region: function (frm) {
		clear_location_fields(frm, "business_");
	},
	business_province: function (frm) {
		clear_location_fields(frm, "business_", ["city", "barangay"]);
	},
	business_city: function (frm) {
		clear_location_fields(frm, "business_", ["barangay"]);
	},

	lessor_region: function (frm) {
		clear_location_fields(frm, "lessor_");
	},
	lessor_province: function (frm) {
		clear_location_fields(frm, "lessor_", ["city", "barangay"]);
	},
	lessor_city: function (frm) {
		clear_location_fields(frm, "lessor_", ["barangay"]);
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
});

// ---------------- Helper Functions ----------------

// Setup query filters for region → province → city → barangay
function setup_location_queries(frm, prefix) {
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
