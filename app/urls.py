# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 16:52:10 2018

@author: Prasad
"""

from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^markup/$',views.process),
    url(r'^$',views.home)
]
