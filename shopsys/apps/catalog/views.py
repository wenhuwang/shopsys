#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404
from  .models import Category,Product

# Create your views here.
def index(request,template_name):
    page_title = '产品分类目录'
    return render(request,template_name,locals())

def show_category(request,category_slug,template_name):
    c_obj = get_object_or_404(Category,slug=category_slug)
    products = c_obj.product_set.all()
    page_title = c_obj.name
    meta_keywords = c_obj.meta_keywords
    meta_description = c_obj.meta_description
    return render(request,template_name,locals())

def show_product(request,product_slug,template_name):
    p_obj = get_object_or_404(Product,slug=product_slug)
    categories = p_obj.categories.filter(is_active=True)
    page_title = p_obj.name
    meta_keywords = p_obj.meta_keywords
    meta_description = p_obj.meta_description
    return render(request,template_name,locals())
