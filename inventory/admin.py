from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import CarMake
from.models import CarModel
from .models import Stock
from .models import JapanStock
from .models import Receipts
from .models import CarExpenses
from .models import LeasedStock

from .resources import CarMakeResource
from .resources import CarModelResource
from .resources import StockResource
from .resources import JapanStockResource

admin.site.site_header="Matel Trading Co., Ltd Dashboard"

# Register your models here.
class CarMakeAdmin(ImportExportModelAdmin):
    resource_class = CarMakeResource
admin.site.register(CarMake, CarMakeAdmin)

class CarModelAdmin(ImportExportModelAdmin):
    resource_class = CarModelResource
admin.site.register(CarModel, CarModelAdmin)

class StockAdmin(ImportExportModelAdmin):
    resource_class=StockResource
admin.site.register(Stock, StockAdmin)

class JapanStockAdmin(ImportExportModelAdmin):
    resource_class=JapanStockResource
admin.site.register(JapanStock, JapanStockAdmin)

admin.site.register(Receipts)
admin.site.register(CarExpenses)
admin.site.register(LeasedStock)