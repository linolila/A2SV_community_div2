class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        s = list(answerKey) 
        max_consecutive = 0
        for ch in ['T', 'F']:
            left, right = 0, 0
            flips = 0
            while right < len(s):
                if s[right] != ch:
                    flips += 1
                while flips > k:
                    if s[left] != ch:
                        flips -= 1
                    left += 1
                max_consecutive = max(max_consecutive, right - left + 1)
                right += 1
        return max_consecutive
