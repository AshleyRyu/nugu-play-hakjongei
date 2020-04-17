import pprint
import json
import requests

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def health(request):
    return JsonResponse({})
    
def dust(request):
    pprint.pprint(request.body)
    # 0. nugu api -> dict
    nugu_body = json.loads(request.body, encoding='utf-8')
    '''
    nugu_body 예시
    {'action': {'actionName': 'dust',
                'parameters': {'intend': {'type': 'DUST', 'value': '미세먼지'},
                               'location': {'type': 'BID_LOC_CITY',
                                            'value': '서울'}}},
     'context': {'device': {'state': {}, 'type': 'speaker'},
                 'session': {'id': '26b83325-1ca9-4bfc-9a78-6ba803c85dd8',
                             'isNew': True,
                             'isPlayBuilderRequest': True},
                 'supportedInterfaces': None},
     'version': '2.0'}
    '''
    if nugu_body.get('action').get('parameters').get('location'):
        nugu_location = nugu_body.get('action').get('parameters').get('location').get('value')

    else:
        nugu_location = '서울'
    # 1. 미세먼지 api
    url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&sidoName={nugu_location}&ver=1.3&pageNo=1&numOfRows=10&_returnType=json'
    print(url)
    response = requests.get(url).json()
    first = response.get('list')[0]
    dust = int(first.get('pm10Value'))
    
    # 2. 응답 만들기
    # 필수 : output, resultCode
    result = nugu_body
    result['output'] = {'status': dust, 'loc': nugu_location }
    result['resultCode'] = 'OK'
    pprint.pprint(result)
    '''
    result 예시
    {'action': {'actionName': 'dust',
                'parameters': {'intend': {'type': 'DUST', 'value': '미세먼지'},
                               'location': {'type': 'BID_LOC_CITY',
                                            'value': '서울'}}},
     'context': {'device': {'state': {}, 'type': 'speaker'},
                 'session': {'id': '26b83325-1ca9-4bfc-9a78-6ba803c85dd8',
                             'isNew': True,
                             'isPlayBuilderRequest': True},
                 'supportedInterfaces': None},
     'output': {'loc': '서울', 'status': 53},
     'resultCode': 'OK',
     'version': '2.0'}
    '''
    return JsonResponse(result)