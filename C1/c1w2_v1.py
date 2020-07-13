import re
import numpy as np
from scipy.spatial import distance


# Считаем строки из файла в список,
with open("sentences.txt", "r") as file:
    file_text = file.read().split("\n")
    sentences = map(lambda x: x.lower(), file_text)

# Разделим строки на отдельные слова
sentences = map(lambda x: re.split('[^a-z]', x), sentences)
sentences = map(lambda x: [w for w in x if w != ''], sentences)  # sentences - двумерный массив

# Составим список всех слов, встречающихся в тексте
sentences = list(sentences)
text_as_sets = sentences[:]
text_as_sets = map(lambda x: set(x), text_as_sets)
words = set()
for sentence in text_as_sets:
    words.update(sentence)
text_as_sets = None
words = list(words)  # список всех слов

# Составим матрицу размера n*d, где n - число предложений
matrix = []
temp_list = []
for sentence in sentences:
    for word in words:
        temp_list.append(sentence.count(word))
    matrix.append(temp_list)
    temp_list = []
matrix = np.array(matrix)

# Считаем  косинусное расстояние от первого предложения
first_sentence = matrix[0]
cos_distances = dict()
counter = 1
for vector in matrix[1:]:
    cos_distances[counter] = distance.cosine(vector, first_sentence)
    counter += 1

# Ищем два ближайших предложения
closest_sentence = min(cos_distances, key = cos_distances.get)
del cos_distances[closest_sentence]
second_closest = min(cos_distances, key = cos_distances.get)
print(closest_sentence, second_closest)

# Запишем ответ в файл
with open("answer1.txt", "w") as answer:
    answer.write(str(closest_sentence) + ' ' + str(second_closest))