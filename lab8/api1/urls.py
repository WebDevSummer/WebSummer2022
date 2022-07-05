from django.urls import path
from api1.views import hello, api, product, category, product_detail, category_detail




urlpatterns = [
    # path('hi/', hello),
    # path('api1/', api),
    path('newproduct/', product),
    path('newproduct/<int:product_id>/', product_detail),
    path('newcategories/<int:category_id>/', category_detail),
    path('newcategories/', category)
]