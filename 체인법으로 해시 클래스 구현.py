#체인법으로 해시 클래스 구현

class ChainedHash:

    def __init__(slef, capacity: int) -> None:

        self.capacity = capaciry
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:

        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(),16) % self.capacity)
        
