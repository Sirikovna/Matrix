import numpy as np

print("1. Найти индексы элементов, значения которых равны 5 в случайном массиве")
np.random.seed(42) 
arr1 = np.random.randint(1, 11, size=15)
indices = np.where(arr1 == 5)[0]
print(f"Случайный массив: {arr1}")
print(f"Индексы элементов со значением 5: {indices}")
print(f"Количество элементов со значением 5: {len(indices)}")
print()

print("2. Создать вектор размера 10 со значениями от 1 до 12")
arr2 = np.linspace(1, 12, 10, endpoint=False)
print(f"Вектор: {arr2}")
print(f"Размер вектора: {arr2.size}")
print()

print("3. Поменять знак у элементов, значения которых больше 8 в случайной матрице")
np.random.seed(123)
matrix3 = np.random.randint(1, 16, size=(4, 5))
print(f"Исходная случайная матрица 4x5:\n{matrix3}")
print(f"Количество элементов > 8: {np.sum(matrix3 > 8)}")
matrix3_modified = matrix3.copy()
matrix3_modified[matrix3_modified > 8] *= -1
print(f"Матрица после изменения знака у элементов > 8:\n{matrix3_modified}")
print(f"Проверка - элементы которые изменили знак: {np.sum(matrix3_modified < 0)}")
print()

print("4. Создать случайную матрицу 3x4 и удалить [1,2] колонки")
np.random.seed(42)
matrix4 = np.random.randint(1, 51, size=(3, 4))
print(f"Исходная матрица:\n{matrix4}")
matrix4_modified = np.delete(matrix4, [1, 2], axis=1)
print(f"Матрица после удаления колонок [1,2]:\n{matrix4_modified}")
print()

print("5. Считать матрицу из файла и разделить на четные/нечетные строки")
m0_test = np.random.randint(1, 100, size=(8, 6))
np.savetxt('matrix_m0.txt', m0_test, fmt='%d')
m0 = np.loadtxt('matrix_m0.txt', dtype=int)
print(f"Матрица m0 (8x6):\n{m0}")
m1 = m0[::2] 
m2 = m0[1::2]
print(f"\nМатрица m1 (четные строки):\n{m1}")
print(f"Размер m1: {m1.shape}")
print(f"\nМатрица m2 (нечетные строки):\n{m2}")
print(f"Размер m2: {m2.shape}")
print()

print("6. Создать матрицу с 0 внутри и 1 на границах")
def create_border_matrix(rows, cols):
    matrix = np.zeros((rows, cols), dtype=int)
    matrix[0, :] = 1      
    matrix[-1, :] = 1     
    matrix[:, 0] = 1      
    matrix[:, -1] = 1   
    return matrix
matrix6 = create_border_matrix(6, 8)
print(f"Матрица 6x8 с 1 на границах и 0 внутри:\n{matrix6}")

