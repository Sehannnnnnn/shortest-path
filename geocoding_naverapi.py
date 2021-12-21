import numpy as np
import pandas as pd
from urllib.request import urlopen
from urllib import parse
from urllib.request import Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import json
from naverApiKEY import client_id, client_pw;

api_url = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='


data = ['서울특별시 노원구 공릉로 232']

geo_coordi = []

for add in data:
  add_url = parse.quote(add)
  url = api_url + add_url
  request = Request(url)
  request.add_header('X-NCP-APIGW-API-KEY-ID', client_id)
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
          print(response_body['addresses'][0]['y'])
          print(response_body['addresses'][0]['x'])
          print("Success!")
    else:
      print('Response error code : %d' % rescode)
      latitude = None
      longitude = None


    
