// https://school.programmers.co.kr/learn/courses/30/lessons/120833
function solution(numbers, num1, num2) {
  return numbers.slice(num1, num2 + 1);
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120829
function solution(angle) {
  if (angle > 0 && angle < 90) {
    return 1;
  }
  if (angle === 90) {
    return 2;
  }
  if (angle > 90 && angle < 180) {
    return 3;
  }
  if (angle === 180) {
    return 4;
  }
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120831
function solution(n) {
  var answer = 0;

  for (var i = 0; i < n + 1; i++) {
    if (i % 2 === 0) {
      answer += i;
    }
  }

  return answer;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120821
function solution(num_list) {
  return num_list.reverse();
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120822
function solution(my_string) {
  return [...my_string].reverse().join("");
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120889
function solution(sides) {
  var answer = sides.sort(function (a, b) {
    return a - b;
  });
  return answer[2] >= answer[0] + answer[1] ? 2 : 1;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120585
function solution(array, height) {
  return array.filter((e) => e > height).length;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120847
function solution(numbers) {
  const result = numbers.sort((a, b) => b - a);
  return result[0] * result[1];
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120910
function solution(n, t) {
  return n << t;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120830
function solution(n, k) {
  return n * 12000 + k * 2000 - Math.floor(n / 10) * 2000;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120817
function solution(numbers) {
  var result = 0;

  for (var i = 0; i < numbers.length; i++) {
    result += numbers[i];
  }
  return result / numbers.length;
}

// https://school.programmers.co.kr/learn/courses/30/lessons/120814
function solution(n) {
  if (n <= 7) return 1;
  if (n % 7 === 0) return Math.floor(n / 7);
  else return Math.floor(n / 7) + 1;
}
