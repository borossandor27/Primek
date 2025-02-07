'''Jav�tatlan pr�msz�m keres�s'''
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start_time = time.time()

print("Pr�m sz�mok 1 �s 10000 k�z�tt:")
for num in range(1, 10000):
    if is_prime(num):
        print(num)

end_time = time.time()
print(f"A fut�si id�: {end_time - start_time:.6f} m�sodperc")
