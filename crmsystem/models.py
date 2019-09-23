from mongoengine import Document, EmbeddedDocument, fields


class Order(EmbeddedDocument):
    orderId = fields.StringField(max_length=10, required=True, null=False)
    orderDate = fields.DateTimeField()
    billingAddress = fields.StringField(
        max_length=255, required=True, null=True)
    units = fields.IntField()
    amount = fields.IntField()
    remarks = fields.StringField(max_length=255, required=False)

class Customer(Document):
    customerId = fields.StringField(max_length=10, required=True, null=False)
    customerName = fields.StringField(max_length=100, required=True)
    credit = fields.IntField()
    status = fields.BooleanField()
    remarks = fields.StringField(max_length=255, required=False)
    orders = fields.EmbeddedDocumentListField(Order)
