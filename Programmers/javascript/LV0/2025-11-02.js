// 짝수의 합
// https://school.programmers.co.kr/learn/courses/30/lessons/120831?language=javascript
function solution(n) {
  let result = 0;
  for (var i = 0; i <= n; i++) {
    if (i % 2 === 0) {
      result += i;
    }
  }
  return result;
}

// 배열의 평균값
// https://school.programmers.co.kr/learn/courses/30/lessons/120817?language=javascript
function solution(n) {
  let result = 0;
  for (var i = 0; i <= n; i++) {
    if (i % 2 === 0) {
      result += i;
    }
  }
  return result;
}

// 배열 뒤집기
// https://school.programmers.co.kr/learn/courses/30/lessons/120821?language=javascript
function solution(num_list) {
  return num_list.reverse();
}

// 뒤집힌 문자열
// https://school.programmers.co.kr/learn/courses/30/lessons/120822?language=javascript
function solution(my_string) {
  var answer = "";
  my_string
    .split("")
    .reverse()
    .map((e) => {
      answer += e;
    });
  return answer;
}

// 편지
// https://school.programmers.co.kr/learn/courses/30/lessons/120898?language=javascript
function solution(message) {
  return message.length * 2;
}

// 피자 나눠 먹기 (1)
// https://school.programmers.co.kr/learn/courses/30/lessons/120814?language=javascript
function solution(n) {
  if (n <= 7) return 1;
  if (n % 7 === 0) return Math.floor(n / 7);
  else return Math.floor(n / 7) + 1;
}

// 세균 증식
// https://school.programmers.co.kr/learn/courses/30/lessons/120910?language=javascript
function solution(n, t) {
  return n << t;
}

// 최댓값 만들기(1)
// https://school.programmers.co.kr/learn/courses/30/lessons/120847?language=javascript
function solution(numbers) {
  numbers.sort((a, b) => b - a);
  return numbers[0] * numbers[1];
}

// 머쓱이보다 키 큰 사람
// https://school.programmers.co.kr/learn/courses/30/lessons/120585?language=javascript
function solution(array, height) {
  return array.filter((e) => e > height).length;
}

// 삼각형의 완성조건 (1)
// https://school.programmers.co.kr/learn/courses/30/lessons/120889?language=javascript
function solution(sides) {
  sides.sort(function (a, b) {
    return a - b;
  });
  return sides[2] < sides[0] + sides[1] ? 1 : 2;
}
