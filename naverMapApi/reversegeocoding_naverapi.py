from urllib import request
import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
from naverMapApi.naverApiKEY import client_id, client_pw;
import xml.etree.ElementTree as ET


#reverse geocoding api - naver
api_url = 'https://naveropenapi.apigw.ntruss.com/map-reversegeocode/v2/gc?coords='



data = ['127.0783723, 37.6316217','126.9297941, 37.5566314']

def reverse_geocoding(cord_dataset):
    results=[]
    for cord in cord_dataset:
        cord_url = parse.quote(cord[0])
        url = api_url + cord_url + "&orders=roadaddr&output=json"
        request = Request(url)
        request.add_header('X-NCP-APIGW-API-KEY-ID',client_id)
        request.add_header('X-NCP-APIGW-API-KEY', client_pw)
        try:
            response = urlopen(request)
        except HTTPError as e:
            print('HTTP Error!', e)
        else: 
            rescode = response.getcode()
            if rescode == 200:
                response_body = response.read().decode('utf-8')
                response_body = json.loads(response_body)
                print(response_body)
                if response_body['status']['code'] == 0:
                  area1 = response_body['results'][0]['region']['area1']['name']
                  area2 = response_body['results'][0]['region']['area2']['name']
                  name = response_body['results'][0]['land']['name']
                  land1 = response_body['results'][0]['land']['number1']
                  addition = response_body['results'][0]['land']['addition0']['value']
                  print(area1, area2, name, land1, addition)
                  results.append(area1+ " " + area2 + " " + name + " " + land1 + " " + addition)
                else: 
                  results.append("주소 정보가 없습니다")
    return results


reverse_geocoding(data)