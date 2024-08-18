class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
            def is_prime(n):
                    if n <= 1:
                        return False
                    if n <= 3:
                        return True
                    if n % 2 == 0 or n % 3 == 0:
                        return False
                    i = 5
                    while i * i <= n:
                        if n % i == 0 or n % (i + 2) == 0:
                            return False
                        i += 6
                    return True

            def primes_in_range(left, right):
                    primes = []
                    for num in range(left, right + 1):
                        if is_prime(num):
                            primes.append(num)
                    return primes
            primes = primes_in_range(left, right)
            if len(primes) < 2:
                return [-1, -1]
            
            min_diff = float('inf')
            result = [-1, -1]
            
            for i in range(len(primes) - 1):
                num1 = primes[i]
                num2 = primes[i + 1]
                diff = num2 - num1
                if diff < min_diff:
                    min_diff = diff
                    result = [num1, num2]
            
            return result

            
                
