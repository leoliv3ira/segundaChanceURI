quantidadesAlnos = int(input())
listaNota1 = []
listaNota2 = []
notaFinal = []
notasAlteradas = 0

for i in range(0,quantidadesAlnos):
    primeiraNota = float(input())
    listaNota1.append(primeiraNota)
    
y = 0

for i in range (0,quantidadesAlnos):
    segundaNota = float(input())
    listaNota2.append(segundaNota)
    if listaNota1[y] == 10:
        var = (listaNota1[y])
        notaFinal.append(var)
        y += 1
    elif segundaNota == 10 and listaNota1[y] == 9:
        var = (listaNota1[y]) + 1
        notaFinal.append(var)
        notasAlteradas += 1
        y += 1
    elif segundaNota == 10 and listaNota1[y] != 9:
        var = (listaNota1[y]) + 2
        notaFinal.append(var)
        notasAlteradas += 1
        y += 1
    else:
        var = (listaNota1[y])
        notaFinal.append(var)
        y += 1
        
            
x = 1
z = 0
print(f"NOTAS ALTERADAS: {notasAlteradas}")
while x <= quantidadesAlnos:
    if (listaNota1[z]) == 10 and (notaFinal[z]) == 10:
        print(f"-({x:03}) original: {(listaNota1[z]):.2f} | final: {(notaFinal[z]):.2f}")
    elif (listaNota1[z]) != 10 and (notaFinal[z]) == 10:
        print(f"*({x:03}) original: 0{(listaNota1[z]):.2f} | final: {(notaFinal[z]):.2f}")
    elif ((listaNota1[z]) != 10 and (notaFinal[z]) != 10) and (listaNota1[z]) == (notaFinal[z]):
        print(f"-({x:03}) original: 0{(listaNota1[z]):.2f} | final: 0{(notaFinal[z]):.2f}")
    elif (listaNota1[z]) != 10 and (notaFinal[z]) != 10:
        print(f"*({x:03}) original: 0{(listaNota1[z]):.2f} | final: 0{(notaFinal[z]):.2f}")
    x += 1
    z += 1
