class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False

        # Create a character count for s1
        s1_count = [0] * 26
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        # Create a character count for the first s1_len characters of s2
        s2_count = [0] * 26
        for i in range(s1_len):
            s2_count[ord(s2[i]) - ord('a')] += 1

        # Check if the character counts match
        if s1_count == s2_count:
            return True

        # Slide the window through s2
        for i in range(s1_len, s2_len):
            s2_count[ord(s2[i]) - ord('a')] += 1
            s2_count[ord(s2[i - s1_len]) - ord('a')] -= 1

            if s1_count == s2_count:
                return True

        return False
