from bitcoin import *

class TxIn:
    def __init__(self):
        self.hash = None # 사용할 UTXO가 포함된 트랜잭션 해쉬.ID
        self.n = 0 # 위 트랜잭션 중에서 몇번째 UTXO인지
        self.address = '' #위 UTXO의 수신주소 ( 그러니까 공개키 해쉬 )
        self.value = '' #위 UTXO의 잔액
        self.sign = '' #서명!!
        self.pubk = '' #사용자의 공개키

class TxOut:
    def __init__(self):
        self.to = '' #받는놈 주소
        self.value = '' #금액

class Transaction:
    def __init__(self):
        self.vin_sz = 0
        self.vout_sz = 0
        self.inputs = []
        self.outputs = []
        self.hash = None

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