from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbspartabook                      # 'dbsparta'라는 이름의 db를 만듭니다.

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

## API 역할을 하는 부분
@app.route('/reviews', methods=['POST'])
def write_review():
    print(request.form)
    # 타이틀을 받아야 하고, 저자를 받아야 하고, 리뷰를 받아야 함.
    # 데이터를 읽어온다. (저자, 제목, 리뷰) 
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']
# DB에 저장하기
    review = { 
        'title':title_receive,
        'author':author_receive,
        'review':review_receive
    }
    #DB에 넣기.
    db.reviews.insert_one(review)
    return jsonify({'result':'success', 'msg': "성공적으로 등록을 완료하였습니다."})

# GET요청도 서버, 클라이언트 순서로 작업. 

@app.route('/reviews', methods=['GET'])
def read_reviews():
      #. 바로 db에 요청. 리뷰 다 들고옴.
    reviews = list(db.reviews.find({}, {'_id': False}))
    print(reviews)
    return jsonify({'result':'success', 'msg':'성공', 'reviews': reviews})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)