class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        digits = list(str(abs(num)))
        if num < 0:
            digits.sort(reverse=True)
            return -int("".join(digits))
        else:
            digits.sort()
            # Find the first non-zero digit
            for i, digit in enumerate(digits):
                if digit != "0":
                    digits.pop(i)
                    digits.insert(0, digit)
                    break
            return int("".join(digits))
