from flask import request, abort

from acct import db
from acct.model import Invoice
from acct.schema import InvoiceSchema


class InvoiceController:
    def get_invoices():
        invoices = Invoice.query.all()
        invoices_schema = InvoiceSchema(many=True)
        return {"invoices": invoices_schema.dump(invoices)}

    def get_invoice(invoice_id):
        invoice = Invoice.query.get(invoice_id)
        if invoice is None:
            abort(404)
        invoice_schema = InvoiceSchema()
        return {"invoice": invoice_schema.dump(invoice)}

    def create_invoice():
        json_data = request.get_json()
        invoice_schema = InvoiceSchema()
        try:
            data = invoice_schema.load(json_data)
        except:
            abort(400)
        invoice = Invoice(user_id=int(data["user_id"]), amount=int(data["amount"]))
        db.session.add(invoice)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500)
        return {"invoice": invoice_schema.dump(invoice)}, 201

    def update_invoice(invoice_id):
        json_data = request.get_json()
        invoice_schema = InvoiceSchema()
        try:
            data = invoice_schema.load(json_data)
        except:
            abort(400)
        invoice = Invoice.query.get(invoice_id)
        if invoice is None:
            abort(404)
        else:
            invoice.user_id = int(data["user_id"])
            invoice.amount = int(data["amount"])
            try:
                db.session.commit()
            except:
                db.session.rollback()
                abort(500)
            return {"message": "A Specific Invoice Updated"}, 204

    def delete_invoice(invoice_id):
        invoice = Invoice.query.get(invoice_id)
        if invoice is None:
            abort(404)
        db.session.delete(invoice)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            abort(500)
        return {"message": "A Specific Invoice Deleted"}, 204
