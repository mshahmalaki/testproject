import requests
from flask import abort, current_app
from flask_restx import Resource


from acct.controller import InvoiceController


class InvoiceResource(Resource):
    def get(self, invoice_id=None, user_id=None):
        user_invoices = []
        if invoice_id is None:
            if user_id is None:
                return InvoiceController.get_invoices()
            else:
                response = requests.get(
                    current_app.config["AUTH_SERVICE_URL"] + f"/users/{user_id}"
                )
                INVOICES = InvoiceController.get_invoices()
                for user_invoice in INVOICES["invoices"]:
                    if user_invoice["user_id"] == user_id:
                        user_invoice["username"] = response.json()["user"]["username"]
                        user_invoice["address"] = response.json()["user"]["address"]
                        user_invoices.append(user_invoice)
                return {"user_invoices": user_invoices}
        else:
            return InvoiceController.get_invoice(invoice_id)


    def post(self, invoice_id=None):
        if invoice_id is None:
            return InvoiceController.create_invoice()
        else:
            abort(405)

    def put(self, invoice_id=None):
        if invoice_id is None:
            abort(405)
        else:
            return InvoiceController.update_invoice(invoice_id)

    def delete(self, invoice_id=None):
        if invoice_id is None:
            abort(405)
        else:
            return InvoiceController.delete_invoice(invoice_id)
