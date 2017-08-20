"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from company.views import *

urlpatterns = [
    url(r'^get_company_list/$',CompanyList.as_view(),name='company_listing'),
    url(r'^get_company_details/(?P<profile_id>[0-9]+)/$',CompanyDetail.as_view(),name='company_detail'),
    url(r'^post_company_details/$',CompanyDetailPost.as_view(),name='company_detail_post'),
    url(r'^post_funding_details/$',FundingDetailPost.as_view(),name='funding_detail_post'),
    url(r'^post_company_detailshtml/$',CompanyDetailPost2.as_view(),name='company_detail_post2'),
]
