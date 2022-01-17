'''

    정규식 테스트

'''

import re

#================================
# 기본
#================================
# [] : 사이의 문자와 매치
# [a-zA-Z] : 알파벳 모두

# [0-9] :  숫자
# [^0-9] : not -> 숫자가 아닌 문자

# \d : = [0-9]
# \D : = [^0-9]

# \s : whitespace 문자와 매치, [ \t\n\r\f\v]와 동일한 표현식이다. 맨 앞의 빈 칸은 공백문자(space)를 의미
# \S : 반대

# \w : = [a-zA-Z0-9_] -> 문자+숫자
# \W : 반대

# . : \n을 제외한 모든 문자. 예)a.b = aab, a0b, abc(x)
#       a[.]b = 그냥 a.b

# * : 반복 예) ca*t = ct, cat, caaat
# + : 반복 예) ca*t = ct(x), cat, caaat ; 최소 한번 이상

# {} : 반복구간 예) ca{2}t = cat(x), caat(o)
# {m,n} : ca{2,5}t = cat(x), caat(o), caaaaat(o)

# ? : ab?c = abc(o), ac(o) ; 없거나 있거나

#================================
# match
#================================
print("===== match =====")
p = re.compile('[a-z]+')
m = p.match("python")
# m = re.match('[a-z]+', "python") 으로 한줄로도 가능
print(m)
# <re.Match object; span=(0, 6), match='python'>

print(m.group())    # python
print(m.start())    # 0
print(m.end())      # 6
print(m.span())     # (0, 6)

m = p.match("3 python")
print(m)
# None -> 처음 문자 3이 정규식에 부합하지 않으므로

#================================
# search
#================================
print("===== search =====")
m = p.search("python")
print(m)
# <re.Match object; span=(0, 6), match='python'>

m = p.search("3 python")
print(m)
# <re.Match object; span=(2, 8), match='python'>
print(m.group())    # python
print(m.start())    # 2
print(m.end())      # 8
print(m.span())     # (2, 8)

#================================
# findall, finditer
#================================
print("===== findall =====")
result = p.findall("life is too short")
print(result)
# ['life', 'is', 'too', 'short']

result = p.finditer("life is too short") # 반복가능한 객체 리턴
print(result)
# <callable_iterator object at 0x0000026B30349908>
for r in result: print(r)
#<re.Match object; span=(0, 4), match='life'>
#<re.Match object; span=(5, 7), match='is'>
#<re.Match object; span=(8, 11), match='too'>
#<re.Match object; span=(12, 17), match='short'>


#================================
# 메타문자
#================================
print("===== 메타문자 =====")
# | : OR
p = re.compile('Crow|Servo')    # crow 와 servo 사이에 공백 들어가면 안됨.
m = p.match('CrowHello')
print(m)
# <re.Match object; span=(0, 4), match='Crow'>

# ^ : 문자열의 맨 처음과 일치
print(re.search('^Life', 'Life is too short'))
# <re.Match object; span=(0, 4), match='Life'>
print(re.search('^Life', 'My Life'))
# None

# $ : 문자열의 끝
print(re.search('short$', 'Life is too short'))
# <re.Match object; span=(12, 17), match='short'>
print(re.search('short$', 'Life is too short, you need python'))
# None

# \b : 공백을 의미함
# p = re.compile(r'\bclass\b')
# print(p.search('no class at all'))
# # <re.Match object; span=(3, 8), match='class'>
# print(p.search('the declassified algorithm'))
# # None

# \B : 공백을 안포함. \b와 반대 의미
p = re.compile(r'\Bclass\B')
print(p.search('no class at all'))
# None
print(p.search('the declassified algorithm'))
# <re.Match object; span=(6, 11), match='class'>

#================================
# grouping
#================================
p = re.compile('(ABC)+') # () -> ABC 반복
m = p.search('ABCABCABC OK?')
print(m)
# <re.Match object; span=(0, 9), match='ABCABCABC'>
print(m.group())
# ABCABCABC

# group(0):전체 / group(1): 첫번째 그룹
# 이름만 -> 이름쪽에 ()
p = re.compile(r"(\w+)\s+\d+[-]\d+[-]\d+")
m = p.search("park 010-1234-1234")
print(m.group(1))
# park

# 전화번호만 -> 전화번호쪽에 괄호
p = re.compile(r"(\w+)\s+(\d+[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(2))
# 010-1234-1234

# 국번만 국번에 괄호
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group(3))
# 010

# 그루핑 문자열 재참조
p = re.compile(r'(\b\w+)\s+\1')
m = p.search('Paris in the the spring').group()
print(m)
# the the

# 그루핑된 문자열에 이름 붙이기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))
# park

p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)')
m = p.search('Paris in the the spring').group()
print(m)
# the the

#================================
# 전방탐색
#================================
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
# http:

p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())
# http

#================================
# 문자열바꾸기
#================================
p = re.compile('(blue|white|red)')
m = p.sub('colour', 'blue socks and red shoes')
print(m)
# colour socks and colour shoes

p = re.compile('(blue|white|red)')
m = p.subn( 'colour', 'blue socks and red shoes')
print(m)
# ('colour socks and colour shoes', 2)

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
# 010-1234-1234 park

p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))
# 010-1234-1234 park

# hexrepl 함수는 match 객체(위에서 숫자에 매치되는)를 입력으로 받아 16진수로 변환하여 돌려주는 함수이다.
# sub의 첫 번째 매개변수로 함수를 사용할 경우 해당 함수의 첫 번째 매개변수에는 정규식과 매치된 match 객체가 입력된다.
# 그리고 매치되는 문자열은 함수의 반환 값으로 바뀌게 된다
def hexrepl(match):
    value = int(match.group())
    return hex(value)

p = re.compile(r'\d+')
print(p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.'))
# Call 0xffd2 for printing, 0xc000 for user code.
