# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('buy/<int:product_id>/', views.buy_product, name='buy_product'),
]
