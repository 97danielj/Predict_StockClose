from flask import Flask, request, jsonify
import pickle
import sys
from datetime import date, timedelta,datetime
application = Flask(__name__)

rinuxtimenow = datetime.now() #리눅스 현재 시각
krtimenow = rinuxtimenow+timedelta(hours=9) # kr현재시각
tomorrow = rinuxtimenow+timedelta(days=1,hours=9) #kr 24시간 후
if(16 <= krtimenow.hour and krtimenow.hour<= 23):
    set_d = tomorrow.date()
elif (0 <= krtimenow.hour and krtimenow.hour< 16):
    set_d = krtimenow.date()
set_d = set_d.isoformat()
set_d = set_d.replace('-','')[2:]
set_d

@application.route("/")
def hello():
    return "Hello goorm!"
    
with open(f'{set_d}pred_dic.pickle','rb') as f:
    pred_dic = pickle.load(f)

with open('certificated_stock_dic.pickle' , 'wb') as f:
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

#캐러셀 스킬
#-------------캐러셀 코드-----------------------
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
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "섬유의복",
                  "messageText": '섬유의복'
                }
              ]
            },
            {
              "title": "화학, 의약품",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "의약품",
                  "messageText": '의약품'
                }
              ]
            },
              {
              "title": "비금속광물, 철강금속",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "철강금속",
                  "messageText": '철강금속'
                }
              ]
            },
              {
              "title": "기계, 전기전자",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "전기전자",
                  "messageText": '전기전자'
                }
              ]
            },
              {
              "title": "건설업, 운수창고",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "운수창고",
                  "messageText": '운수창고'
                }
              ]
            },
              {
              "title": "유통업, 전기가스업",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "전기가스업",
                  "messageText": '전기가스업'
                }
              ]
            },
              {
              "title": "통신업, 금융업",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "금융업",
                  "messageText":'금융업'
                }
              ]
            },
              {
              "title": "증권, 보험",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
                  "label": "보험",
                  "messageText": '보험'
                }
              ]
            },
              {
              "title": "서비스업, 제조업",
              "description": set_d+" 일자 업종 시세 예상 추이 확인",
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
                  "action":  "message",
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



sector_l = {
    '음식료품' : ['오리온', '하이트진로', '농심', '롯데칠성'],
    '섬유의복' : ['LF', '한섬', '한세실업'],
    '화학' :  ['SK이노베이션', 'S-Oil', 'LG생활건강', '아모레퍼시픽'],
    '의약품' :  ['삼성바이오로직스', '셀트리온', '한미약품'],
    '비금속광물' : ['쌍용C&E', '아이에스동서'],
    '철강금속' : ['POSCO홀딩스', '고려아연', '현대제철', 'KG스틸', '동국제강'],
    '기계' : ['두산에너빌리티', '한온시스템', '두산밥캣', '씨에스윈드'],
    '전기전자': ['삼성전자', 'SK하이닉스', 'LG전자'],
    '건설업' : ['현대건설', 'GS건설', '대우건설', '한전KPS'],
    '운수창고' : ['HMM', '대한항공', '현대글로비스', '한진칼', '팬오션'],
    '유통업' : ['삼성물산', '롯데쇼핑', 'BGF리테일', '이마트', '신세계'],
    '전기가스업' : ['한국전력', '한국가스공사'],
    '통신업' : [ 'KT', 'LG유플러스'],
    '금융업' :  ['LG' , '삼성화재', '미래에셋증권'],
    '증권' : ['NH투자증권' ,'삼성증권', '메리츠증권', '키움증권'],
    '보험' : ['삼성생명', 'DB손해보험', '현대해상'],
    '서비스업' : [ '삼성에스디에스', '엔씨소프트'],
    '제조업' :  ['현대차', '기아', '현대모비스', 'KT&G', '삼성전기']
}




#업종별 리스트 출력(listitem)
#---------------------------------------------------
@application.route("/listitem", methods=["POST"])
def listitem():
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['sector_entity']['value']   # json파일 읽기
    n = len(sector_l[answer])
    res = sector_l_response(answer,n)
    
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
                  "messageText" : "업종별",
                }
              ]
        }
      }
    ]
  }
}

    return jsonify(response)


#listitem의 json코드만들기
def sector_l_response(answer,n):
    if n==1:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://img.danawa.com/prod_img/500000/284/976/img/8976284_1.jpg?shrink=330:330&_v=20190802153645",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
        ]
    elif n==2:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://img.danawa.com/prod_img/500000/164/976/img/8976164_1.jpg?shrink=330:330&_v=20190802153555",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://img.danawa.com/prod_img/500000/452/976/img/8976452_1.jpg?shrink=330:330&_v=20190802154103",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
        ]
    elif n==3:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FO16783343728.jpg%3Fut%3D20220324163643",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/2021/03/08/15/3/3c275dcf-458d-4af1-8bc2-45ed7ea70219.jpg",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
            {
              "title": sector_l[answer][2],
              "imageUrl": "https://img.danawa.com/prod_img/500000/044/976/img/8976044_1.jpg?shrink=330:330&_v=20190802153539",
              "action": "message",
              "messageText": sector_l[answer][2],
              },
        ]
    elif n==4:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://cdn.011st.com/11dims/resize/600x600/quality/75/11src/product/3181252337/B.jpg?479000000",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://img.danawa.com/prod_img/500000/284/976/img/8976284_1.jpg?shrink=330:330&_v=20190802153645",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
            {
              "title": sector_l[answer][2],
              "imageUrl": "http://image.kyobobook.co.kr/newimages/giftshop_new/goods/400/1730/hot1539673071039.jpg",
              "action": "message",
              "messageText": sector_l[answer][2],
              },
            {
              "title": sector_l[answer][3],
              "imageUrl": "http://mstatic1.e-himart.co.kr/contents/goods/00/15/59/76/87/0015597687__MW64027_1944709__M_640_640.jpg",
              "action": "message",
              "messageText": sector_l[answer][3],
              },
        ]
    elif n==5:
        res = [
             {
              "title": sector_l[answer][0],
              "imageUrl": "https://shop1.daumcdn.net/thumb/R500x500/?fname=http%3A%2F%2Fshop1.daumcdn.net%2Fshophow%2Fp%2FO16783343728.jpg%3Fut%3D20220324163643",
              "action": "message",
              "messageText": sector_l[answer][0],
              },
            {
              "title": sector_l[answer][1],
              "imageUrl": "https://thumbnail9.coupangcdn.com/thumbnails/remote/492x492ex/image/retail/images/2021/03/08/15/3/3c275dcf-458d-4af1-8bc2-45ed7ea70219.jpg",
              "action": "message",
              "messageText": sector_l[answer][1],
              },
            {
              "title": sector_l[answer][2],
              "imageUrl": "https://img.danawa.com/prod_img/500000/044/976/img/8976044_1.jpg?shrink=330:330&_v=20190802153539",
              "action": "message",
              "messageText": sector_l[answer][2],
              },
            {
              "title": sector_l[answer][3],
              "imageUrl": "https://img.danawa.com/prod_img/500000/164/976/img/8976164_1.jpg?shrink=330:330&_v=20190802153555",
              "action": "message",
              "messageText": sector_l[answer][3],
              },
            {
              "title": sector_l[answer][4],
              "imageUrl": "https://img.danawa.com/prod_img/500000/452/976/img/8976452_1.jpg?shrink=330:330&_v=20190802154103",
              "action": "message",
              "messageText": sector_l[answer][4],
              },
        ]
    return res


#업종별 리스트 출력(basiccard)
#---------------------------------------------------
@application.route("/basiccard", methods=["POST"])
def basiccard():
    text = None
    req = request.get_json(silent=True)
    answer = req["action"]['detailParams']['stock_code']['value']
    stock_code = answer[-6:]
    sector_name = answer[:-6]
    stock_idx = certificated_stock_dic[sector_name].index(stock_code)
    stock_code_kr = sector_l[sector_name][stock_idx]
    result = pred_dic[sector_name][stock_code][0]
    URL = None
    if result == 2:
        URL = 'https://media.discordapp.net/attachments/992344867718037604/1006739068345917591/up.png'
    elif result == 1:
        URL = 'https://cdn.discordapp.com/attachments/992344867718037604/1006739067918106696/down.png'
    else: 
    	URL = 'https://cdn.discordapp.com/attachments/992344867718037604/1006739067398004756/sideways.png'
    response = {
      "version": "2.0",
      "template": {
        "outputs": [
          {
            "basicCard": {
              "title": "보물상자",
              "description": "보물상자 안에는 뭐가 있을까",
              "thumbnail": {
                "imageUrl": "https://t1.kakaocdn.net/openbuilder/sample/lj3JUcmrzC53YIjNDkqbWK.jpg"
              },
              "profile": {
                "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT4BJ9LU4Ikr_EvZLmijfcjzQKMRCJ2bO3A8SVKNuQ78zu2KOqM",
                "nickname": "보물상자"
              },
              "social": {
                "like": 1238,
                "comment": 8,
                "share": 780
              },
              "buttons": [
                {
                  "action": "message",
                  "label": "열어보기",
                  "messageText": "짜잔! 우리가 찾던 보물입니다"
                },
                {
                  "action":  "webLink",
                  "label": "구경하기",
                  "webLinkUrl": "https://e.kakao.com/t/hello-ryan"
                }
              ]
            }
          }
        ]
      }
    }
    return jsonify(response)
  


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)