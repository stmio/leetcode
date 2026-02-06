class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""

        values = self.map[key]
        n = len(values)
        res = ""

        l, r = 0, n - 1
        while 0 <= l <= r < n:
            mid = (l + r) // 2
            
            if values[mid][1] > timestamp:
                r = mid - 1
            else:
                res = values[mid][0] 
                l = mid + 1

        return res



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)