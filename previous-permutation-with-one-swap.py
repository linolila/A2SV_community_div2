class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        idx = -1
        for i in range(n - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                idx = i
                break
        if idx == -1:
            return arr
        for i in range(n - 1, idx, -1):
            if arr[i] < arr[idx] and arr[i] != arr[i - 1]:
                swap_idx = i
                break
        
        
        arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
        
        return arr
