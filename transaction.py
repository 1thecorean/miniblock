from bitcoin import *

class TxIn:
    def __init__(self,pre_tx_id, order_in_tx,user_address, utxo_balance ):
        self.hash = pre_tx_id # 사용할 UTXO가 포함된 트랜잭션 해쉬, 이전 트랜잭션의 ID가됨.
        self.n = order_in_tx # 위 트랜잭션 중에서 몇번째 UTXO인지
        self.address = user_address #위 UTXO의 수신주소 (사용자 공개키 해쉬 )
        self.value = utxo_balance #나에게 들어온 UTXO의 잔액
        self.sign = '' #서명!!
        self.pubk = '' #사용자의 공개키

class TxOut:
    def __init__(self, reciever, amount):
        self.to = reciever #받는놈 주소
        self.value = amount #금액

class Transaction:
    def __init__(self,blockchain, value, receiver_address, sender_address=None, sender_private_key=None):
        self.vin_sz = 0
        self.vout_sz = 0
        self.inputs = []
        self.outputs = []
        self.hash = None
        self.timestamp = time.time()

    def can_spent(self):
        for input in self.inputs:
            #pubk의 해쉬가 address가 맞는지
            #sign이 pubk로 풀리는지

            hashlib.sha256(str(self).encode()).hexdigest()
# pubk = privtopub(priv)
# addr = pubtoaddr(pubk)

    def gen_hash(self):
        #tx_in의 sign을 제외한 모든 데이터에 대한 hash
        #self.hash = str(self)
        pass

    def sign(self, priv):
        #tx_in들에 sign에 self.hash에 대한 서명을 작성
        pass