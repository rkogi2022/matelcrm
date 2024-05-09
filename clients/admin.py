from django.contrib import admin
from .models import Prospects
from.models import Business
from .models import Receipt

admin.site.site_header="Matel Trading Co., Ltd Dashboard"
# Register your models here.
admin.site.register(Prospects)
admin.site.register(Business)
admin.site.register(Receipt)