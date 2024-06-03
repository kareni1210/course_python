import numpy as np

# Matriz A
A = np.array([
    [1, -0.942857, 0, 0, 0],
    [0, 1, -0.942857, 0, 0],
    [0, 0, 1, -0.942857, 0],
    [0, 0, 0, 1, -0.942857],
    [0, 0, 0, 0, 1]
])

# Vector b
b = np.array([1171.429, 1171.429, 1171.429, 1171.429, 2904.762])

# Resolver el sistema de ecuaciones lineales
reservas = np.linalg.solve(A, b)

# Mostrar resultados
print("Reservas necesarias al inicio de cada año:")
for i, R in enumerate(reservas):
    print(f"R{i} = {R:.2f}")





# import numpy as np
#
# # Definir la matriz A
# A = np.array([
#     [0.1, 0.2, 0.1, 0.05, 0.1, 0.15],
#     [0.3, 0.1, 0.15, 0.1, 0.2, 0.1],
#     [0.2, 0.25, 0.1, 0.05, 0.15, 0.1],
#     [0.1, 0.15, 0.1, 0.2, 0.05, 0.1],
#     [0.05, 0.1, 0.05, 0.05, 0.1, 0.1],
#     [0.2, 0.1, 0.15, 0.1, 0.1, 0.1]
# ])
#
# # Crear la matriz identidad I de tamaño 6x6
# I = np.identity(6)
#
# # Calcular la matriz (I - A)
# I_minus_A = I - A
# print(I_minus_A)
#
# # Calcular la inversa de (I - A)
# I_minus_A_inv = np.linalg.inv(I_minus_A)
#
# # Definir el vector de demanda final D
# D = np.array([50, 100, 150, 80, 60, 90])
#
# # Calcular el vector de producción total X
# X = np.dot(I_minus_A_inv, D)
#
# print("La matriz inversa de (I - A) es:")
# print(I_minus_A_inv)
# print("\nEl vector de producción total X es:")
# print(X)



# # Definimos la matriz de coeficientes y el vector de demanda final
# A = np.array([
#     [0.1, 0.2, 0.1, 0.05, 0.1, 0.15],
#     [0.3, 0.1, 0.15, 0.1, 0.2, 0.1],
#     [0.2, 0.25, 0.1, 0.05, 0.15, 0.1],
#     [0.1, 0.15, 0.1, 0.2, 0.05, 0.1],
#     [0.05, 0.1, 0.05, 0.05, 0.1, 0.1],
#     [0.2, 0.1, 0.15, 0.1, 0.1, 0.1]
# ])
#
# d = np.array([50, 100, 150, 80, 60, 90])
#
# # Calculamos la matriz identidad
# I = np.eye(6)
# # print(I)
#
# # Calculamos (I - A)
# I_minus_A = I - A
# print(I_minus_A)
#
# # # Calculamos la inversa de (I - A)
# # I_minus_A_inv = np.linalg.inv(I_minus_A)
# # print(I_minus_A_inv)
# #
# # # Calculamos el vector de producción x
# # x = np.dot(I_minus_A_inv, b)
# x = np.linalg.solve(I_minus_A, d)
# print("Los niveles de producción necesarios son:", x)
