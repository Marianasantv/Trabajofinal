list = (4,5,2,6,3,5)
def binary_search (lista,search):
  principio = 0
  final =  len(lista)-1
  while principio<= final:
    mitad = (principio + final)//2
    if lista[mitad] == search:
      return "Si se encuentra en la lista"
    elif lista [mitad] < search:
      principio = mitad + 1
    elif lista[mitad] > search:
      final = mitad - 1
  return "No se encuentra en la lista"

print(binary_search(list,2))

