import frappe


def execute():
	doc = frappe.get_doc("Currency Exchange Settings")
	if doc.service_provider != "frankfurter.app":
		return

	doc.set_parameters_and_result()
	doc.flags.ignore_validate = True
	doc.save()