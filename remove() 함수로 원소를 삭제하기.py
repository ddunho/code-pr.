#remove() 함수로 원소를 삭제하기

def remove(self, key: Any) -> bool:
    hash = self.hash_value(key)
    p = self.table[hash]
    pp = None
