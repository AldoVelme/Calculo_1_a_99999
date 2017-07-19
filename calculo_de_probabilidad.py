# -*- coding: cp1252 -*-
import random
#
CheckPlusThatOne=0
ProbCount=0
Cicle=0

#
#ciclo de comprobación
while True:
    bound = raw_input("Ingrese probalididad entera entre 1 y 99999 : ")
    try:
        if float(bound) >= 1 and float(bound) <= 99999:
            bound = float(bound)
            break
        else:
            continue
    except:
        continue

#ciclo de enterizacion
n=bound
while True:
    if n>0:
        n=int(n)
        break
    else:
        CheckPlusThatOne+=1
        n=n*10
        if CheckPlusThatOne > 5:
            #barrera en caso de dar una probabilidad no redondeable ej:10.2443545345
            #de esta forma solo subirá la "enterización" cinco veces -> 1024435.45345
            n=int(n)
            #A continuacion se vuelve numero entero para poder usarse en el siguiente ciclo.
            break

#generador de probabilidad
while True:
    Cicle+=1
    num = random.randint(1,1000*(100**CheckPlusThatOne))
    if num <= n:
        ProbCount+=1
        print 1
    else:
        print 0
    seguir=raw_input("... ")
    if seguir != "":
        break
print "probabilidad: ", float(ProbCount)/Cicle, "%"
