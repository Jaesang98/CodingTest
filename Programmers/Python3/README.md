# Python 기본 함수 및 연산 정리

> 코딩테스트를 하면서 기록하는 곳 입니다

## 📅 작성일
2025년 2월 01일

---

## 📌 목차
1. **소개**
2. **2025-01-23**
3. **2025-01-24**
4. **2025-02-01**
7. **참고 자료**

---

## 📝 소개
코딩테스트 기록을 하는 곳 입니다!

---

## Python 기본 함수 및 연산 정리

### 📌 함수
#### reverse()
- **설명**: 리스트의 순서를 뒤집는다.
- **제한**: 문자열 ❌ 딕셔너리 ❌ 리스트 ✅

```python
nums = [1, 2, 3]
nums.reverse()  # [3, 2, 1]
```

#### pop()
- **설명**:
  - 리스트: 마지막 요소를 제거하고 반환
  - 딕셔너리: 특정 키를 제거하고 값을 반환
- **제한**: 문자열 ❌ 딕셔너리 ✅ 리스트 ✅

```python
# 리스트
nums = [10, 20, 30]
nums.pop()  # 30

# 딕셔너리
data = {"a": 1, "b": 2}
data.pop("b")  # 2
```

#### sort()
- **설명**: 기존의 리스트를 정렬
- **제한**: 문자열 ❌ 딕셔너리 ❌ 리스트 ✅

```python
nums = [3, 1, 2]
nums.sort()  # [1, 2, 3]
```

#### sorted()
- **설명**: 새로운 정렬된 리스트를 만든다
- **제한**: 문자열 ✅ 딕셔너리 ✅ 리스트 ✅

```python
# 리스트 정렬
nums = [3, 1, 2]
sorted_nums = sorted(nums)  # [1, 2, 3]

# 문자열 정렬
sorted_str = sorted("dcba")  # ['a', 'b', 'c', 'd']

# 딕셔너리 키 정렬
data = {"b": 2, "a": 1, "c": 3}
sorted_keys = sorted(data)  # ['a', 'b', 'c']
```

#### append()
- **설명**: 리스트에 요소를 추가
- **제한**: 문자열 ❌ 딕셔너리 ❌ 리스트 ✅

```python
nums = [1]
nums.append(2)  # [1, 2]
```

#### replace()
- **설명**: 문자열의 특정 값을 다른 값으로 교체
- **제한**: 문자열 ✅ 딕셔너리 ❌ 리스트 ❌

```python
text = "hello world"
text.replace("world", "Python")  # "hello Python"
```

#### len()
- **설명**: 문자열, 리스트, 딕셔너리의 길이를 반환
- **제한**: 문자열 ✅ 딕셔너리 ✅ 리스트 ✅

```python
len("hello")  # 5
len([1, 2, 3])  # 3
len({"a": 1, "b": 2})  # 2
```

### 📌 연산
#### n ** 0.5 (제곱근 구하기)
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

---

## 📚 참고 자료
- [프로그래머스](https://school.programmers.co.kr/learn/challenges?order=acceptance_asc&languages=python3&page=1&levels=0)
- [내 깃허브](https://github.com/Jaesang98/CodingTest)
