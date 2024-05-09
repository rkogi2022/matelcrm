from django.urls import path
from  . import views

app_name='matel'


urlpatterns = [
    # office expenses urls
    path('officeexpenseslist/', views.officeexpenses_list, name='officeexpenseslist'),
    path('addofficeexpense/', views.add_officeexpense, name='addofficeexpense'),
    path('updateofficeexpense/<int:id>/',views.update_officeexpense, name='updateofficeexpense'),
    path('searchofficeexpense', views.search_officeexpense, name='search_officeexpense'),

    # personal expenses urls
    path('personalexpenseslist', views.personalexpenses_list, name='personalexpenseslist'),
    path('addpersonalexpense/', views.add_personalexpense, name='addpersonalexpense'),
    path('updatepersonalexpense/<int:id>/',views.update_personalexpense, name='updatepersonalexpense'),
    path('searchpersonalexpense', views.search_personalexpense, name='searchpersonalexpense'),
]