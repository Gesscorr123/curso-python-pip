# Puedo hacer mis propios módulos, cada archivo con la extención .py es un módulo | ahí podemos definir clases, funciones o variables

def get_population(country_dict) :
  population_dict = {
    '2022' : int(country_dict['2022 Population']), 
    '2020' : int(country_dict['2020 Population']), 
    '2015' : int(country_dict['2015 Population']), 
    '2010' : int(country_dict['2010 Population']),  
    '2000' : int(country_dict['2000 Population']),  
    '1990' : int(country_dict['1990 Population']), 
    '1980' : int(country_dict['1980 Population']), 
    '1970' : int(country_dict['1970 Population']), 
  }
  return population_dict.keys(), population_dict.values()

# A = 'hola c:' por lo general solo se tiene funciones

def get_column(data, column):
  data = list(filter(lambda item : item['Continent'] == 'South America', data)) # Reducimos la data para que el chart duera más fácil de leer
  
  labels = [ country.get('Country/Territory') for country in data]
  data_columns = [ country.get(column) for country in data]
  
  '''for country in data :
    labels.append(country.get('Country/Territory'))'''
    
  dict = {label : data_column for (label, data_column) in zip(labels, data_columns)}
  return dict.keys(), dict.values()


def population_by_country(data, country) :
  result = list(filter(lambda item : item['Country/Territory'] == country, data))
  return result