from django.urls import path
from . import views

app_name = 'SuperMarket1'

urlpatterns = [
	path('', views.all_products, name='all_products'),
	path('maincatopros/<int:mc_id>/', views.Main_catogory_product_list, name='main_catogory_product_list'),
	path('prodcatopros/<int:pc_id>/', views.Prod_catogory_product_list, name='prod_catogory_product_list'),
	path('cart/', views.view_cart, name='view_cart'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('itempage/<int:p>/', views.itempage, name='itempage'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
	path('remove_one/<int:item_id>/', views.remove_one_from_cart, name='remove_one_from_cart'),
    path('logine/',views.user_logine,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('signup/',views.user_signup,name='user_signup'),
    path('search/',views.search,name='search'),
    path('prosearch/',views.Prodsearch,name='Prodsearch'),
    path('amc/',views.addMainCat,name='amc'),
    path('apc/',views.addProdCat,name='apc'),
    path('ap/',views.addProducts,name='ap'),
    path('mnbvcstoreroom/',views.storeroom,name='storeroom'),

]
