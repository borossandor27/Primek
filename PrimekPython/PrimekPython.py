'''Javítatlan prímszám keresés'''
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start_time = time.time()

print("Prím számok 1 és 10000 között:")
for num in range(1, 10000):
    if is_prime(num):
        print(num)

end_time = time.time()
print(f"A futási idõ: {end_time - start_time:.6f} másodperc")
