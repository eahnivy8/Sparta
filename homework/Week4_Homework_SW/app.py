from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbspartahw4                     # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    # 타이틀을 받아야 하고, 저자를 받아야 하고, 리뷰를 받아야 함. 
    buyer_receive = request.form['buyer_give']
    quantity_receive = request.form['quantity_give']
    address_receive = request.form['address_give']
    tel_receive = request.form['tel_give']
# DB에 저장하기
    doc = { 
        'buyer':buyer_receive,
        'quantity':quantity_receive,
        'address':address_receive,
        'tel':tel_receive
    }
    db.orderreview.insert_one(doc)
    return jsonify({'result':'success', 'msg': "정상적으로 주문이 접수됨."})

# GET요청도 서버, 클라이언트 순서로 작업. 

@app.route('/reviews', methods=['GET'])
def read_reviews():

    reviews = list(db.orderreview.find({},{'_id': False}))

    return jsonify({'result':'success', 'all_review': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)