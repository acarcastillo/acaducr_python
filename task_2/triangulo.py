num = input("Ingrese un número: ")
while not num.isdigit():
    num = input("Error: Debe ingresar un número. Ingrese nuevamente: ")

num = int(num)
for i in range(1, num+1):
    for j in range(1, i+1):
        print(j, end="")
    print()