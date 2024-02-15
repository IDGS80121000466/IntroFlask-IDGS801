from io import open

"""
CREAR EL ARCHIVO Y METERLE DATOS

archivo1=open('archivo.txt', 'a')
archivo1.write('\n saludo IDGS801 nuevo')
archivo1.close()
"""

""" LEE EL ARCHIVO"""
archivo1=open('archivo.txt', 'r')
"""IMPRIME UNA VEZ"""
print(archivo1.read()) 
"""IMPRIME LAS VECES QUE MANDES""" 
archivo1.seek(10)
print(archivo1.read())  

"""IMPRIME UNA VEZ EN FORMA DE LISTA"""
print(archivo1.readlines())
archivo1.close()