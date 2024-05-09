from django.urls import path
from  . import views

app_name='clients'

urlpatterns = [
    #prospects meodel urls
    path('prospectslist/', views.prospects_list, name='prospectslist'),
    path('addprospect/', views.add_prospect, name='addprospect'),
    path('updateprospect/<int:id>/', views.update_prospect, name='updateprospect'),

    #business model urls
    path('businesslist/', views.business_list, name='businesslist'),
    path('addbusiness/', views.add_business, name='addbusiness'),
    path('updatebusiness/<int:id>/', views.update_business, name='updatebusiness'),
    path('proformainvoice/<int:id>/', views.proforma, name='proformainvoice'),
    path('finalinvoice/<int:id>/', views.finalinvoice, name='finalinvoice'),
    path('salesagreement/<int:id>/', views.salesagreement, name='salesagreement'),

    # Receipts model Urls
    path('receiptslist/',views.receipts_list, name='receiptslist'),
    path('addreceipt/', views.add_receipt, name='addreceipt'),
    path('updatereceipt/<int:id>/', views.update_receipt, name='updatereceipt'),
    path('transactionalreport/', views.transactional_report, name='transactionalreport'),
]