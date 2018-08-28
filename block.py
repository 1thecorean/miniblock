import time
import hashlib
import json
class Block:
    def __init__(self,prev_hash=None,timestamp=time.time(),mrkl_root=None,bits=3,nounce=0,hash=None,transactions=[]):
        self.prev_hash = None
        self.timestamp = time.time()
        self.mrkl_root = None
        self.bits = 3
        self.nounce = 0
        self.hash = None
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def gen_mrkl_root(self):
        data_len = len(self.transactions)
        tmp_merkle = []
        for t in self.transactions :
            tmp_merkle.append(t.hash)

        if data_len % 2 != 0:
            tmp_merkle.append(tmp_merkle[-1])

        while len(tmp_merkle) != 1:
            tmp = []
            for i in range(0, len(tmp_merkle), 2):
                tmp.append(hashlib.sha256(
                    (tmp_merkle[i] + tmp_merkle[i+1]).encode() )
                           .hexdigest())
            tmp_merkle = tmp

        self.mrkl_root = tmp_merkle[0]

    def gen_hash(self):
        while True:
            h = hashlib.sha256(str(self).encode()).hexdigest()
            self.nounce += 1
            if h[:self.bits] == '0' * self.bits:
                self.hash = h
                break

    def __str__(self):
        return json.dumps(self.__dict__, sort_keys=True)

    def load(self, **kvs):
        self.__dict__.update(kvs)

if __name__ == '__main__':
    s = 'hello world'
    b = Block()
    # print(b)
    b.add_transaction('Hello')
    b.add_transaction('World')
    b.gen_hash()
    print(b)
    obj = json.loads(str(b))

    b2 = Block()
    b2.load(obj)

    # obj = Block(**obj)
    print(obj)
