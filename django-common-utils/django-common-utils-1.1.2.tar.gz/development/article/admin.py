from django.contrib import admin

from django_common_utils.libraries.fieldsets import DefaultAdminMixin
from django_common_utils.libraries.fieldsets.mixins import TitleAdminFieldsetMixin
from .models import Article


class ArticleAdmin(DefaultAdminMixin):
    mixins = [
        TitleAdminFieldsetMixin,
    ]
    fieldset_fields = {
        "default": ["clicks", "...!"]
    }


admin.site.register(Article, ArticleAdmin)
