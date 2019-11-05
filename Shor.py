import random
from fractions import gcd

n = 23 * 41

def modexp(x, e, n):
  y = 1
  while e > 1:
    if (e % 2 == 1):
      y = x * y
      y = y % n
    x = x * x
    x = x % n 
    e = e // 2
  return (x * y) % n

a = 0
r = 0
while True:
  a = random.randint(1, n-1)
  r = random.randint(1, n-1)
  while(modexp(a, r, n) != 1):
    r = random.randint(1, n-1)
  if(r % 2 == 1):
    continue;
  if(modexp(a, r/2, n) == n - 1):
    continue;
  factor1 = gcd(modexp(a, r/2, n)+1, n)
  factor2 = n // factor1
  if (factor1 != 1 and factor2 != 1):
    break;
print("factors:")
print(factor1)
print(factor2) 
