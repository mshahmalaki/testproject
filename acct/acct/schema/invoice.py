from acct import ma
from acct.model import Invoice


class InvoiceSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Invoice

    id = ma.auto_field(dump_only=True)
    user_id = ma.auto_field()
    amount = ma.auto_field()
