import frappe


def execute():
	doc = frappe.get_doc("Currency Exchange Settings")
	if doc.service_provider != "frankfurter.app":
		return

	set_parameters_and_result(doc)
	doc.flags.ignore_validate = True
	doc.save()


def set_parameters_and_result(doc):
	if doc.service_provider == "exchangerate.host":
		if not doc.access_key:
			frappe.throw(
				_("Access Key is required for Service Provider: {0}").format(
					frappe.bold(doc.service_provider)
				)
			)

		doc.set("result_key", [])
		doc.set("req_params", [])

		doc.api_endpoint = get_api_endpoint(doc.service_provider, doc.use_http)
		doc.append("result_key", {"key": "result"})
		doc.append("req_params", {"key": "access_key", "value": doc.access_key})
		doc.append("req_params", {"key": "amount", "value": "1"})
		doc.append("req_params", {"key": "date", "value": "{transaction_date}"})
		doc.append("req_params", {"key": "from", "value": "{from_currency}"})
		doc.append("req_params", {"key": "to", "value": "{to_currency}"})
	elif doc.service_provider == "frankfurter.app":
		doc.set("result_key", [])
		doc.set("req_params", [])

		doc.api_endpoint = get_api_endpoint(doc.service_provider, doc.use_http)
		doc.append("result_key", {"key": "rates"})
		doc.append("result_key", {"key": "{to_currency}"})
		doc.append("req_params", {"key": "base", "value": "{from_currency}"})
		doc.append("req_params", {"key": "symbols", "value": "{to_currency}"})