# Python 기본 함수 및 연산 정리

> 파이썬 기본 함수와 문법들을 정리하는 곳 입니다.

## 📅 작성일

2025년 2월 01일

## 📌 목차

1. **소개**
2. **함수**
3. **문법**
4. **참고 자료**

## 📝 소개

파이썬 기본 함수와 문법들의 설명과 예시를 작성합니다

## 함수

### 📌 [reverse()](https://velog.io/@jaesang98/Python-reverse) 순서뒤집기

### 📌 [sort()](https://velog.io/@jaesang98/Python-sort) 정렬하기

### 📌 [pop()](https://velog.io/@jaesang98/Python-pop) 제거하기

### 📌 [append()](https://velog.io/@jaesang98/Python-append) 추가하기

### 📌 [replace()](https://velog.io/@jaesang98/Python-replace) 교체하기

### 📌 [len()](https://velog.io/@jaesang98/Python-len) 길이구하기

### 📌 [swapcase()](https://velog.io/@jaesang98/Python-swapcase) 대소문자 반전

### 📌 [index()](https://velog.io/@jaesang98/Python-index) 인덱스 구하기

### 📌 [sum()](https://velog.io/@jaesang98/Python-sum) 합 구하기

### 📌 [map()](https://velog.io/@jaesang98/Python-map) 리스트 요소변환

### 📌 [max()](https://velog.io/@jaesang98/Python-max) 최대값

### 📌 [min()](https://velog.io/@jaesang98/Python-min) 최소값

### 📌 [list()](https://velog.io/@jaesang98/Python-list) 리스트로변환

### 📌 [eval()](https://velog.io/@jaesang98/Python-eval) 문자열을 계산


## 문법

#### n \*\* 0.5 (제곱근 구하기)

- **설명**: 숫자의 제곱근 계산

```python
144 ** 0.5  # 12.0
```

#### n // n (정수 나눗셈)

- **설명**: 정수 나눗셈(몫) 계산

```python
15 // 4  # 3
```

#### & 와 |

- **설명**:
  - `&` (AND 연산)
  - `|` (OR 연산)

```python
a, b = True, False
a & b, a and b  # False
a | b, a or b  # True
```

#### 문자열 포매팅 (f-string)

- **설명**: 문자열 내에서 변수 값을 쉽게 삽입

```python
a = 100
print(f"{a} is even")  # "100 is even"
```

#### 반복문 (슬라이싱)

- **설명**: 문자열 내에서 변수 값을 쉽게 삽입

```python
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(arr[::5]) # 출력: [0, 5, 10]
print(arr[::-1] ) # 출력: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```
