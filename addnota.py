"""
notas = ["do", "re", "mi", "fa", "sol", "la", "si"]

def addnota(nota, num):
 anota = nota[0]+nota[1]
 if anota == "so":
  anota = "sol"
 anum = int(nota.replace(anota, ""))
 if num >= 7-notas.index(anota):
  anum += 1
  anum += (num-(7-notas.index(anota)))/7
 anota = notas[(notas.index(anota)+num)%7]
 return "%s%d" % (anota, anum)

print addnota("do1", 8)
"""
notas = ["c", "d", "e", "f", "g", "a", "b"]

def addnota(nota, num):
     anota = nota[0]
     anum = int(nota.replace(anota, ""))
     if num >= 7-notas.index(anota):
      anum += 1
      anum += (num-(7-notas.index(anota)))/7
     anota = notas[(notas.index(anota)+num)%7]
     return "%s%d" % (anota, anum)
     
print addnota("c3", (77-9) / 4)
