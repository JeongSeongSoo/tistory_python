user = {"name": "pddu", "birth": "0801", "job": "programmer"}
user["name"] # pddu
user.get("name") # pddu
user["age"] # KeyError: 'age'
user.get("age") # None

# 2022.12.14[프뚜]: 값 추가하기
user = {"name": "pddu", "birth": "0801", "job": "programmer"}
user["hobby"] = "coding" 
# {'name': 'pddu', 'birth': '0801', 'job': 'programmer', 'hobby': 'coding'}

# 2022.12.14[프뚜]: keys, values, items
user = {"name": "pddu", "birth": "0801", "job": "programmer"}
user.keys() # dict_keys(['name', 'birth', 'job'])
user.values() # dict_values(['pddu', '0801', 'programmer'])
user.items() # dict_items([('name', 'pddu'), ('birth', '0801'), ('job', 'programmer')])

# 2022.12.14[프뚜]: 초기화
user = {"name": "pddu", "birth": "0801", "job": "programmer"}
user.clear() # {}

# 2022.12.14[프뚜]: 값 여부 확인
user = {"name": "pddu", "birth": "0801", "job": "programmer"}
print("name" in user) # True
print("age" in user) # Faluse