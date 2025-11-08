// 배열 자르기
// https://school.programmers.co.kr/learn/courses/30/lessons/120833?language=javascript
function solution(numbers, num1, num2) {
  return numbers.slice(num1, num2 + 1);
}

// 피자 나눠 먹기 (3)
// https://school.programmers.co.kr/learn/courses/30/lessons/120816?language=javascript
function solution(numbers, num1, num2) {
  return numbers.slice(num1, num2 + 1);
}

// 점의 위치 구하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120841?language=javascript
function solution(dot) {
  if (dot[0] > 0 && dot[1] > 0) {
    return 1;
  } else if (dot[0] < 0 && dot[1] > 0) {
    return 2;
  } else if (dot[0] < 0 && dot[1] < 0) {
    return 3;
  } else {
    return 4;
  }
}

// 배열의 유사도
// https://school.programmers.co.kr/learn/courses/30/lessons/120903?language=javascript
function solution(s1, s2) {
  const result = s1.filter((e) => s2.includes(e));
  return result.length;
}

// 순서쌍의 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/120836?language=javascript
function solution(n) {
  var answer = 0;
  for (var i = 2; i <= n; i++) {
    if (n % i === 0) answer++;
  }
  return answer + 1;
}

// 배열 원소의 길이
// https://school.programmers.co.kr/learn/courses/30/lessons/120854?language=javascript
function solution(strlist) {
  var answer = [];
  strlist.forEach((e) => {
    answer.push(e.length);
  });
  return answer;
}

// 아이스 아메리카노
// https://school.programmers.co.kr/learn/courses/30/lessons/120819?language=javascript
function solution(money) {
  if (money < 5500) {
    return [0, money];
  } else {
    return [Math.floor(money / 5500), money % 5500];
  }
}

// 문자열안에 문자열
// https://school.programmers.co.kr/learn/courses/30/lessons/120908?language=javascript
function solution(str1, str2) {
  return str1.includes(str2) ? 1 : 2;
}

// 문자 반복 출력하기
// https://school.programmers.co.kr/learn/courses/30/lessons/120825?language=javascript
function solution(my_string, n) {
  var answer = "";
  for (var i = 0; i < my_string.length; i++) {
    for (var j = 0; j < n; j++) {
      answer += my_string[i];
    }
  }
  return answer;
}

// n의 배수 고르기
// https://school.programmers.co.kr/learn/courses/30/lessons/120905?language=javascript
function solution(n, numlist) {
  const result = numlist.filter((e) => {
    if (e % n === 0) {
      return e;
    }
  });
  return result;
}
