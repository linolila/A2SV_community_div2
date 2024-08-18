class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(start: int, path: List[str]):
                # If we have 4 segments and we've used all characters
                if len(path) == 4:
                    if start == len(s):
                        # Join the segments with dots and add to result
                        result.append('.'.join(path))
                    return
                
                # If we have too many segments or run out of characters
                if len(path) > 4 or start >= len(s):
                    return
                
                # Try segments of length 1 to 3
                for length in range(1, 4):
                    if start + length > len(s):
                        break
                    segment = s[start:start + length]
                    
                    # Validate the segment
                    if (length > 1 and segment[0] == '0') or int(segment) > 255:
                        continue
                    
                    # Recur for the next segment
                    path.append(segment)
                    backtrack(start + length, path)
                    path.pop()  # Backtrack

        result = []
        backtrack(0, [])
        return result 
