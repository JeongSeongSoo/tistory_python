
user = "my name is pddu"
user = "my name is 'pddu'"
user = "my name is \"pddu\""

user = 'my name is pddu'
user = 'my name is "pddu"'
user = 'my name is \'pddu\''

user = """my name is pddu"""
user = """my name is 'pddu'"""
user = """my "name" is pddu"""

user = '''my name is pddu'''
user = '''my name 'is' pddu'''
user = '''my "name" "is" pddu'''




user = "my name" + " is pddu"

user = "\npddu" * 2

user = "pddu"
len(user)

user = "pddu"
user[0] # 앞에서 index 시작
user[-1] # 뒤에서 index 시작
user[0:4] # n번부터 n번까지
user[2:] # n번부터 끝까지
user[:4] # 시작부터 n번까지

user = "my name is %s" % "pddu"
age = "how old are you? %d" % 20

user = "my name is {0}".format("pddu")
age = "how old are {0}? {1}".format("you", 20)

# 2022.12.13[프뚜]: d의 갯수 
user = "my name is pddu"
user.count("d")

# 2022.12.13[프뚜]: 원하는 문자 찾은 후 index
user = "my name is pddu"
user.find("name") # 3
user.find("ace") # -1

# 2022.12.13[프뚜]: 원하는 문자 찾은 후 index
user = "my name is pddu"
user.index("name") # 3
user.index("ace") # ValueError: substring not found

# 2022.12.13[프뚜]: 문자열 사이에 값 넣기
",".join("pddu")

# 2022.12.13[프뚜]: 소 -> 대문자
user = "pddu"
user.upper()

# 2022.12.13[프뚜]: 대 -> 소문자
user = "PDDU"
user.lower()

# 2022.12.13[프뚜]: 왼쪽 빈 값 제거
user = "  pddu"
user.lstrip()

# 2022.12.13[프뚜]: 오른쪽 빈 값 제거
user = "pddu  "
user.rstrip()

# 2022.12.13[프뚜]: 양쪽 빈 값 제거
user = "  pddu  "
user.strip()

# 2022.12.13[프뚜]: A -> B로 변경
user = "name"
user.replace("name", "pddu")

# 2022.12.13[프뚜]: 기준 값으로 나누기 -> 배열
user = "p:d:d:u"
user.split(":")