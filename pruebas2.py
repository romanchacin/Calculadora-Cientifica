# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns
import math
# sns.distplot(random.normal(size=1000), hist=False)

# plt.show()

import math

def eval_degrees(expression):
  """Evalua una expresión matemática en grados.

  Args:
    expression: La expresión matemática a evaluar.

  Returns:
    El valor de la expresión evaluada en grados.
  """

  # Convertir la expresión a una lista de tokens.
  tokens = expression.split()

  # Iterar sobre los tokens.
  for token in tokens:
    # Si el token es una función trigonométrica, convertirla a grados.
    if token in ["sin", "cos", "tan", "cot", "sec", "csc"]:
      tokens[tokens.index(token)] = math.radians(float(token))

  # Evaluar la expresión en grados.
  result = eval(" ".join(tokens))

  # Convertir el resultado a grados.
  result = math.degrees(result)

  return result

print(eval_degrees("cos(60) - 3"))