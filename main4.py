""""Дано три змінні: X, Y, Z.
Якщо їх значення впорядковані за спаданням, то подвоїти їх;
в іншому випадку замінити значення кожної змінної на протилежне."""
import random

x = random.randint(1, 10)
y = random.randint(1, 10)
z = random.randint(1, 10)
print(x, y, z)

if x < y < z:  # x > y > z
    x, y, z = x * 2, y * 2, z * 2
else:
    x, y, z = -x, -y, -z
print(x, y, z)
