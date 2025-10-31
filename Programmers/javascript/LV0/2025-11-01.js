// 나머지 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120810?language=javascript
function solution(num1, num2) {
  return num1 % num2;
}

// 두 수의 차 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120803?language=javascript
function solution(num1, num2) {
  return num1 - num2;
}

// 숫자 비교하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120807?language=javascript
function solution(num1, num2) {
  return num1 === num2 ? 1 : -1;
}

// 나이 출력
// https://school.programmers.co.kr/learn/courses/30/lessons/120820?language=javascript
function solution(age) {
  return 2023 - age;
}

// 두 수의 나눗셈
// https://school.programmers.co.kr/learn/courses/30/lessons/120806?language=javascript
function solution(num1, num2) {
  return Math.floor((num1 / num2) * 1000);
}

// 몫 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120805?language=javascript
function solution(num1, num2) {
  return Math.floor(num1 / num2);
}

// 두 수의 곱 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120804?language=javascript
function solution(num1, num2) {
  return num1 * num2;
}

// 두 수의 합 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120802?language=javascript
function solution(num1, num2) {
  return num1 + num2;
}

// 각도기
// https://school.programmers.co.kr/learn/courses/30/lessons/120829?language=javascript
function solution(angle) {
  return validate(angle);
}

function validate(angle) {
  if (angle > 0 && angle < 90) {
    return 1;
  } else if (angle === 90) {
    return 2;
  } else if (angle > 90 && angle < 180) {
    return 3;
  } else {
    return 4;
  }
}

// 양꼬치
// https://school.programmers.co.kr/learn/courses/30/lessons/120830?language=javascript
function solution(n, k) {
  return n * 12000 + k * 2000 - Math.floor(n / 10) * 2000;
}
