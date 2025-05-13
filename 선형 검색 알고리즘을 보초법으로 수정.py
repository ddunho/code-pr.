#선형 검색 알고리즘을 보초법으로 수정

from typing import Any, Sequence
import copy

def seq__search(seq: Sequence, key: Any) -> int:
    a = copy.deepcopy(seq)
