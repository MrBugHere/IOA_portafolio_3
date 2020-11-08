# Le da formato py al txt de 1.000.000 de linas
f = open("ShortestPathInstance_1000x1000000.txt","r")
a = open("../casos/salida.py","a")
i = 0
for l in f:
    i += 1
    if i > 7:
        line = l.rstrip('\n')
        line = line.replace(' ',',')
        line = '['+line+'],'
        a.write(line)
        a.write("\n")
f.close()
a.close()