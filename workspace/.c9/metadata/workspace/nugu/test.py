{"filter":false,"title":"test.py","tooltip":"/nugu/test.py","undoManager":{"mark":33,"position":33,"stack":[[{"start":{"row":0,"column":0},"end":{"row":5,"column":36},"action":"insert","lines":["import pprint","import json","import requests","","from django.shortcuts import render","from django.http import JsonResponse"],"id":1}],[{"start":{"row":5,"column":36},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":2},{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":13,"column":25},"action":"insert","lines":["headers = {'Accept':'application/json', 'Content-Type':'application/json; charset=UTF-8', appKey:'827eb1d5-b04b-43fb-a7d6-f1d9b7a97e55'}","    req_url = f'https://api2.sktelecom.com/tmap/geo/geocoding?version=1&city_do=서울시&gu_gun=마포구&dong=상수동&bunji=101'","    print(headers)","    print(req_url)","    ","    result = requests.get(req_url, headers=headers).json()","    pprint.pprint(result)"],"id":3}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "],"id":4}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["    "],"id":5}],[{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "],"id":6}],[{"start":{"row":12,"column":0},"end":{"row":12,"column":4},"action":"remove","lines":["    "],"id":7}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "],"id":8}],[{"start":{"row":7,"column":90},"end":{"row":7,"column":91},"action":"insert","lines":["'"],"id":9}],[{"start":{"row":7,"column":97},"end":{"row":7,"column":98},"action":"insert","lines":["'"],"id":10}],[{"start":{"row":13,"column":21},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":14,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["d"]},{"start":{"row":15,"column":1},"end":{"row":15,"column":2},"action":"insert","lines":["e"]},{"start":{"row":15,"column":2},"end":{"row":15,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":15,"column":3},"end":{"row":15,"column":4},"action":"insert","lines":[" "],"id":14}],[{"start":{"row":15,"column":4},"end":{"row":15,"column":5},"action":"insert","lines":["t"],"id":15},{"start":{"row":15,"column":5},"end":{"row":15,"column":6},"action":"insert","lines":["e"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["x"]},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":10},"action":"insert","lines":["()"],"id":16}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":10},"action":"remove","lines":["()"],"id":17},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"remove","lines":["t"]},{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"remove","lines":["x"]}],[{"start":{"row":15,"column":6},"end":{"row":15,"column":7},"action":"insert","lines":["s"],"id":18},{"start":{"row":15,"column":7},"end":{"row":15,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":8},"end":{"row":15,"column":10},"action":"insert","lines":["()"],"id":19}],[{"start":{"row":15,"column":9},"end":{"row":15,"column":10},"action":"insert","lines":["r"],"id":20},{"start":{"row":15,"column":10},"end":{"row":15,"column":11},"action":"insert","lines":["e"]},{"start":{"row":15,"column":11},"end":{"row":15,"column":12},"action":"insert","lines":["q"]},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["e"]},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["u"]}],[{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"remove","lines":["u"],"id":21},{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"remove","lines":["e"]}],[{"start":{"row":15,"column":12},"end":{"row":15,"column":13},"action":"insert","lines":["u"],"id":22},{"start":{"row":15,"column":13},"end":{"row":15,"column":14},"action":"insert","lines":["e"]},{"start":{"row":15,"column":14},"end":{"row":15,"column":15},"action":"insert","lines":["s"]},{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["t"]}],[{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":[":"],"id":23}],[{"start":{"row":15,"column":18},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":24},{"start":{"row":16,"column":0},"end":{"row":16,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":7,"column":40},"end":{"row":8,"column":0},"action":"insert","lines":["",""],"id":25}],[{"start":{"row":8,"column":50},"end":{"row":9,"column":0},"action":"insert","lines":["",""],"id":26}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"insert","lines":["    "],"id":27}],[{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "],"id":28}],[{"start":{"row":8,"column":4},"end":{"row":8,"column":8},"action":"insert","lines":["    "],"id":29}],[{"start":{"row":9,"column":4},"end":{"row":9,"column":8},"action":"insert","lines":["    "],"id":30}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":18},"action":"remove","lines":["","def test(request):"],"id":31}],[{"start":{"row":6,"column":0},"end":{"row":15,"column":21},"action":"remove","lines":["","headers = {'Accept':'application/json', ","        'Content-Type':'application/json; charset=UTF-8', ","        'appKey':'827eb1d5-b04b-43fb-a7d6-f1d9b7a97e55'}","req_url = f'https://api2.sktelecom.com/tmap/geo/geocoding?version=1&city_do=서울시&gu_gun=마포구&dong=상수동&bunji=101'","print(headers)","print(req_url)","    ","result = requests.get(req_url, headers=headers).json()","pprint.pprint(result)"],"id":32}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":33}],[{"start":{"row":0,"column":0},"end":{"row":9,"column":4},"action":"remove","lines":["import pprint","import json","import requests","","from django.shortcuts import render","from django.http import JsonResponse","","","","    "],"id":34},{"start":{"row":0,"column":0},"end":{"row":61,"column":31},"action":"insert","lines":["import pprint","import json","import requests","","from django.shortcuts import render","from django.http import JsonResponse","","# Create your views here.","def health(request):","    return JsonResponse({})","    ","def dust(request):","    pprint.pprint(request.body)","    # 0. nugu api -> dict","    nugu_body = json.loads(request.body, encoding='utf-8')","    '''","    nugu_body 예시","    {'action': {'actionName': 'dust',","                'parameters': {'intend': {'type': 'DUST', 'value': '미세먼지'},","                               'location': {'type': 'BID_LOC_CITY',","                                            'value': '서울'}}},","     'context': {'device': {'state': {}, 'type': 'speaker'},","                 'session': {'id': '26b83325-1ca9-4bfc-9a78-6ba803c85dd8',","                             'isNew': True,","                             'isPlayBuilderRequest': True},","                 'supportedInterfaces': None},","     'version': '2.0'}","    '''","    if nugu_body.get('action').get('parameters').get('location'):","        nugu_location = nugu_body.get('action').get('parameters').get('location').get('value')","","    else:","        nugu_location = '서울'","    # 1. 미세먼지 api","    url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=QaGapZXPV5DTM72fy6lrf3hJnrJxhila1UVkPlUCo0N0g0F0RZ9WEngT8RkNjNo4IF%2BikV%2BthQLze39nK4IQjA%3D%3D&sidoName={nugu_location}&ver=1.3&pageNo=1&numOfRows=10&_returnType=json'","    print(url)","    response = requests.get(url).json()","    first = response.get('list')[0]","    dust = int(first.get('pm10Value'))","    ","    # 2. 응답 만들기","    # 필수 : output, resultCode","    result = nugu_body","    result['output'] = {'status': dust, 'loc': nugu_location }","    result['resultCode'] = 'OK'","    pprint.pprint(result)","    '''","    result 예시","    {'action': {'actionName': 'dust',","                'parameters': {'intend': {'type': 'DUST', 'value': '미세먼지'},","                               'location': {'type': 'BID_LOC_CITY',","                                            'value': '서울'}}},","     'context': {'device': {'state': {}, 'type': 'speaker'},","                 'session': {'id': '26b83325-1ca9-4bfc-9a78-6ba803c85dd8',","                             'isNew': True,","                             'isPlayBuilderRequest': True},","                 'supportedInterfaces': None},","     'output': {'loc': '서울', 'status': 53},","     'resultCode': 'OK',","     'version': '2.0'}","    '''","    return JsonResponse(result)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":41,"column":29},"end":{"row":41,"column":29},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1554115966023,"hash":"806ab395b272c4a54a5e8cb8d5eb5f2d277cfb8a"}