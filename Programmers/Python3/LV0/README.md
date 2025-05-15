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
