class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store :
            self.store[key] = []
        self.store[key].append([value , timestamp])

    def get(self, key: str, timestamp: int) -> str:
         result =  " "
         vals = self.store.get(key , [])
         l , r = 0 ,len(vals) - 1
         while l <= r :
              mid =( l + r) // 2
              if vals[mid][1] <= timestamp :
                result = vals[mid][0]
                l = mid + 1
              else : 
                  r = mid - 1
         return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
