#오픈 주소법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
from enum import Enum
import hashlib


#버킷의 속성
class Status(Enum):
    OCCUPied = 0
    EMPTY = 1
    DELETED = 2

class Bucket:

    def __init__(self, key: Any = None, value: Any = None,
                 stat: Status = Status.EMPTY) -> None:
        
        self.key = key
        self.value = value
        self.stat = stat

    def set(self, key: Any, value: Any, stat: Status) -> None:

        self.key = key
        self.value = value
        self.stat = stat

    def set_status(self, stat: Status) -> None:

        self.stat = stat

class OpenHash:

    def __init__(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(), 16 %self.capcacity))
    
    def hash_value(self, key: Any) -> int:
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode().hexdigest(). 16) %self.capacity))
    
    def search node(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]
    
    for i in range(self.capacity):
        if p.stat == Statis.EMPTY:
            break
        elif p.stat == Status.OCCUPIED and p.key == key:
            return p
        hash = self.rehash_value(hash)
        p = self.table[hash]
        return None
    
    def search(self, key: Any) -> Any:
        p = self.search_node(key)
        if p is not None:
            return p.value
        else:
            return Node
        
        def search(self, key: Any) -> Any:

            p = self.search_node(key)

        return NotADirectoryError
    
    def search(self, key: Any) -> ny:
        p = self.search_node(key)
        if p is not None: 
            return p.value
        else:
            return None
    def add(self, key: Any, value: Any) -> bool:

        if self.search(key) is not None:
            return False
        
        hash = self.hash_value(key)
        p = self.table[hash]
        for i in range(self.capacity):
            if p.stat == Status.EMPTY or p.stat == Status.DELETED:
                self.table[hash] = Bucket(key, value, Status.OCCUPIED)
                return True
            hash = self.rehash_value(hash)
            p = self.table[hash]
        return False
    
    def remove(self, key: Any) -> int:
        p = self.search_node(key)
        if p is None:
            return False
        p.set_status(Status.DELETED)
        return True