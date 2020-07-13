import re
import numpy as np
from scipy.spatial.distance import cosine

text = []
with open('sentences.txt') as file:
    for line in file:
        lst = re.split('[^a-z]', line.lower()[:-1])
        text.append(list(filter(lambda x: x != '', lst)))
        
words = set()

for line in text:
    for i in line:
        words.add(i)
        
matrix = []
for line in text:
    lst = []
    for word in words:
        lst.append(line.count(word))
    matrix.append(lst)
matrix = np.array(matrix)

res_vec = []
for vec in matrix[1:]:
    res_vec.append(cosine(vec, matrix[0]))
    
answer = []
i = 0
while i <= 1:
    ind = res_vec.index(min(res_vec))
    answer.append(ind + 1)
    res_vec[ind] += 1
    i += 1
    
with open('answer1.txt', 'w') as answer1:
    answer1.write(f'{answer[0]} {answer[1]}')
