from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    path('menu/', views.menu),
    path('index', views.index),
    path('menu_item/<str:dish>/', views.menu_item),
    re_path(r'^get_num/([0-9]{2})/$', views.get_num),
    path('login_form/', views.login_form_view),
    # Using generic view
    path('people', views.PeopleView.as_view())
    # path('people', views.people)
]
