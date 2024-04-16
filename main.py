from flask import Flask, request, jsonify

app = Flask(__name__)

# 단어와 뜻을 저장하는 사전
word_dict = {
    "intangible": "무형의 무형자산",
    "legitimate": "정당한, 합법적인, 적법한",
    "reflex": "반사작용, 반사 운동",
    "vulnerability": "취약성, 연약한 면/점",
    "aboriginal": "원주민의, 토착민의",
    "affluent": "부유한, 풍족한",
    "tangled": "엉켜 있는, 복잡한",
    "crave": "갈망하다, 열망하다",
    "reign": "지배하다, 통치하다, 지배 시기, [가왕] 재임",
    "discern": "식별하다, 분별하다, 인식하다",
    "definitive": "명확한, 분명한",
    "immerse": "담그다, 잠수하다, (완전히) 몰두하다",
    "impoverish": "가난하게 만들다",
    "peripheral": "주변의, 외곽의, 주변장치",
    "alert A to B": "A에게 B를 알리다 (주의, 위험 등을 알리다), 경보하다",
    "be subject to": "~을 받을 위험이 있다",
    "establish oneself as": "~으로서 입지를 굳히다, 성립되다",
    "give oneself over to": "~에 헌신적이 되다, 바치는, ~에 빠지다",
    "put across A to B": "A를 B에게 이해시키다, A를 B에게 알려주어 이해시키다",
    "take measures": "조치를 취하다",
    "faculty": "학부, 계열, 교수진",
    "homogenous": "동종의, 단일종의",
    "pervasive": "만연하는, 퍼져있는",
    "pronounced": "뚜렷한, 명확한",
    "receptive": "수용적인",
    "sedentary": "주로 앉아서 하는 일을 하는",
    "alleviate": "경감하다, 완화하다",
    "attentive": "주의 깊은, 세심한",
    "communal": "공동체적인, 공동의",
    "comply": "(법률) 따르다, 복종하다"
}

@app.route('/get_meaning', methods=['GET'])
def get_meaning():
    word = request.args.get('word')
    meaning = word_dict.get(word)
    if meaning:
        return jsonify({"word": word, "meaning": meaning})
    else:
        return jsonify({"error": "단어를 찾을 수 없습니다."})

if __name__ == '__main__':
    app.run(debug=True)
