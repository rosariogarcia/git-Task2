#Descomposicion de numeros

entrada = 999
#inicializamos la posicion en 0
posicion = 0

digito = entrada % 10
print ('digito: ', digito, 'posicion: ', posicion)

entrada = entrada // 10
posicion = posicion + 1
digito = entrada % 10
print ('digito: ', digito, 'posicion: ', posicion)

entrada = entrada // 10
posicion = posicion + 1
digito = entrada % 10
print ('digito: ', digito, 'posicion: ', posicion)
