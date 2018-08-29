from block import Block

from flask import Flask, render_template, request, jsonify
class BlockChain:
    def __init__(self):
        self.chain = []
        genesis_block = Block()
        genesis_block.bits = 5 #초기 난이도
        self.chain.append(genesis_block)



#pip install flask
# 어떤요청이 어떤 데이터랑 들어왔네 어떤 페이지로 어떤 데이터 실려서 보내줘야지
app = Flask(__name__)
@app.route('/')
def index():
    print('요청이 들어옵니까')
    return render_template('index.html', result={'a':10, 'b':20})

@app.route('/hello')
def hello():
    b = Block()
    b.gen_hash()
    return jsonify(str(b))

app.run(host='0.0.0.0', port=8080)

