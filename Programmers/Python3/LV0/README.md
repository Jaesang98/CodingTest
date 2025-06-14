# Python - LV0

> LV0 단계에서는 기본 문법과 함수들을 익히는 것을 목표로 합니다.

## 📝 문법

#### 삼항연산자

```python
# num1 == num2가 같으면 1 다르면 -1
def solution(num1, num2):
    return 1 if num1 == num2 else -1
```

#### 몫 구하기

```python
# 근본
a // b

# divmod
divmod(a,b)[0] #[0]이 몫, [1]이 나머지
```

#### 제곱수 판별별

```python
변수 = 64
print(변수 ** 0.5) # 8
print((변수 ** 0.5) ** 2) # 64
```

#### 슬라이싱

```python
리스트[시작:끝:간격]
```

### 배열 구하기

- `[표현식 for 변수 in 반복가능한_객체]`

```python
# 1차원배열
[a for a in range(3)] # [0,1,2]

# 2차원배열
[[a] for a in range(3)] # [[0], [1], [2]]
```

### 배열의 인덱스 교체하기기

```python
# 이렇게 하면 동시에 된다
my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
```

### 배열 독립적인 객체 참조 세팅

```python
# 이렇게 하면 독립적인 객체
answer = [[0] * n for _ in range(n)]

# 이렇게 하면 같은 객체를 공유
answer = [[0] * n] * n
```

```python
# 이렇게 하면 동시에 된다
my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
```

### 딕셔너리

```python
for i in strArr :
    answer_dict[len(i)] = answer_dict.get(len(i), 0) + 1

# keys()도 있음
print(max(answer_dict.values()))
```

## 📝 함수

#### 특정 문자열 바꾸기

```python
문자열 = 'abcdea'
문자열.replace('a' , '')
print(문자열) # bcde
```

#### 정렬

```python
# 문자열 정렬
문자열 = 'acbd'
print(''.join(sorted(문자열))) # abcd

# 배열 정렬
배열 = ['a','c','b']
배열.sort()
print(배열) # [a,b,c]
```

#### 리스트 합

```python
배열 = [1,2,3,4]
print(sum(배열)) #10
```

#### 리스트 길이

```python
배열 = [1,2,3,4]
문자열 = "1234"

print(len(배열)) #4
print(len(문자열)) #4
```

### 입력값 받기

```python
# 이건 깔아놓고 시작
import sys
input = sys.stdin.readline

n= map(int, input().split())
```

### 문자열 잘라서 배열로

```python
# 이건 깔아놓고 시작
a = "i    love  you"
print(a.split()) # ["i", "love", "you"]
```

### 반올림 내림

- `math.ceil` : 무조건 올림
- `math.floor` : 무조건 내림

```python
import math
math.ceil(3.4) # 4
math.floor(3.4) # 3
```

### 인덱스와 값

```python
리스트 = [10, 20, 30]

for i, v in enumerate(리스트):
    print(i, v) #0 10 / 1 20 / 2 30
```

### 숫자문자 구별

```python
"1".isdigit() # true
"1".isalpha() # false
```

### 대문자 소문자

```python
'a'.isupper()   # False
'b'.islower()   # True

"abc".upper()   # "ABC"
"ABC".lower()   # "abc"

"AbC".swapcase()  # "aBc"
"aBCdE".swapcase()  # "AbcDe"
```

### value와 index꺼내기

```python
arr = ["apple", "banana", "cherry"]

for i, fruit in enumerate(arr):
    print(i, fruit)

```

### 오른쪽 왼쪽 데이터

```python
arr = "0001100"
print(arr.lstrip("0")) # 1100

arr = "0001100"
print(arr.rstrip("0")) # 0011
```

### 절대값

```python
a = -2
print(abs(a)) # 2
```

### deque - rotate

```python
from collections import deque
numbers = deque(numbers)
numbers.rotate(1) # 오른쪽으로 한바퀴회전
numbers.rotate(-1) # 왼쪽으로 한바퀴회전
```

### find()

```python
s = "ababcab"

s.find("ab")   # 0
s.rfind("ab")  # 4
```

### startswith()

```python
s = "hello world"
print(s.startswith("hello"))  # True
print(s.startswith("world"))  # False
```

### 이진수

```python
binary = "1011"
num = int(binary, 2)

num = 11
binary = bin(num)[2:]
```

### eval

```python
data = "3 + 4"
print(eval(data)) # 7
```
