// 제곱수 판별하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120909?language=javascript
function solution(n) {
  return Number.isInteger(Math.sqrt(n)) ? 1 : 2;
}

// 특정 문자 제거하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120826?language=javascript
function solution(my_string, letter) {
  return my_string.split(letter).join("");
}

// 모음 제거
// https://school.programmers.co.kr/learn/courses/30/lessons/120849?language=javascript
function solution(my_string) {
  var vowel = ["a", "e", "i", "o", "u"];
  var answer = [...my_string].filter((e) => {
    return vowel.includes(e) === false;
  });

  return answer.join("");
}

// 짝수 홀수 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/120824?language=javascript
function solution(num_list) {
  var answer = [0, 0];

  num_list.forEach((e) => {
    if (e % 2 === 0) {
      answer[0] += 1;
    } else {
      answer[1] += 1;
    }
  });

  return answer;
}

// 자릿수 더하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120906?language=javascript
function solution(n) {
  const result = [...n.toString()];
  return result.reduce((a, b) => Number(a) + Number(b), 0);
}

// n의 배수
// https://school.programmers.co.kr/learn/courses/30/lessons/181937?language=javascript
function solution(num, n) {
  return num % n === 0 ? 1 : 0;
}

// 문자 리스트를 문자열로 변환하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181941?language=javascript
function solution(arr) {
  return arr.join("");
}

// 공배수
// https://school.programmers.co.kr/learn/courses/30/lessons/181936?language=javascript
function solution(number, n, m) {
  return number % n === 0 && number % m === 0 ? 1 : 0;
}

// 문자열 붙여서 출력하기
// https://school.programmers.co.kr/learn/courses/30/lessons/181946?language=javascript
const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", function (line) {
  input = line.split(" ");
}).on("close", function () {
  str1 = input[0];
  str2 = input[1];

  console.log(str1 + str2);
});

// n 번째 원소부터
// https://school.programmers.co.kr/learn/courses/30/lessons/181892?language=javascript
function solution(num_list, n) {
  var answer = num_list.filter((e, i) => {
    return i >= n - 1;
  });
  return answer;
}
