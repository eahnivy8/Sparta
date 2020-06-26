import requests
import pprint
import urllib.parse
import time
from pymongo import MongoClient

# 동물병원 데이터는 cat_lovers 라는 데이터베이스에 저장하겠습니다.
client = MongoClient('localhost', 27017)
db = client.cats_loverss

# 서울시 구마다 고양이 병원 검색.
seoul_gu = ["종로구", "중구", "용산구", "성동구", "광진구", "동대문구", "중랑구", "성북구", "강북구", "도봉구", "노원구", "은평구", "서대문구", "마포구", "양천구", "강서구", "구로구", "금천구", "영등포구", "동작구", "관악구", "서초구", "강남구", "송파구", "강동구"]

# 네이버 검색 API 신청을 통해 발급받은 아이디와 시크릿 키 입력.
client_id = "zFYTXtos1wK2sjinQtkQ"
client_secret = "Qh6U2Zll04"

# 검색어를 전달하면 결과를 반환하는 함수
def get_naver_result(keyword):
    time.sleep(0.1)
    # url에 전달받은 검색어를 삽입합니다.
    api_url = f"https://openapi.naver.com/v1/search/local.json?query={keyword}&display=10&start=1&sort=random"
    # 아이디와 시크릿 키를 부가 정보로 같이 보냅니다.
    headers = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret }
    # 검색 결과를 data에 저장합니다.
    data = requests.get(api_url, headers=headers)
    # 받아온 JSON 결과를 딕셔너리로 변환합니다.
    data = data.json()
    return data['items']
# 저장할 전체 병원 목록 
docs = [] 
# 구별로 검색을 실행합니다.
for gu in seoul_gu:
    # '강님구 병원', '종로구 병원', '용산구 병원' .. 을 반복해서 인코딩합니다.
    keyword = f'{gu} 고양이병원'
    # 병원 리스트를 받아옵니다.
    hospitals_list = get_naver_result(keyword)

    # 구별 병원 구분선입니다.
    print("*"*80 + gu)

    for hospital in hospitals_list:
        # 구 정보를 추가함.
        hospital['gu'] = gu
        # 병원을 인쇄합니다.
        pprint.pprint(hospital)
        # docs에 병원을 추가 
        # docs.append(hospital)        
        db.hospital4.insert(hospital)
