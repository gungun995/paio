from database import *
import matplotlib.pyplot as plt

count = page_info.select().count()
print(count)  # 输出记录总数
strings = []
ASIN = []
# transactions = page_info.select(page_info.rank).limit(1)
# output = [e for e in transactions.tuples()]
# print(output)


def jaccard_similarity(str1, str2):
    set1 = set(str1.lower().split())
    set2 = set(str2.lower().split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    return len(intersection) / len(union)

def calculate_similarity_matrix(strings):
    similarity_matrix = [[0] * len(strings) for _ in range(len(strings))]

    for i in range(len(strings)):
        for j in range(len(strings)):
            if i != j:
                similarity_matrix[i][j] = jaccard_similarity(strings[i], strings[j])

    return similarity_matrix

with db.cursor() as cursor:
    cursor.execute("SELECT * FROM page_info")
    for row in cursor:
        log1 =  row(0) #记录asin
        log2 = row[8]  #45
        if log2:
            ASIN.append(log1)
            strings.append(log2)

matrix = calculate_similarity_matrix(strings)
print(matrix)
plt.imshow(matrix)
plt.show()