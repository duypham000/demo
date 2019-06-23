from django.urls import path
# import views
from . import views

# tạo path
urlpatterns = [
    # khi người dùng gõ path, method index của views sẽ được gọi
    path('', views.index),
]
