#키로 원소를 검색하는 search()함수

def search(self, key: Any) -> Any:
        hash = self.hash_value(key)
        p = self.table[hash]

        while p is not None:
            if p.key == key:
                return p.value
            p = p.next

        return None

def add(self, key: Any, value: Any) -> bool:
     hash = self.hash_value(key)
     p = self.table[hash]

     while p is not None:
          if p.key == key:
               return False
          p = p.next
    
            
