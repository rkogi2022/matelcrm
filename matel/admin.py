from django.contrib import admin
from .models import CompanyExpenses
from .models import PersonalExpenses

admin.site.site_header="Matel Trading Co., Ltd Dashboard"

# Register your models here.
admin.site.register(CompanyExpenses)
admin.site.register(PersonalExpenses)
