# Python - LV0

> 코딩테스트의 문제들을 기록합니다.

## 📅 작성일

2025년 2월 01일

## 📝 개요

Programmers 를 Python이라는 언어를 통해 진행 중 새롭게 알게 되거나 유용했던 문제들을 기록합니다

### 1. [제곱수 판별하기](https://school.programmers.co.kr/learn/courses/30/lessons/120909)

- **문제점**  
  제곱수를 도대체 어떻게 구해야 할 지 난해했음
- **해결**  
  `n**0.5` 이렇게 작성 시 제곱근을 구할 수 있다는 것을 알게 됨

### 2. [최댓값 만들기(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120847)

- **문제점**  
  리스트 안에 최대값 하나는 구할 수 있지만 두 번째 최대값은 어떻게 구해야 할지 고민되었음
- **해결**  
  내가 생각한 방식은 최대값을 한번 구한 후, 구한 값을 리스트에서 삭제하고 다시 최대값을 구하는 방식이었다
  - **다른 해결**: `sort()`를 사용하여 -1, -2 인덱스를 통해 최대값 두 개를 가져오는 방법도 있음 (이게 더 효율적일 것 같음)

### 3. [피자 나눠 먹기 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120814)

- **문제점**  
  풀긴 했지만 `if`문을 너무 많이 썼다는 문제가 있었음
- **해결**  
  `return (n - 1) // 7 + 1` 이렇게 `return` 값을 주는 방법이 있음. 이 방식이 실제 프로젝트에 적합할지는 모르겠음

### 4. [삼각형의 완성조건 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120889)

- **문제점**  
  코드 실행시 잘 되었지만 제출 후 체점하는 경우 오류가 있었고, 그 이유를 전혀 알지 못했음
- **해결**  
  틀렸던 예시문제는 중복된 값이 있는 것이었고, `sort()`를 통해 값을 구하면 되는 거였음

### 5. [홀짝 구분하기](https://school.programmers.co.kr/learn/courses/30/lessons/181944)

- **문제점**  
  숫자를 문자열로 바꾸어 출력하게 된 코드가 마음에 들지 않았음
- **해결**  
  문자열 포매팅 방법을 사용하여 더 깔끔한 출력 방법을 적용했음

### 6. [짝수는 싫어요](https://school.programmers.co.kr/learn/courses/30/lessons/120813)

- **문제점**  
  항상 홀수만 또는 짝수만 가져오는 문제를 `%2==0`으로 가져오는 게 별로라고 생각했었음
- **해결**  
  `for`문에서 `(0, n, 2)` 형태로 홀수번째만 가져올 수 있다는 점이 신박했음

### 7. [옷가게 할인 받기](https://school.programmers.co.kr/learn/courses/30/lessons/120818)

- **문제점**  
  단순 할인 계산 문제였음
- **해결**  
  예를 들어 10% 할인이면 원래 가격에서 10%를 빼는 것이 아닌, `원래가격 * 0.9`로 계산하면 되는 것임

### 8. [숨어있는 숫자의 덧셈 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120851)

- **문제점**  
  for문을 쓸 때 나는 항상 `range(0,10)` 이런식으로 써왔었음
- **해결**  
  시작점이 0인 기본형태는 그냥 길이만 써도 됨 `range(10)`

### 9. [대문자와 소문자](https://school.programmers.co.kr/learn/courses/30/lessons/120893)

- **문제점**  
  알파벳 소문자 대문자 구분 해서 바꿔주는걸 일일이 썼었음
- **해결**  
  `swapcase()` 함수를 쓰면 되는거였다...

### 10. [인덱스 바꾸기](https://school.programmers.co.kr/learn/courses/30/lessons/120895)

- **문제점**  
  문자열의 인덱스 위치를 바꾸려고 조건문을 여러개 썻는데 더 좋은 방법이 없을까 고민되었다
- **해결**  
  그냥 문자열을 복사해서 변수에 저장한 다음 `A[0] = A[1]` 이렇게 하면되는거였는데 너무 돌아갔다

### 11. [문자열 바꿔서 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/181864)

- **문제점**  
  A를 B로 , B를 A로 바꿀 때 replace를 쓰면 간단할 줄 알았지만 하나를 바꾸는 순간 전부다 바뀌는 문제가 있어 일일이 바꾸는 작업을 함
- **해결**  
  `replace('A', 'C').replace('B', 'A').replace('C', 'B')` 형태로 처음에 A를 다른 문자열로 바꾸면 간편한거였다

### 12. [ad 제거하기](https://school.programmers.co.kr/learn/courses/30/lessons/181870)

- **문제점**  
  `if a in b`을 통해 a가 b 안에 있는지는 확인할 수 있지만, a가 b안에 없는지를 구하는걸 고민하였고 혹시 `not`이 되나? 했다
- **해결**  
  `not`된다..! 앵간히 할 수 있는건 다되는듯
