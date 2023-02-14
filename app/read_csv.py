import csv

def read_csv(path) :
  # 'r' solo permisos de lectura
  with open(path, 'r') as csvfile:
    # delimiter, la forma en que vienen separados los datos
    reader = csv.reader(csvfile, delimiter = ',')
    # para hacerlo diccionario hay que agarra el nombre de las columnas como las llaves, el primer iterable será ese
    header = next(reader) # 0 vamos a unir el header con un zip
    data = [] # 3 Necesito una lista por cada uno de esos diccionarios
    for row in reader :
      iterable = zip(header, row) # 1 ahora tenemos tuplas
      country_dict = {key : value for key, value in iterable} # 2 Ahora generaremos el diccionario | dictionary comprehension 
      data.append(country_dict) # 3
    return data 

if __name__ == '__main__' :
  data = read_csv('./app/data.csv')
  print(data[0])
# 0 Esto se nos presenta como un llista/array de datos y yo quiero un diccionario