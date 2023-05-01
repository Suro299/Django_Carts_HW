from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name = "index"),
   path("cart/", views.cart, name = "cart"),
   path('login/', views.login_request, name='login'),
   path('register/',views.register_request, name='register'),
   path('logout/', views.logout_request, name='logout')
]