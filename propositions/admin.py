from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

from .models import Proposition

# Automatically register all models
app_models = apps.get_app_config('propositions').get_models()
for model in app_models:
    try: admin.site.register(model)
    except AlreadyRegistered: pass