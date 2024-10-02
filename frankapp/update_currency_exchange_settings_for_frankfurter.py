import frappe


def execute():
	doc = frappe.get_doc("Currency Exchange Settings")
	if doc.service_provider != "frankfurter.app":
		return

	set_parameters_and_result(doc)
	doc.flags.ignore_validate = True
	doc.save()