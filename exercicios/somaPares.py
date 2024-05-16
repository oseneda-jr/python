# Soma pares a partir do número dado, se o número for impar,
# começa do par subsequente.

import sys

numero: int
resultado: int = 0
x: int

print("Informe um numero: ")
numero = int(sys.stdin.readline())

if numero % 2 != 0:
  numero += 1

x = numero

while x < numero + 10:
  resultado += x
  x += 2

print("O resultado é = ", resultado)