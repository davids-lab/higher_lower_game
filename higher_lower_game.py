from art import logo,vs
from game_data import data
import os
import random

acierto = True
compare_a = {} 
compare_b = {}
print(logo)

def generador_comparaciones (ejecucion_cantidad, residual):
  global compare_a
  global compare_b 
  if ejecucion_cantidad == 1:
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    print(f"Compara A: {compare_a['name']}, {compare_a['description']},de {compare_a['country']}\n")
    print(vs)
    print(f"\nCompara B: {compare_b['name']}, {compare_b['description']},de {compare_b['country']}\n")
    return compare_b
  else:
    compare_a = residual
    compare_b = random.choice(data)
    print(f"Compara A: {compare_a['name']}, {compare_a['description']},de {compare_a['country']}\n")
    print(vs)
    print(f"\nCompara B: {compare_b['name']}, {compare_b['description']},de {compare_b['country']}\n")
    return compare_b

def logica_comparacion (comparacion_1, comparacion_2):
  if comparacion_1['follower_count'] > comparacion_2['follower_count']:
    return "a"
  elif comparacion_1['follower_count'] < comparacion_2['follower_count']:
    return "b"

puntos = 0
ejecucion = 1
eleccion_residual = {}

while acierto == True:
  eleccion_residual = generador_comparaciones(ejecucion, eleccion_residual)
  eleccion_usuario = input("¿Quien tiene mas seguidores?(A o B) :").lower()
  os.system('cls')
  print(logo)
  if eleccion_usuario == logica_comparacion(compare_a, compare_b):
    puntos += 1
    print(f"Buena eleccion. Tu puntaje actual:{puntos}")
    if eleccion_usuario == "a":
      eleccion_residual = compare_a 
    elif eleccion_usuario == "b":
      eleccion_residual = compare_b
  else:
    print(f"No es correcto. Tu puntuacion final es : {puntos}")
    acierto = False
    
  ejecucion += 1