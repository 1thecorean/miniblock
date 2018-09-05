from bitcoin import *

class TxIn:
    def __init__(self,pre_tx_id, pre_tx_output_index,sender_address, received_money, input_maker_pubkey ):

        #이전 트랜잭션의 해쉬값이 서명을 푼 것과 같고, 보낸 사람의 주소와 보낸사람의 공개키 해쉬가 같으면 참.
        self.pre_tx_id = pre_tx_id # 사용할 UTXO가 포함된 트랜잭션 해쉬, 이전 트랜잭션의 ID가됨.
        self.pre_tx_output_index = pre_tx_output_index # 위 트랜잭션 중에서 몇번째 UTXO인지
        self.sender_address = sender_address #위 UTXO의 발신주소 (발신자 공개키 해쉬 )
        self.received_money = received_money#받은 금액
        self.TxIn_sign = '' #현재 TxIn의 서명!!
        self.input_maker_pubkey = input_maker_pubkey #보낸 사람의 공개키



class TxOut:
    def __init__(self, receiver_address, send_money):
        self.receiver_address = receiver_address #송금,받을 사람 주소
        self.send_money = send_money #송금액



#블록은 Header, Transactions로 구성되어 있고 Transactions는
#Coinbase를 시작으로 tx1,tx2,tx3...으로 구성된다.
class Transaction:
    def __init__(self, utxo, value, receiver_address, input_maker_pubkey=None):
        self.timestamp = time.time()
        self.vin_sz = 0
        self.vout_sz = 0
        self.inputs = []
        self.outputs = []
        self.hash = None

        if input_maker_pubkey is None:
            txout = TxOut(receiver_address, value)
            self.outputs.append(txout)
            self.output_count = 1
            self.gen_hash()
            print("코인베이스 생성됨.")
            return

    def transaction_verify(self,my_private_key):
        if (ecdsa_verify(sha256(str(input)), input.TxIn_sign, my_private_key) and (
                pubtoaddr(input.sender_pubkey) == input.sender_address)):
            print("트랜잭션 이상무");
        else:
            print("이것은 잘못된 트랜잭션.")

    def gen_hash(self):
        self.vout_sz = len(self.outputs)
        self.vin_sz = len(self.inputs)
        self.hash = sha256(str(self))

    def sign(self, private_key):
        # tx_in들에 sign을 제외하고 sign에 self.hash에 대한 서명을 작성
        for tx_in in self.inputs:
            tx_in.pubk = privkey_to_pubkey(private_key)
            digest = sha256(str(tx_in))
            tx_in.sign = ecdsa_sign(digest, private_key)