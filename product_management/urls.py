
from django.conf.urls import include, url
from django.contrib import admin
from product_management.views import CategoryView, UpdateCategoryView,\
    DisplayCategoryView, DeleteCategoryView, CreateProductView,\
    DisplayProductView, UpdateProductView, DeleteProductView, HomeView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomeView.as_view(),name='home'),
    url(r'^createCategory$', CategoryView.as_view(),name='create_category'),
    url(r'^listCategory$', DisplayCategoryView.as_view(),name='category_list'),
    url(r'^updateCategory/(\d+)/$', UpdateCategoryView.as_view(),name='update_category'),
    url(r'^deleteCategory/(\d+)/$', DeleteCategoryView.as_view(),name='delete_category'),
    
    url(r'^createProduct$', CreateProductView.as_view(),name='create_product'),
    url(r'^listProduct$', DisplayProductView.as_view(),name='product_list'),
    url(r'^updateProduct/(\d+)/$', UpdateProductView.as_view(),name='update_product'),
    url(r'^deleteProduct/(\d+)/$', DeleteProductView.as_view(),name='delete_product'),
]
