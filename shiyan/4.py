def jaccard_similarity(str1, str2):
    set1 = set(str1.lower().split())
    set2 = set(str2.lower().split())

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    return len(intersection) / len(union)
str1 = '#166,592 in Industrial & Scientific (See Top 100 in Industrial & Scientific)\n#258 in Commercial Floor Mats & Matting'
str2 = '#259,532 in Sports & Outdoors (See Top 100 in Sports & Outdoors)\n#14 in Boat Trailer Tires & Wheels'

similarity = jaccard_similarity(str1, str2)
print(similarity)