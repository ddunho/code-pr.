#체인법으로 해시 함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:

    def __init__(self, key: Any, value: Any, next: Node) -> None:

        self.key = key
        self.value = value
        self.next = next
