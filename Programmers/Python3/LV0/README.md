# 기록

## 코테하다가 알게된것들

1. [제곱수 판별하기](https://school.programmers.co.kr/learn/courses/30/lessons/120909)

   - 문제점 : 제곱수를 도대체 어떻게 구해야 할 지 난해했음
   - 해결 : n\*\*0.5 이렇게 작성 시 제곱근을 구할 수 있는것을 알게됨

2. [최댓값 만들기(1)](https://school.programmers.co.kr/learn/courses/30/lessons/120847)

   - 문제점 : 리스트안에 최대값 하나는 구할 수 있지만 두번째 최대값은 어떻게 구해야할지 고민됬다
   - 해결 : 내가 생각한 방식은 최대값을 한번 구한 후 구한 값을 리스트에서 삭제하고 다시 최대값을 구하는 방식이었다
   - 다른해결 : sort()를 하여 -1 -2 인덱스를 통해 가져오는방법도 있다 (이게 좋아보임)

3. [피자 나눠 먹기 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120814)

   - 문제점 : 풀긴 했지만 if문을 너무 많이 썻다는 문제가 있었다
   - 해결 : return (n - 1) // 7 + 1 이렇게 return값을 주는 방법이 있는데 이 부분이 실제 프로젝트 때 사용하지 좋은 코드인지 모르겠다

4. [삼각형의 완성조건 (1)](https://school.programmers.co.kr/learn/courses/30/lessons/120889)

   - 문제점 : 코드 실행시 잘 되었지만 제출 후 체점하는 경우 오류가 있었고 그 이유를 전혀 알지 못하였다
   - 해결 : 틀렸던 예시문제는 중복된 값이 있는것이었고 sort를 통해 값을 구하면 되는 거였다

5. [홀짝 구분하기](https://school.programmers.co.kr/learn/courses/30/lessons/181944)

   - 문제점 : 숫자를 문자열로 바꾸어 출력하게 된 코드가 마음에 들지 않았음
   - 해결 : 문자열 포매팅방법을 사용했다

6. [짝수는 싫어요](https://school.programmers.co.kr/learn/courses/30/lessons/120813)

   - 문제점 : 항상 홀수만 or 짝수만 가져오는 문제를 %2==0으로 가져오는게 별루라고 생각했었음
   - 해결 : for문에서 (0, n, 2) 이런식으로 홀수번째만 가져올 수 있던게 신박했음

7. [옷가게 할인 받기](https://school.programmers.co.kr/learn/courses/30/lessons/120818)
   - 문제점 : 단순 할인 계산 문제였음
   - 해결 : 예를 들어 10% 할인이면 원래가격 - 원래가격*0.1 이었는데 사실 원래가격*0.9만 하면 되는거였음
