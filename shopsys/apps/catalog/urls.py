#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,{'template_name':'catalog/index.html'},
        'catalog_home'),
    url(r'^catagory/(?P<category_slug>[-\w]+)/$',views.show_category,
        {'template_name':'catalog/category.html'},'catalog_category'),
    url(r'^product/(?P<category_slug>[-\w]+)/$',views.show_product,
        {'template_name':'catalog/product.html'},'catalog_product'),

]
