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