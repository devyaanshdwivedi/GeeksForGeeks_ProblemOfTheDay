#User function Template for python3
class Solution:
    def solve (self,Num1,Num2):
        def isPrime(n):
            if n == 2 or n == 3:
                return True
            if n <= 1 or n % 2 == 0 or n % 3 == 0:
                return False
            end = int(n**0.5 + 1)
            for i in range(5, end, 6):
                if n % i == 0 or n % (i + 2) == 0:
                    return False
            return True
            
        if Num1 == Num2:
            return 0
        prime = [False] * 10000
        for i in range(1000, 10000):
            prime[i] = isPrime(i)
            
        q = [(Num1, 0)]
        not_visited = [True] * 10000
        while q:
            p = q[0]
            q.pop(0)
            for i in range(1, 10):
                for j in [1, 10, 100, 1000]:
                    num = p[0] + i * j
                    if p[0] % (j * 10) > num % (j * 10):
                        num -= j * 10
                    if prime[num]:
                        if num == Num2:
                            return p[1] + 1
                        elif not_visited[num]:
                            not_visited[num] = False
                            q.append((num, p[1] + 1))
        return -1

