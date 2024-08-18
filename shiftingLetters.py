class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            diff[start] += shift_value
            if end + 1 < n:
                diff[end + 1] -= shift_value
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += diff[i]
            net_shifts[i] = current_shift
        result = []
        for i in range(n):
            char = s[i]
            shift_amount = net_shifts[i] % 26  
            new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
