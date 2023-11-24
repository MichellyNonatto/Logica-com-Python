import sys
lista = []
for line in sys.stdin:
    line = line.rstrip()
    lista.append(line)
   
for i in lista:
    print(i)
