from django.urls import path
from . import views

app_name = 'nugu'

urlpatterns = [
    path('health', views.health, name='health'),
    path('deadline', views.deadline, name='deadline'),
    path('d_univ', views.deadline, name='deadline'),
    path('d_univ_start', views.deadline, name='deadline'),
    path('d_univ_end', views.deadline, name='deadline'),
    path('d_univ_term', views.deadline, name='deadline'),
    path('d_univ_date', views.deadline, name='deadline'),
    path('d_univ_date_start', views.deadline, name='deadline'), 
    path('d_univ_date_end', views.deadline, name='deadline'),
    path('d_univ_date_term', views.deadline, name='deadline'),
# 수시원서
# ---------------------------------------------------------------------

    path('interview', views.interview, name='interview'),
    path('i_result', views.interview, name='interview'),
    path('i_result_empty', views.interview, name='interview'),
    
    path('i_univ_subject_typical', views.interview, name='interview'),
    path('i_univ_subject_typical_result', views.interview, name='interview'),
    path('i_univ_subject_typical_empty', views.interview, name='interview'),
    
    path('i_subject_univ_typical', views.interview, name='interview'),
    path('i_subject_univ_typical_result', views.interview, name='interview'),
    path('i_subject_univ_typical_empty', views.interview, name='interview'),
    
    path('i_typical_univ_subject', views.interview, name='interview'),
    path('i_typical_univ_subject_result', views.interview, name='interview'),
    path('i_typical_univ_subject_empty', views.interview, name='interview'),
    
    path('univ_subject_typical', views.interview, name='interview'),
    path('univ_subject_typical_result', views.interview, name='interview'),
    path('univ_subject_typical_empty', views.interview, name='interview'),
    
    path('univ_typical_subject', views.interview, name='interview'),
    path('univ_typical_subject_result', views.interview, name='interview'),
    path('univ_typical_subject_empty', views.interview, name='interview'),
    
    path('typical_subject_univ', views.interview, name='interview'),
    path('typical_subject_univ_result', views.interview, name='interview'),
    path('typical_subject_univ_empty', views.interview, name='interview'),
    
    path('i_total', views.interview, name='interview'),
    path('i_total_result', views.interview, name='interview'),
    path('i_total_empty', views.interview, name='interview'),
# 면접날짜
# ---------------------------------------------------------------------

    path('result', views.result, name='result'),
    path('r_result_first', views.result, name='result'),
    path('r_result_final', views.result, name='result'),
    path('r_result_empty', views.result, name='result'),
    
    path('r_univ_typical', views.result, name='result'),
    path('r_univ_typical_first', views.result, name='result'),
    path('r_univ_typical_final', views.result, name='result'),
    
    path('r_first_univ_typical', views.result, name='result'),
    path('r_first_univ_typical_result', views.result, name='result'),
    path('r_first_univ_typical_empty', views.result, name='result'),
    
    path('r_first_typical_univ', views.result, name='result'),
    path('r_first_typical_univ_result', views.result, name='result'),
    path('r_first_typical_univ_empty', views.result, name='result'),
    
    path('r_final_univ_typical', views.result, name='result'),
    path('r_final_typical_univ', views.result, name='result'),
    
    path('result_univ_typical', views.result, name='result'),
    path('result_univ_typical_first', views.result, name='result'),
    path('result_univ_typical_final', views.result, name='result'),
    path('result_univ_typical_first_empty', views.result, name='result'),

    path('r_univ_first_typical', views.result, name='result'),
    path('r_univ_first_typical_result', views.result, name='result'),
    path('r_univ_first_typical_empty', views.result, name='result'),
    
    path('r_univ_final_typical', views.result, name='result'),
    
    path('univ_typical', views.result, name='result'),
    path('univ_typical_first', views.result, name='result'),
    path('univ_typical_final', views.result, name='result'),
    path('univ_typical_first_empty', views.result, name='result'),
# 1차발표와 최종발표
]
