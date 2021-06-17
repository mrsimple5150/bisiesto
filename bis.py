a = int(input("introduce un año: "))
if a % 4 == 0 and a % 100 != 0:
    print("Si, 1ro")
elif a % 4 == 0 and a % 400 == 0:
    print("Si, 1ro")
else:
    print("no, 1ro")

print("\nSegundo programa\n")

anio = int(input("introduce un año: "))

if anio % 4 != 0:#debe cumplir siempre
    print("no, 2do")
else:
    if anio % 100 != 0 or anio % 400 == 0:#si cumple 1ra no importa cual cumpla aqui
        print("si, 2do")
    else:
        print("no, 2do")
