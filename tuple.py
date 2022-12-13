
# 2022.12.13[프뚜]: 튜플 값은 변경할 수 없음
tuples = (1, 2, 3)
del tuples[0] # TypeError: 'tuple' object doesn't support item deletion
tuples[0] = 5 # TypeError: 'tuple' object does not support item assignment

# 2022.12.13[프뚜]: 인덱싱
tuples = (1, 2, 3)
tuples[0] # 1
tuples[0:2] # (1, 2)
tuples[:2] # (1, 2)

# 2022.12.13[프뚜]: 튜플 합치기
tuples1 = (1, 2, 3)
tuples2 = (4, 5)
tuples1 + tuples2 # (1, 2, 3, 4, 5)

# 2022.12.13[프뚜]: 튜플 반복 생성하기
tuples = (1, 2) * 2 # (1, 2, 1, 2)

# 2022.12.13[프뚜]: 튜플 길이(size)
tuples = (1, 2, 3)
len(tuples) # 3