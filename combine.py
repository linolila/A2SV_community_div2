class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            # If the path length is k, we have a valid combination
            if len(path) == k:
                result.append(path[:])
                return
            
            # Explore further numbers to add to the current path
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)  # Move to the next number
                path.pop()  # Backtrack to try another number

        result = []
        backtrack(1, [])
        return result
