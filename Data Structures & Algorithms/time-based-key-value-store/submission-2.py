class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self._map[key]
        if len(arr) == 0: return ""

        left, right = 0, len(arr) -1
        max_index = -1
        while left <= right:
            mid = left + (right - left)// 2

            if arr[mid][0] < timestamp:
                max_index = max(max_index, mid)
                left = mid + 1
            elif arr[mid][0] > timestamp:
                right = mid - 1
            else:
                return arr[mid][1]

        if max_index >= 0:
            return arr[max_index][1]
        else:
            return ""

        
