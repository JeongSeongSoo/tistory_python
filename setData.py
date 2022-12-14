# 2022.12.14[프뚜]: set data
data = set([1, 2, 3])
print(data) # {1, 2, 3}

data = set("pddu")
print(data) # {'p', 'u', 'd'}

# 2022.12.14[프뚜]: 인덱싱
array = list(data)
print(array) # ['p', 'u', 'd']

tuples = tuple(data)
print(tuples) # ('p', 'u', 'd')

# 2022.12.14[프뚜]: 값 추가
data = set([1, 2, 3])
data.add(4)
print(data) # {1, 2, 3, 4}

# 2022.12.14[프뚜]: 값 여러 개 추가
data = set([1, 2, 3])
data.update([4, 5])
print(data) # {1, 2, 3, 4, 5}

# 2022.12.14[프뚜]: 값 제거
data = set([1, 2, 3])
data.remove(3)
print(data) # {1, 2}

# 2022.12.14[프뚜]: 교집합
data1 = set([1, 2, 3])
data2 = set([2, 3, 4])
print(data1 & data2) # {2, 3}

data1 = set([1, 2, 3])
data2 = set([2, 3, 4])
print(data1.intersection(data2)) # {2, 3}
print(data2.intersection(data1)) # {2, 3}

# 2022.12.14[프뚜]: 합집합
data1 = set([1, 2, 3])
data2 = set([2, 3, 4])
print(data1 | data2) # {1, 2, 3, 4}

data1 = set([1, 2, 3])
data2 = set([2, 3, 4])
print(data1.union(data2)) # {1, 2, 3, 4}

# 2022.12.14[프뚜]: 차집합
data1 = set([1, 2, 3])
data2 = set([2, 3, 4])
print(data1 - data2) # {1}
print(data2 - data1) # {4}

data1 = set([1, 2, 3])
data2 = set([2, 3, 4])
print(data1.difference(data2)) # {1}
print(data2.difference(data1)) # {4}