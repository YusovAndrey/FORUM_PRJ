from django.db import router
from django.urls import path, include
from rest_framework import routers
#from api.views import CheckBoxViewSet
from api import views



#router = routers.DefaultRouter()
#router.register('checkbox', CheckBoxViewSet)


urlpatterns = [
    #path('', include(router.urls)),
    path('checkbox_list', views.CheckBox_list, name="CheckBox list"),
    path('checkbox_list/<int:pk>', views.CheckBox_detail, name="CheckBox details"),
    path('checkbox_create', views.CheckBox_create, name="CheckBox create"),
    path('checkbox_update/<int:pk>', views.CheckBox_update, name="CheckBox update"),
    path('checkbox_delete/<int:pk>', views.CheckBox_delete, name="CheckBox delete"),
]