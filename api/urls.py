from django.urls import re_path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    re_path(r'^flag/(?P<pk>[0-9]+)', views.flag_detail),
    re_path(r'^flags/', views.flag_list),
    re_path(r'^sh0t/(?P<pk>[0-9]+)', views.sh0t_detail),
    re_path(r'^sh0ts/', views.sh0t_list),
    re_path(r'^assessment/(?P<pk>[0-9]+)', views.assessment_detail),
    re_path(r'^assessments/', views.assessment_list),
    re_path(r'^project/(?P<pk>[0-9]+)', views.project_detail),
    re_path(r'^projects/', views.project_list),
    re_path(r'^template/(?P<pk>[0-9]+)', views.template_detail),
    re_path(r'^templates/', views.template_list),
    re_path(r'^case-master/(?P<pk>[0-9]+)', views.case_master_detail),
    re_path(r'^case-masters/', views.case_master_list),
    re_path(r'^module-master/(?P<pk>[0-9]+)', views.module_master_detail),
    re_path(r'^module-masters/', views.module_master_list),
    re_path(r'^methodology-master/(?P<pk>[0-9]+)', views.methodology_master_detail),
    re_path(r'^methodology-masters/', views.methodology_master_list),
]
urlpatterns = format_suffix_patterns(urlpatterns)
