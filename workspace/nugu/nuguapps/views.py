import pprint
import json
import requests

from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import School, App

# Create your views here.
def health(request):
    return JsonResponse({})

def deadline(request):
    pprint.pprint(request.body)

    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    pprint.pprint(nugu_body)

    name='없음'
    time='없음'
    # 1. school 정보 DB에 접근
    if nugu_body.get('action').get('parameters').get('d_univ'):
        nugu_univ = nugu_body.get('action').get('parameters').get('d_univ').get('value')
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
    result['output'] = {'d_univname': name,
                        'd_time': time}
    result['resultCode'] = 'OK'

    pprint.pprint(result)
    return JsonResponse(result)

def interview(request):
    pprint.pprint(request.body)

    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    pprint.pprint(nugu_body)

    i_univname = '없음'
    i_subjectname ='없음'
    i_typicalname = '없음'
    i_result = '없음'
    # 1. school 정보 DB에 접근
    if nugu_body.get('action').get('parameters').get('i_univ'):
        nugu_univ = nugu_body.get('action').get('parameters').get('i_univ').get('value')

        school = School.objects.filter(university=nugu_univ)[0]
        i_univname = school.university
    
    if nugu_body.get('action').get('parameters').get('subject'):
        subject = nugu_body.get('action').get('parameters').get('subject').get('value')
        i_subjectname = subject
        
    if nugu_body.get('action').get('parameters').get('typical'):
        nugu_typical = nugu_body.get('action').get('parameters').get('typical').get('value')
        i_typicalname = nugu_typical
        
    if i_univname!='없음' and i_subjectname!='없음' and i_typicalname!='없음':
        total_result = School.objects.filter(university=i_univname).filter(typical=i_typicalname).filter(subject=i_subjectname)[0]
        i_result = total_result.interview_date
        result = nugu_body
        if i_result=='no':
            context = {'i_univname': i_univname,
                        'i_subjectname':i_subjectname,
                        'i_typicalname':i_typicalname}
        elif i_result != 'no':
            context = {'i_univname': i_univname,
                        'i_subjectname':i_subjectname,
                        'i_typicalname':i_typicalname,
                        'i_result': i_result }
                        
        result['output'] = context
        result['resultCode'] = 'OK'
        pprint.pprint(result)
        return JsonResponse(result)
        
    result = nugu_body
    result['output'] = {'i_univname': i_univname,
                        'i_subjectname':i_subjectname,
                        'i_typicalname':i_typicalname}
    result['resultCode'] = 'OK'
    pprint.pprint(result)
    return JsonResponse(result)
    
def result(request):
    pprint.pprint(request.body)

    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    pprint.pprint(nugu_body)
    
    r_univname = '없음'
    r_typicalname = '없음'
    r_first_result = '없음'
    r_final_result = '없음'
    
    if nugu_body.get('action').get('parameters').get('r_univ'):
        nugu_univ = nugu_body.get('action').get('parameters').get('r_univ').get('value')

        school = School.objects.filter(university=nugu_univ)[0]
        r_univname = school.university
    
    if nugu_body.get('action').get('parameters').get('r_typical'):
        nugu_typical = nugu_body.get('action').get('parameters').get('r_typical').get('value')
        r_typicalname = nugu_typical 
    
    if r_univname!='없음' and r_typicalname!='없음':
        total_result = School.objects.filter(university=r_univname).filter(typical=r_typicalname)[0]
        r_first_result = total_result.first_result
        r_final_result = total_result.final_result
        result = nugu_body
        if r_first_result=='no':
            context = {'r_univname': r_univname,
                        'r_typicalname':r_typicalname,
                        'final_result': r_final_result }
        else:
            context = {'r_univname': r_univname,
                        'r_typicalname':r_typicalname,
                        'first_result': r_first_result,
                        'final_result': r_final_result }
        result['output'] = context
        result['resultCode'] = 'OK'
        pprint.pprint(result)
        return JsonResponse(result)

    result = nugu_body
    result['resultCode'] = 'OK'
    result['output'] = {'r_univname': r_univname}
    pprint.pprint(result)
    return JsonResponse(result)