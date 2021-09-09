from mongoengine import Document, StringField, DateTimeField, SequenceField
import datetime
class User(Document):
    user_id = SequenceField(required=True, primary_key=True)
    name = StringField(required=True)
    time  = DateTimeField(default=datetime.datetime.now)
    