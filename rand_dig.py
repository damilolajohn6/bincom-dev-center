import random

random_number = "".join(random.choices(["0", "1"], k=4))
decimal_number = int(random_number, 2)

print("Random 4-digit number:", random_number)
print("Decimal equivalent:", decimal_number)
