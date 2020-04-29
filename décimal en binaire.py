result = []
print("Entrer un nombre")
nombre = input()
nq = int(nombre)
first_nombre = nombre

while nq > 0:
    nq,nr = divmod(nq, 2)
    if nr == 0:
        result.append('0')
    else:
        result.append('1')

result.reverse()
print("La version bianaire de " + str(first_nombre) + " est:" + "".join(result))
