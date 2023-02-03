
cadea = "Un texto calquera"
numero = 5
booleano = True
print(type(booleano))

print(type(numero))

reais = 3e-15
print(type(reais))

complexo = 2.5 + 8.4j
print(type(complexo))

op = numero ** 2 #exponente
op2 = numero // 2 #division sin resto

resto = numero % 2


'''Operaciones a nivel de bit'''
operacion = 3 & 5


'''Operacion Boolean'''
print(True and False)
print(True or False)
print(not False)


'''Listas'''

l=[1,2,3,4,5]

print(type(l))
print(l[1:5]) #de 1º a 5º
print(l[1:5:2]) #de 1º a 5º salto de 2


l2=[1,2.3,True,"Elemento",[5,6,False]]

print(l2[4][1])
print(l2[4])

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

'''tuplas (no son modificables)'''
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print('\nDiccionarios\n')
'''Diccionarios'''

thisdict =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


print(thisdict)
print(thisdict["brand"])


'''Condicion'''

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
