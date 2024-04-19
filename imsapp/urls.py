from django.urls import path
from .views import *
urlpatterns = [
    path('company_info/',CompanyInfoApiView.as_view(),name='company info'),
    path('company_info/<int:pk>/',CompanyInfoIdApiView.as_view(),name='company info detail'),
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('admin_create/',admin_create,name='admin-create'),
    path('group/',GroupApiView.as_view(),name='group_list'),
    path('product_type/',ProductTypeApiView.as_view(),name='product type'),
    path('product_type/<int:pk>/',ProductTypeIdApiView.as_view(),name='product tyoe detail'),
    path('product_info/',ProductApiView.as_view(),name='product_info')



]