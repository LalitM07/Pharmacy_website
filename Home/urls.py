from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
url(r'^$', views.Home,name="home"),
url(r'^signin/', views.signin,name="signin"),
url(r'^login/', views.login_user,name="login"),
url(r'^logout_user/', views.logout_user,name="logout_user"),
url(r'^removecartitem/(?P<pid>[0-9]+)/$',views.removecartitem, name = "removecartitem"),

url(r'^register/', views.UserFormView.as_view(), name="register"),
url(r'^mail/', views.mail, name="mail"),
url(r'^prescription/', views.prescriptiontable, name="prescription"),
url(r'^baby/', views.babytable, name="baby"),
url(r'^personal/', views.personaltable, name="personal"),
url(r'^wellness/', views.wellnesstable, name="wellness"),
url(r'^health/', views.aidtable, name="health"),
url(r'^cart/', views.viewcart, name="cart"),
url(r'^details/(?P<pid>[0-9]+)/$', views.detailsfunction, name="details"),
url(r'^details/cart/', views.addtocart, name="cartf"),
url(r'^checkout/', views.checkout,name="checkout"),
url(r'^contactus/',views.contactus,name = 'contactus'),
#admin part
url(r'^admin_profile/', views.admin_profile,name="admin_profile"),
url(r'^allorders/', views.allorders,name="allorders"),
url(r'^customers/', views.customers,name="customers"),
url(r'^suppliers/', views.suppliers,name="suppliers"),
url(r'^supply_details/(?P<suppid>[0-9]+)/$',views.supply_details,name='supply_details'),
url(r'^view_customer_orders/(?P<uid>[0-9]+)/$',views.view_customer_orders,name = 'view_customer_orders'),
url(r'^employees/', views.employees,name="employees"),
url(r'^add_employee/',views.add_employee,name='add_employee'),
url(r'^remove_employee/(?P<emplid>[0-9]+)/$',views.remove_employee,name = 'remove_employee'),
url(r'^insertemployee/',views.insertemployee,name = 'insertemployee'),
url(r'^viewfeedback',views.viewfeedback,name ='viewfeedback'),
url(r'^stock_products/',views.stock_products,name='stock_products'),
url(r'^addstock/',views.addstock,name='addstock'),
url(r'^add_products_to_stock/',views.add_products_to_stock,name='add_products_to_stock'),
]

