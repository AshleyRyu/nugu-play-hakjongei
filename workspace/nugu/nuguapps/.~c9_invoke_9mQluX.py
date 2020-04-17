import pprint
import json
import requests

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import School,

# Create your views here.
def health(request):
    return JsonResponse({})
    

def call(request):
    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    pprint.pprint(nugu_body)
    
    if nugu_body.get('action').get('parameters').get('call_appname'):
        
    
def deadline(request):
    pprint.pprint(request.body)
    
    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    pprint.pprint(nugu_body)
    
    name=''
    time=''
    # 1. school 정보 DB에 접근
    if nugu_body.get('action').get('parameters').get('univ'):
        nugu_univ = nugu_body.get('action').get('parameters').get('univ').get('value')
        print(nugu_univ)
        if nugu_univ[-1]=='대':
            nugu_univ += '학교'
        school = School.objects.filter(university=nugu_univ)[0]
        name = school.university
    
    if nugu_body.get('action').get('parameters').get('start'):
        time = school.start
    elif nugu_body.get('action').get('parameters').get('end'):
        time = school.end
    elif nugu_body.get('action').get('parameters').get('term'):
        time = school.term
    
    
    # 2. 응답 만들기
    # 필수 : output, resultCode
    result = nugu_body
    result['output'] = {'univname': name, 
                        'time': time}
    result['resultCode'] = 'OK'

    pprint.pprint(result)
    return JsonResponse(result)
    
def interview(request):
    pprint.pprint(request.body)
    
    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    pprint.pprint(nugu_body)
    
    i_name='-'
    i_time='-'
    # 1. school 정보 DB에 접근
    if nugu_body.get('action').get('parameters').get('i_univ'):
        nugu_univ = nugu_body.get('action').get('parameters').get('i_univ').get('value')
        
        school = School.objects.filter(university=nugu_univ)[0]
        i_name = school.university
        if nugu_body.get('action').get('parameters').get('i_typical'):
            i_typical = school.typical
            
        if nugu_body.get('action').get('parameters').get('i_interview'):
            i_time = school.interview_date
    
    
    # 2. 응답 만들기
    # 필수 : output, resultCode
    result = nugu_body
    result['output'] = {'i_univname': i_name, 
                        'i_time': i_time}
    result['resultCode'] = 'OK'

    pprint.pprint(result)
    return JsonResponse(result)