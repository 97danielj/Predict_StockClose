from flask import Flask, request, jsonify
import pickle
import sys
from datetime import date, timedelta, datetime

application = Flask(__name__)

linuxtimenow = datetime.now()  # 리눅스 현재 시각
krtimenow = linuxtimenow + timedelta(hours=9)  # kr현재시각
tomorrow = linuxtimenow + timedelta(days=1, hours=9)  # kr 24시간 후
if (16 <= krtimenow.hour and krtimenow.hour <= 23):
    set_d = tomorrow.date()
elif (0 <= krtimenow.hour and krtimenow.hour < 16):
    set_d = krtimenow.date()
set_d = set_d.isoformat()
set_d = set_d.replace('-', '')[2:]
set_d
print(linuxtimenow)
print(set_d)


@application.route("/")
def hello():
    return "Hello goorm!"


with open(f'{set_d}pred_dic.pickle', 'rb') as f:
    pred_dic = pickle.load(f)

with open('certificated_stock_dic.pickle', 'rb') as f:
    certificated_stock_dic = pickle.load(f)

'''
@application.route("/return_entry", methods=["POST"])
def return_entry():

    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['sector_entity']['value']   # json파일 읽기

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)
'''


# 캐러셀 스킬
# -------------캐러셀 코드-----------------------
@application.route("/carousel", methods=["POST"])
def carousel():
    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "carousel": {
                        "type": "basicCard",
                        "items": [
                            {
                                "title": "음식료품, 섬유의복",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Clothing-Food.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "음식료품",
                                        "messageText": '음식료품'
                                    },
                                    {
                                        "action": "message",
                                        "label": "섬유의복",
                                        "messageText": '섬유의복'
                                    }
                                ]
                            },
                            {
                                "title": "화학, 의약품",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Medicine-Chemical.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "화학",
                                        "messageText": '화학'
                                    },
                                    {
                                        "action": "message",
                                        "label": "의약품",
                                        "messageText": '의약품'
                                    }
                                ]
                            },
                            {
                                "title": "비금속광물, 철강금속",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Metal-NonMetal.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "비금속광물",
                                        "messageText": '비금속광물'
                                    },
                                    {
                                        "action": "message",
                                        "label": "철강금속",
                                        "messageText": '철강금속'
                                    }
                                ]
                            },
                            {
                                "title": "기계, 전기전자",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Electronic-Machine.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "기계",
                                        "messageText": '기계'
                                    },
                                    {
                                        "action": "message",
                                        "label": "전기전자",
                                        "messageText": '전기전자'
                                    }
                                ]
                            },
                            {
                                "title": "건설업, 운수창고",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Transport-Construction.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "건설업",
                                        "messageText": '건설업'
                                    },
                                    {
                                        "action": "message",
                                        "label": "운수창고",
                                        "messageText": '운수창고'
                                    }
                                ]
                            },
                            {
                                "title": "유통업, 전기가스업",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Power-Distribution.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "유통업",
                                        "messageText": '유통업'
                                    },
                                    {
                                        "action": "message",
                                        "label": "전기가스업",
                                        "messageText": '전기가스업'
                                    }
                                ]
                            },
                            {
                                "title": "통신업, 금융업",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": 'https://github.com/97danielj/stock_api/blob/master/CarouselImages/Finance-Tele.png?raw=true'
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "통신업",
                                        "messageText": '통신업'
                                    },
                                    {
                                        "action": "message",
                                        "label": "금융업",
                                        "messageText": '금융업'
                                    }
                                ]
                            },
                            {
                                "title": "증권, 보험",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Insure-Brokerage.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "증권",
                                        "messageText": '증권'
                                    },
                                    {
                                        "action": "message",
                                        "label": "보험",
                                        "messageText": '보험'
                                    }
                                ]
                            },
                            {
                                "title": "서비스업, 제조업",
                                "description": set_d + " 일자 업종 시세 예상 추이 확인",
                                "thumbnail": {
                                    "imageUrl": "https://github.com/97danielj/stock_api/blob/master/CarouselImages/Manufacturer-Service.png?raw=true"
                                },
                                "buttons": [
                                    {
                                        "action": "message",
                                        "label": "서비스업",
                                        "messageText": '서비스업'
                                    },
                                    {
                                        "action": "message",
                                        "label": "제조업",
                                        "messageText": '제조업'
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(response)


sector_l_list = {
    'Food': ['CJ제일제당', '오리온', '하이트진로', '농심', '롯데칠성'],
    'Clothing': ['LF', '한샘', '한세실업', '대한방직'],
    'Chemical': ['LG화학', 'SK이노베이션', 'S-Oil', 'LG생활건강', '아모레퍼시픽'],
    'Medicine': ['삼성바이오로직스', '셀트리온', '유한양행', '한미약품'],
    'Non_Metal': ['쌍용C&E', '아이에스동서'],
    'Metal': ['POSCO홀딩스', '고려아연', '현대제철', '동국제강'],
    'Machine': ['두산에너빌리티', '한온시스템', '두산밥캣', '씨에스윈드'],
    'Electronic': ['삼성전자', 'SK하이닉스', 'LG전자'],
    'Construction': ['현대건설', 'GS건설', '대우건설', '한전KPS'],
    'Transport': ['HMM', '대한항공', '현대글로비스', '한진칼', '팬오션'],
    'Distribution': ['삼성물산', '롯데쇼핑', 'BGF리테일', '이마트', '신세계'],
    'Power': ['한국전력', '한국가스공사', '서울가스'],
    'Tele': ['SK텔레콤', 'KT', 'LG유플러스'],
    'Finance': ['LG', '삼성화재', '미래에셋증권'],
    'Brokerage': ['NH투자증권', '삼성증권', '메리츠증권', '키움증권'],
    'Insurer': ['삼성생명', 'DB손해보험', '메리츠화재', '현대해상'],
    'Service': ['삼성에스디에스', '엔씨소프트'],
    'Manufacturer': ['현대자동차', '기아자동차', '현대모비스', 'KT&G', '삼성전기']
}
sector_l = {
    'Food': {'CJ제일제당': '097950', '오리온': '271560', '하이트진로': '000080', '농심': '004370', '롯데칠성': '005300'},
    'Clothing': {'LF': '093050', '한샘': '020000', '한세실업': '105630', '대한방직': '001070'},
    'Chemical': {'LG화학': '051910', 'SK이노베이션': '096770', 'S-Oil': '010950', 'LG생활건강': '051900', '아모레퍼시픽': '090430'},
    'Medicine': {'삼성바이오로직스': '207940', '셀트리온': '068270', '유한양행': '000100', '한미약품': '128940'},
    'Non_Metal': {'쌍용C&E': '003410', '아이에스동서': '010780'},
    'Metal': {'POSCO홀딩스': '005490', '고려아연': '010130', '현대제철': '004020', '동국제강': '001230'},
    'Machine': {'두산에너빌리티': '034020', '한온시스템': '018880', '두산밥캣': '241560', '씨에스윈드': '112610'},
    'Electronic': {'삼성전자': '005930', 'SK하이닉스': '000660', 'LG전자': '066570'},
    'Construction': {'현대건설': '000720', 'GS건설': '006360', '대우건설': '047040', '한전KPS': '051600'},
    'Transport': {'HMM': '011200', '대한항공': '003490', '현대글로비스': '086280', '한진칼': '180640', '팬오션': '028670'},
    'Distribution': {'삼성물산': '028260', '롯데쇼핑': '023530', 'BGF리테일': '282330', '이마트': '139480', '신세계': '004170'},
    'Power': {'한국전력': '015760', '한국가스공사': '036460', '서울가스': '017390'},
    'Tele': {'SK텔레콤': '017670', 'KT': '030200', 'LG유플러스': '032640'},
    'Finance': {'LG': '003550', '삼성화재': '000810', '미래에셋증권': '006800'},
    'Brokerage': {'NH투자증권': '005940', '삼성증권': '016360', '메리츠증권': '008560', '키움증권': '039490'},
    'Insurer': {'삼성생명': '032830', 'DB손해보험': '005830', '메리츠화재': '000060', '현대해상': '001450'},
    'Service': {'삼성에스디에스': '018260', '엔씨소프트': '036570'},
    'Manufacturer': {'현대자동차': '005380', '기아자동차': '000270', '현대모비스': '012330', 'KT&G': '033780', '삼성전기': '009150'}
}


# 업종별 리스트 출력(listitem)
# ---------------------------------------------------
@application.route("/listitem", methods=["POST"])
def listitem():
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['sector_entity']['value']  # json파일 읽기
    n = len(sector_l_list[answer])
    res = sector_l_response(answer, n)

    # 답변 텍스트 설정
    response = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": answer
                        },
                        "items": res,
                        "buttons": [
                            {
                                "label": "뒤로가기",
                                "action": "message",
                                "messageText": "업종별",
                            }
                        ]
                    }
                }
            ]
        }
    }

    return jsonify(response)


# listitem의 json코드만들기
def sector_l_response(answer, n):
    res = []
    image_urls = [
        "https://img.danawa.com/prod_img/500000/284/976/img/8976284_1.jpg?shrink=330:330&_v=20190802153645",
        "https://img.danawa.com/prod_img/500000/164/976/img/8976164_1.jpg?shrink=330:330&_v=20190802153555",
        "https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FO16783343728.jpg%3Fut%3D20220324163643",
        "https://thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/2021/03/08/15/3/3c275dcf-458d-4af1-8bc2-45ed7ea70219.jpg",
        "https://img.danawa.com/prod_img/500000/044/976/img/8976044_1.jpg?shrink=330:330&_v=20190802153539",
        "http://image.kyobobook.co.kr/newimages/giftshop_new/goods/400/1730/hot1539673071039.jpg",
        "http://mstatic1.e-himart.co.kr/contents/goods/00/15/59/76/87/0015597687__MW64027_1944709__M_640_640.jpg",
    ]

    for i in range(n):
        res.append({
            "title": sector_l_list[answer][i],
            "imageUrl": image_urls[i],
            "action": "message",  # stock_code = sector_l_list[answer][sector_l[answer][i]]
            "messageText": sector_l_list[answer][i] + "는 " + pred_dic[answer][
                sector_l[answer][sector_l_list[answer][i]]]

        })

    return res


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)