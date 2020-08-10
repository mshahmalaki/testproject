from acct import api
from acct.view.invoices import InvoiceResource


api.add_resource(InvoiceResource, "/invoices", methods=["GET", "POST", "PUT", "DELETE"])
api.add_resource(InvoiceResource, "/invoices/<int:invoice_id>", methods=["GET", "POST", "PUT", "DELETE"])
api.add_resource(InvoiceResource, "/user_invoices/<int:user_id>", methods=["GET"])
