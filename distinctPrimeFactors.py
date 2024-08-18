class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(n):
            factors = set()
            while n % 2 == 0:
                factors.add(2)
                n //= 2
            for i in range(3, int(n**0.5) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 2:
                factors.add(n)
            return factors
        distinct_primes = set()
        for num in nums:
            distinct_primes.update(prime_factors(num))
        return len(distinct_primes)
