from django.urls import path, include
from . import views
from rest_framework import routers

# router=routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
urlpatterns = [
    # path('',views.index, name='index'),
    # path('', include(router.urls)),
    path('', views.flight_list),
    path('<int:primary_key>/', views.flight_detail)

]
