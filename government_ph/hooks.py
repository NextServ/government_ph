app_name = "government_ph"
app_title = "Government PH"
app_publisher = "SERVIO Technologies"
app_description = "An ERPNext Localization for Philippine Government/LGU"
app_email = "david@servio.ph"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "government_ph",
# 		"logo": "/assets/government_ph/logo.png",
# 		"title": "Government PH",
# 		"route": "/government_ph",
# 		"has_permission": "government_ph.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/government_ph/css/government_ph.css"
# app_include_js = "/assets/government_ph/js/government_ph.js"

# include js, css files in header of web template
# web_include_css = "/assets/government_ph/css/government_ph.css"
# web_include_js = "/assets/government_ph/js/government_ph.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "government_ph/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "government_ph/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "government_ph.utils.jinja_methods",
# 	"filters": "government_ph.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "government_ph.install.before_install"
# after_install = "government_ph.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "government_ph.uninstall.before_uninstall"
# after_uninstall = "government_ph.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "government_ph.utils.before_app_install"
# after_app_install = "government_ph.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "government_ph.utils.before_app_uninstall"
# after_app_uninstall = "government_ph.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "government_ph.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"government_ph.tasks.all"
# 	],
# 	"daily": [
# 		"government_ph.tasks.daily"
# 	],
# 	"hourly": [
# 		"government_ph.tasks.hourly"
# 	],
# 	"weekly": [
# 		"government_ph.tasks.weekly"
# 	],
# 	"monthly": [
# 		"government_ph.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "government_ph.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "government_ph.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "government_ph.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["government_ph.utils.before_request"]
# after_request = ["government_ph.utils.after_request"]

# Job Events
# ----------
# before_job = ["government_ph.utils.before_job"]
# after_job = ["government_ph.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"government_ph.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
	{
		"doctype": "Role",
		"filters": [
			[
				"name",
				"in",
				[
					"Barangay Officer",
					"BPLO Head",
					"DENR Officer",
					"Endorsing Officer",
					"Mayor",
					"BFP Officer",
					"Health/Sanitary Officer",
					"Engineer",
					"Zoning Officer",
					"Assessor",
					"Treasurer",
					"BPLO Officer",
				],
			]
		],
	},
	{"doctype": "PH Region"},
	{"doctype": "PH Province"},
	{"doctype": "PH City"},
	{"doctype": "PH Barangay"},
	{"doctype": "PH Postal Code"},
	{
		"doctype": "Workflow State",
		"filters": [
			[
				"state",
				"in",
				[
					"Partial Payment",
					"Awaiting Initial Document Submission",
					"For Endorsement to Ancillary Offices",
					"Saved as Draft",
					"Licensed Issued",
					"For Issuance",
					"For Payment",
					"For Approval",
					"For Assessment",
					"For Verification",
				],
			]
		],
	},
	{
		"doctype": "Workflow",
		"filters": [
			[
				"name",
				"in",
				[
					"Business Permit Application Workflow",
				],
			]
		],
	},
	{
		"doctype": "Workflow Action Master",
		"filters": [
			[
				"name",
				"in",
				[
					"Partial Payment",
					"Complete Document",
					"Approved by City Planning Office",
					"Approved by BFP",
					"Issue",
					"Paid",
					"Approve Assessment",
					"Approved and Completed Clearances",
					"Verified and Approved",
					"Submit Application",
				],
			]
		],
	},
	{"doctype": "Ancillary Documents Template"},
	{
		"doctype": "Role Profile",
		"filters": [
			[
				"name",
				"in",
				[
					"BPLO Officer",
					"Assessor",
					"Mayor",
					"Health/Sanitary Office",
					"Treasurer's Office",
					"City Engineer",
					"LGU - DENR Office",
					"LGU - Barangay",
					"BPLO Head",
					"LGU - BFP Office",
					"LGU - Zoning Office",
				],
			]
		],
	},
]
