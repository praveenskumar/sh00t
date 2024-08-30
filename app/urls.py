from django.urls import re_path
from app import views

urlpatterns = [
    re_path(r'^flags/new/$', views.flags_new),
    re_path(r'^flags/all/', views.flags_all),
    re_path(r'^flags/open/', views.open_flags),
    re_path(r'^flag/([0-9]+)/$', views.flag),
    re_path(r'^sh0ts/new/$', views.sh0ts_new),
    re_path(r'^sh0ts/all/', views.sh0ts_all),
    re_path(r'^sh0t/([0-9]+)/$', views.sh0t),
    re_path(r'^assessments/new/$', views.assessments_new),
    re_path(r'^assessments/all/', views.assessments_all),
    re_path(r'^assessment/([0-9]+)/$', views.assessment),
    re_path(r'^projects/new/$', views.projects_new),
    re_path(r'^projects/all/', views.projects_all),
    re_path(r'^project/([0-9]+)/$', views.project),
    re_path(r'^templates/$', views.templates),
    re_path(r'^template/([0-9]+)/$', views.template),
    re_path(r'^case-masters/$', views.case_masters),
    re_path(r'^case-master/([0-9]+)/$', views.case_master),
    re_path(r'^module-masters/$', views.module_masters),
    re_path(r'^module-master/([0-9]+)/$', views.module_master),
    re_path(r'^methodology-masters/$', views.methodology_masters),
    re_path(r'^methodology-master/([0-9]+)/$', views.methodology_master),
]