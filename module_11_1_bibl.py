import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#----------------pandas------------
    #библиотека pandas применяется для обработки и анализа табличных данных
    #В библиотеке pandas определены два класса объектов для работы с данными:
        #Series — одномерный массив, который может хранить значения любого типа данных;
        #DataFrame — двумерный массив (таблица), в котором столбцами являются объекты класса Series.

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print(s)
print()
s = pd.Series(np.linspace(0, 1, 5))
print(s)

        #Для Series доступно:
    # взятие элемента по индексу,
    # срезы,
    # поэлементные математические операции аналогично массивам numpy

s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Выбор одного элемента")
print(s["a"])
print("Выбор нескольких элементов")
print(s[["a", "d"]])
print("Срез")
print(s[1:])
print("Поэлементное сложение")
print(s + s)

    #Для Series можно применять фильтрацию данных по условию, записанному в качестве индекса:
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print("Фильтрация")
print(s[s > 2])

    #Объект класса DataFrame работает с двумерными табличными данными:
students_marks_dict = {"student": ["Студент_1", "Студент_2", "Студент_3"],
                       "math": [5, 3, 4],
                       "physics": [4, 5, 5]}
students = pd.DataFrame(students_marks_dict)
print(students)

    #Обычно табличные данные хранятся в файлах. Такие наборы данных принято называть дата-сетами.
# Файлы с дата-сетом могут иметь различный формат. Pandas поддерживает операции чтения и записи
# для CSV, Excel 2007+, SQL, HTML, JSON, буфер обмена и др. Несколько примеров:
    # CSV. Используется функция read_csv(). Аргумент file является строкой, в которой записан путь до файла с
# дата-сетом. Для записи данных из DataFrame в CSV-файл используется метод to_csv(file).
    # Excel. Используется функция read_excel(). Для записи данных из DataFrame в Excel-файл используется метод
# to_excel().
    # JSON. Используется функция read_json(). Для записи данных из DataFrame в JSON используется метод to_json().
#Для работы с другими форматами файлов в pandas есть функции, работающие аналогично.

students_300 = pd.read_excel('student_mark.xlsx')

#xlsx = pd.ExcelFile('student_mark.xlsx')
# Производим считывание данных первого листа
#sheet1_df = xlsx.parse('Лист1')
#print(sheet1_df)

#----------------NumPy------------
    #NumPy — библиотека, добавляющая поддержку больших многомерных массивов и матриц, вместе с большой библиотекой
# высокоуровневых (и очень быстрых) математических функций для операций с этими массивами.
# массивы могут хранить только значения одного типа

a = np.array([1, 2.5, 3])
print(a)
print(a.dtype)
b = np.array(['text', 1, 2.5], dtype='str')
print(b)
print(b.dtype)
c = np.array(['text', 1, 2.5])
print(c)
print(c.dtype)

    #Для работы с массивами доступны все стандартные арифметические операции, а также тригонометрические,
# экспоненциальная и другие функции. Выполнение математических операций над массивами происходит поэлементно.
# Размерность массивов должна совпадать при выполнении этих операций. Пример:
matr1 = np.array([9, 6, 8])
matr2 = np.array([1, 2, 4])
print(matr1 + matr2)
print(matr1 - matr2)
print(matr1 * matr2)
print(matr1 / matr2)

    #Для умножения матриц используется операция @ или функция dot:
matrix1 = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
matrix2 = np.array([[0, 0, 1],
              [0, 1, 0],
              [1, 0, 0]])
print(matrix1 @ matrix2)
print(matrix1 * matrix2)

    #Матрицы можно транспонировать функцией transpose() и поворачивать функцией rot90(). При повороте можно указать
# направление поворота вторым аргументом:
matr_tran = np.arange(1, 13).reshape(4, 3)
print(matr_tran)
print("Транспонирование")
print(matr_tran.transpose())
print("Поворот влево")
print(np.rot90(matr_tran))
print("Поворот вправо")
print(np.rot90(matr_tran, -1))

#------------------matplotlib----------------------

    #Для визуализации данных pandas использует библиотеку matplotlib:

students = pd.read_excel('student_mark.xlsx')
plt.hist(students["physics"], label="Тест по физике")
plt.xlabel("Баллы за тест")
plt.ylabel("Количество студентов")
plt.legend()
plt.show()


