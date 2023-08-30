import json

# 제목 / 장르 / 이미지 / 

game = {
    'INTJ': { 'title' : '문명', 'genre': '턴제 게임, 전략 시뮬레이션, 카드, MMORPG', 'img' :'https://cdn.gametoc.co.kr/news/photo/202005/54894_106222_638.jpg'},
    'INTP': {'title' : '스타크래프트', 'genre': '오픈월드, MMORPG, MOBA, 전략', 'img' :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRrDPQjBTrfRMczrwOBacZ3YIT_w7f-3CS1eA&usqp=CAU'},
    'ENTJ': {'title' : '리그오브레전드', 'genre': '실시간 전략게임, MOBA, 시뮬레이션', 'img' :'https://theme.zdassets.com/theme_assets/43400/87a1ef48e43b8cf114017e3ad51b801951b20fcf.jpg'},
    'ENTP': {'title' : '스플래툰', 'genre': 'MMOG, MMORPG, MOBA', 'img' :'https://www.nintendo.co.kr/switch/av5ja/assets/images/index/pc/info/img_twitter.png'},
    'INFJ': {'title' : '언더테일', 'genre': 'MMORPG, 시뮬레이션, 어드벤쳐, 인디', 'img' :'https://d3kxs6kpbh59hp.cloudfront.net/community/COMMUNITY/cffde743706a4aa680b41dae02077ce4/e4fd649cdd774edda45c267278bb5ead_1600215546.png'},
    'INFP': {'title' : '스타듀밸리', 'genre': '어드벤처, 인디, 캐주얼, MMORPG', 'img' :'https://cdn.gametoc.co.kr/news/photo/201809/49202_94286_458.JPG'},
    'ENFJ': {'title' : '오버워치', 'genre': 'eSports, AOS, MMORPG, 소셜, 액션', 'img' :'https://static.wikia.nocookie.net/overwatch152/images/b/bf/%EC%98%A4%EB%B2%84%EC%9B%8C%EC%B9%98_%EB%A1%9C%EA%B3%A0.jpg/revision/latest?cb=20160616114533&path-prefix=ko'},
    'ENFP': {'title' : '동물의숲', 'genre': 'MMORPG, eSports, 전략게임', 'img' :'https://i.namu.wiki/i/oU0avPQmlPv0p13BPnuEqyzmtGl9SoTArdKVYpb1r5CYXrpUjEqtiurvlFDjpXdOMyDXwIFYpz0x3PgtS92_8A.webp'},
    'ISTJ': {'title' : '포탈', 'genre': '플랫포머, 퍼즐, 어드벤처', 'img' :'https://i.namu.wiki/i/hLeT30QQNywS7OLOE7BLIMICSrC5NV8fsTP9DUf6Dbku-S6B1lTpwWWeYnHaZ3-QoSGYBHTYV8EbtQvvQ4yRog.webp'},
    'ISFJ': {'title' : '마인크래프트', 'genre': '어드벤처, 캐쥬얼, 퍼즐, RPG, 싱글플레이', 'img' :'https://upload.wikimedia.org/wikipedia/ko/thumb/f/f0/%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8_%ED%91%9C%EC%A7%80.jpg/220px-%EB%A7%88%EC%9D%B8%ED%81%AC%EB%9E%98%ED%94%84%ED%8A%B8_%ED%91%9C%EC%A7%80.jpg'},
    'ESTJ': {'title' : '카운터스트라이크', 'genre': '스포츠, 액션, 전략', 'img' :'https://i.namu.wiki/i/uGTmFd5g5BLvPZIvAUj9f3Apf0Z7Cxl7ywpNfh9ziqRR3yeGgVTXM242IonzCswbbsFBmyULtamJXeU9iCGNfg.webp'},
    'ESFJ': {'title' : '링피트', 'genre': 'MOBA, eSports, 파티', 'img' :'https://i.namu.wiki/i/43P_oenkE853O8uxU2eVZ5EwCVnWIlxZdiP7jz-VYGR6A5vNkkHYJX9noIrYZ8WctYYZn-PqWx4WDP_KkqiBWQ.webp'},
    'ISTP': {'title' : '배틀필드', 'genre': '시뮬레이션, 타이쿤, 전략', 'img' :'https://i.namu.wiki/i/lRUtWQsPNHtLntsugfd9iJKOKxXrPObtxmtZ1bfwb1VdvzX_-R3iDqYbKRsHxQ_1Hbyk2NdI3nHL_N6IQsUE6Q.webp'},
    'ISFP': {'title' : '데빌메이크라이', 'genre': '턴제 게임, 전략 시뮬레이션, 카드, MMORPG', 'img' :'https://i.namu.wiki/i/kgl3X_lFZuvT1KLG7c0eDwLoxDZ4F75Dpbi_tilfcEYusIDA0r4PunJNi0qeCY-pFlbHtesnkzmWKYqyxL-ccw.webp'},
    'ESTP': {'title' : 'GTA', 'genre': 'FPS, 배틀로얄, 액션, 격투, 호러, 스포츠', 'img' :'https://image.api.playstation.com/vulcan/ap/rnd/202202/2816/mYn2ETBKFct26V9mJnZi4aSS.png'},
    'ESFP': {'title' : '저스트댄스', 'genre': '파티, 댄스, 리듬, 슈', 'img' :'https://i.namu.wiki/i/S9JUymuqtRHDqzeyqgRTzhyKoMNXfD73s8ILxbeetW0S2a4yJ5-J3phHNLgoBjsW5_GJ4kflV_boljvCRgmEeg.webp'}
}


def GameResult(mbti):
    data = {
    'mbti': mbti,
    'title': game[mbti]['title'],
    'genre': game[mbti]['genre'],
    'img' : game[mbti]['img']
    }
    # print('aa')
    # print(mbti, game[mbti]['title'], game[mbti]['genre'], game[mbti]['img'])

    json_data = json.dumps(data, ensure_ascii=False)
    print(json_data)
    return json_data
