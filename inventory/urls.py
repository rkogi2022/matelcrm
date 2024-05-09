from django.urls import path
from  . import views

app_name='inventory'

urlpatterns = [
        # Car make urls
    path('carmake/',views.carmake_list, name='carmake'),
    path('addcarmake/',views.create_carmake, name='addcarmake'),
    path('updatecarmake/<int:id>/', views.update_carmake, name='updatecarmake'),
    path('deletecarmake/<int:id>/', views.delete_carmake, name='deletecarmake'),

    # car models urls
    path('carmodel/',views.carmodel_list, name='carmodel'),
    path('addcarmodel/',views.addcarmodel, name='addcarmodel'),
    path('updatecarmodel/<int:id>/', views.update_carmodel, name='updatecarmodel'),
    path('deletecarmodel/<int:id>/', views.delete_carmodel, name='deletecarmodel'),
    
    #  stock urls-localstock
    path('stock/',views.stocklist, name='stock'),
    path('stock_searchbar/', views.stock_searchbar, name='stock_searchbar'),
    path('addstock/', views.add_stock, name='addstock'),
    path('updatestock/<int:id>/', views.update_stock, name='updatestock'),
    #  stock urls-japanstock
    path('japanstock/',views.japanstock, name='japanstock'),
    path('addjapanstock/', views.add_japanstock, name='addjapanstock'),
    path('updatejapanstock/<int:id>/', views.update_japanstock, name='updatejapanstock'),
    path('japanstock_searchbar/', views.japanstock_searchbar, name='japanstock_searchbar'),

    #receipts
    path('receiptsdetails/', views.receiptsdetails, name='receiptsdetails'),
    path('update_receipts/<int:id>/', views.update_receipts, name='update_receipts'),
    path('searchbyinvoice', views.search_by_invoice, name='searchbyinvoice'),

    #car expenses
    path('carexpenses_list/', views.carexpenses_list, name='carexpenses_list'),
    path('addexpense/', views.addexpense, name='addexpense'),
    path('updatecarexpenses/<int:id>/', views.update_carexpenses, name='updatecarexpenses'),
    path('searchcarexpenses', views.search_carexpenses, name='searchcarexpenses'),

         # leased cars urls
    path('leasedstock/',views.leasedstock_list, name='leasedstock'),
    path('addleasedcar/',views.add_leasedcars, name='addleasedcar'),
    path('updateleased/<int:id>/', views.update_leasedcars, name='updateleased'),
    path('leasedsearchbar/', views.leasedcars_searchbar, name='leasedsearchbar'),

]
