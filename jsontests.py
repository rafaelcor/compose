import json

notas = ["c", "d", "e", "f", "g", "a", "b"]

def oaddnota(nota, num):
    anota = nota[0]
    anum = int(nota.replace(anota, ""))
    if num >= 7-notas.index(anota):
     anum += 1
     anum += (num-(7-notas.index(anota)))/7
    anota = notas[(notas.index(anota)+num)%7]
    return "%s%d" % (anota, anum)

def save(datos):
    archivo = open("save.json", "w")
    json.dump(datos, archivo)
    archivo.close()

def load():
    archivo = open("save.json")
    datos = json.load(archivo)
    archivo.close()
    return datos

