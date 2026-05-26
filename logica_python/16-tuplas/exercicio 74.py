from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100),
           randint(1, 100), randint(1, 100))

print("Os valores sorteados foram: ", end="")
for n in numeros:
    print(f"{n} ", end="")

print(f"\nO maior valor sorteado foi o {max(numeros)}")
print(f"O menor valor sorteado foi o {min(numeros)}")
