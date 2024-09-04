from django.contrib import admin

from .models import User, Language
from .translations import LanguageTranslationOptions


admin.site.register(User)
admin.site.register(Language)
