#체인법으로 해시 클래스 구현

class ChainedHash:

    def __init__(slef, capacity: int) -> None:

        self.capacity = capaciry
        self.table = [None] * self.capacity
        
