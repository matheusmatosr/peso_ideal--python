def info(): 
  sexo = input('Sexo (M ou F): ')
  h = float(input('Altura: '))
  return sexo, h

def calculo(sexo, h):
  if sexo == 'M':
   return (72.7*h) - 58
  elif sexo == 'F':
    return (62.1*h) - 44.7 
  else:
    return -1

def exibir(peso):
  if peso == -1:
    print('Erro, dados invalidos')
  else:
    print(peso)

carac = info()
valor = calculo(carac[0], carac[1])
exibir(valor)