# models.py
from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    telegram_id = fields.CharField(max_length=50, unique=True)
    gamepts = fields.IntField(default=0)

    class Meta:
        table = "user"
