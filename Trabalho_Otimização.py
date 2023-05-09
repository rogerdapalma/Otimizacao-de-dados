# -*- coding: utf-8 -*-
"""Cópia de aula 01 (feito)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e13sMt8CgrVY2HOuWzwwlNwZAR-cdMOo
"""

import numpy as np
import matplotlib.pyplot as plt

constraints = []

# Pede ao usuário para digitar o número de restrições
num_constraints = int(input("Digite o número de restrições: "))

# Pede ao usuário para digitar as restrições na forma 'ax + by <= c'
for i in range(num_constraints):
    while True:
        constraint_str = input(f"Digite a restrição {i+1} na forma 'ax +/- by <= c': ")
        operator_idx = constraint_str.find("<=")
        if operator_idx == -1:
            operator_idx = constraint_str.find(">=")
            if operator_idx == -1:
                operator_idx = constraint_str.find("=")
        if operator_idx == -1:
            print("Entrada inválida. Operador de comparação não encontrado. Tente novamente.")
            continue
        
        operator = constraint_str[operator_idx:operator_idx+2]
        try:
            terms = constraint_str[:operator_idx].strip().split()
            a = float(terms[0])
            if len(terms) > 1 and terms[1] in "+-":
                b = float(terms[1] + terms[2])
            else:
                b = float(terms[1])
            c = float(constraint_str[operator_idx+2:].strip())
            if operator == ">=":
                a = -a
                b = -b
                c = -c
            constraints.append((a, b, c))
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

# Define as restrições
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)

# Cria as restrições a partir das entradas do usuário
for a, b, c in constraints:
    y_constraint = (c - a * x) / b
    plt.plot(x, y_constraint, label=f"{a}x + {b}y {operator} {c}")
    
    # Define as regiões viáveis
    if operator == "<=":
        y_constraint[y_constraint < 0] = np.nan
    else:
        y_constraint[y_constraint > 0] = np.nan
    plt.fill_between(x, y_constraint, color='blue', alpha=0.2)
    
    # Encontra a interseção com os eixos x e y
    x_intersection = c / a if a != 0 else np.nan
    y_intersection = c / b if b != 0 else np.nan
    
    # Verifica se a interseção está dentro dos limites do gráfico
    if 0 <= x_intersection <= 10:
        plt.plot(x_intersection, 0, 'ro')
    if 0 <= y_intersection <= 10:
        plt.plot(0, y_intersection, 'ro')

        # Encontra e plota os pontos de interseção
    for i in range(len(constraints)):
      for j in range(i+1, len(constraints)):
        a1, b1, c1 = constraints[i]
        a2, b2, c2 = constraints[j]
        det = a1*b2 - a2*b1
        if det != 0:
            x_intercept = (c1*b2 - c2*b1) / det
            y_intercept = (a1*c2 - a2*c1) / det
            if 0 <= x_intercept <= 7 and 0 <= y_intercept <= 7:
                plt.plot(x_intercept, y_intercept, 'ro')
                print(f"Interseção das restrições {i+1} e {j+1}: ({x_intercept}, {y_intercept})")

plt.plot(0, 0, 'ro')
plt.xlim((0, 7))
plt.ylim((0, 7))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper right')
plt.show()