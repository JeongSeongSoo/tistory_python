
list1 = [1, 2, 3]
list2 = list1

# 2022.12.14[프뚜]: 참조 주소 값이 같음
print(id(list1)) # 1560269851328(random)
print(id(list2)) # 1560269851328(random)

# 2022.12.14[프뚜]: 값 변경
list2[0] = 4
print(list1) # [4, 2, 3]
print(list2) # [4, 2, 3]


list1 = [1, 2, 3]
list2 = list1[:]

# 2022.12.14[프뚜]: 참조 주소 값이 다름
print(id(list1)) # 1560269851328(random)
print(id(list2)) # 1560269851328(random)

# 2022.12.14[프뚜]: 값 변경
list2[0] = 4
print(list1) # [1, 2, 3]
print(list2) # [4, 2, 3]


