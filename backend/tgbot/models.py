from django.db import models


class User(models.Model):
    telegram_id = models.PositiveBigIntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "telegram_users"


class Method(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "methods"


class Field(models.Model):
    method = models.ForeignKey(Method, models.CASCADE)
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "fields"
        unique_together = ('method', 'name', )


class AdsChat(models.Model):
    chat_id = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.chat_id

    class Meta:
        db_table = "ads_chats"
