from import_export import resources
from .models import CarMake, CarModel, Stock, JapanStock

class CarMakeResource(resources.ModelResource):
    class Meta:
        model = CarMake

class CarModelResource(resources.ModelResource):
    class Meta:
        model = CarModel

class StockResource(resources.ModelResource):
    class Meta :
        model = Stock

class JapanStockResource(resources.ModelResource):
    class Meta:
        model=JapanStock
