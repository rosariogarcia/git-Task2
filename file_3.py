#Descomposicion de numeros

entrada = 123
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
