from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def myPage(): 
    return 'This is MyPage'


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
