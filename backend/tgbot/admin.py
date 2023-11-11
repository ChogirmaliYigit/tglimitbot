from django.contrib import admin
from .models import User as TelegramUser, Method, Field, AdsChat


@admin.register(TelegramUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "username", "telegram_id", )
    fields = ("full_name", "username", "telegram_id", )
    search_fields = ("full_name", "username", "telegram_id", )


admin.site.register(Method)
admin.site.register(Field)
admin.site.register(AdsChat)
