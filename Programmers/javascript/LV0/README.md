# Javascript - LV0

> LV0 단계에서는 코딩 전 머리 예열 코딩테스트에 필요한 문법을 익힙니다.

## Math

```javascript
// Math.floor (소수점을 버린다)
const result = Math.floor(1.12112);
console.log(result); //1

// Math.ceil (소수점 있으면 올림)
const result = Math.ceil(1.12112);
console.log(result); //2

// Math.pow (제곱을 한다)
const result = Math.pow(2, 3);
console.log(result); //8
```

## Data Change

#### reduce

```javascript
// acc는 누적, cur은 현재값
const sum = [1, 2, 3, 4, 5].reduce((acc, cur) => acc + cur, 0);
console.log(sum); // 15
```

#### map

```javascript
const upper = ["banana", "apple", "grape"].map((item) => item.toUpperCase());
console.log(upper); // ["BANANA", "APPLE", "GRAPE"]
```

#### 스프레드

```javascript
const data = "bananaGood";
console.log([...data]); // ["b", "a", "n", "a", "n", "a", "G", "o", "o", "d"]
```

#### join

```javascript
const data = ["b", "a", "n", "a", "n", "a", "G", "o", "o", "d"];
console.log(data.join("")); // bananaGood
console.log(data.join("-")); // b-a-n-a-n-a-G-o-o-d
```

#### 비트연산을 통해 제곱

```javascript
console.log(2 << 3); // 8
```

#### repeat

```javascript
console.log("hi".repeat(3)); // hihihi
```

#### slice

```javascript
const arr = [10, 20, 30, 40, 50];
console.log(arr.slice(1, 3)); // [20, 30]

const str = "banana";
console.log(str.slice(1, 4)); // "ana"
```

---

## 코딩 꿀팁

#### 최대 최소

```javascript
// sort로 구하는 방법이 있다..!
function solution(numbers) {
  numbers.sort((a, b) => b - a);
  return numbers[0] * numbers[1];
}
```

#### 문자를 배열로

```javascript
// 스프레드
const data = "bananaGood";
console.log([...data]); // ["b", "a", "n", "a", "n", "a", "G", "o", "o", "d"]
```

#### 배열을 문자로

```javascript
// join
const data = ["b", "a", "n", "a", "n", "a", "G", "o", "o", "d"];
console.log(data.join("")); // bananaGood
console.log(data.join("-")); // b-a-n-a-n-a-G-o-o-d
```
