from collections import Counter

b = ["a", "b", "c", "a", "c", "d", "b", "a", "c", "d"]

# 使用Counter统计字符串数量
count = Counter(b)
most_common = count.most_common(3)
print(most_common)
# [('a', 3), ('c', 3), ('b', 2)]

# print(count)
# Counter({'a': 3, 'c': 3, 'b': 2, 'd': 2})
