from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name="homepage"),
    path('news',views.news, name="newspage")

]
