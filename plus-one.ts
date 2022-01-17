// https://leetcode.com/problems/plus-one/

function plusOne(digits: number[]): number[] {
  digits.reverse();

  let carry = false;
  for(let i = 0; i < digits.length; ++i) {
    if(digits[i] === 9) {
      digits[i] = 0;
      carry = true;
    } else {
      digits[i]++;
      carry = false;
      break;
    }
  }

  if(carry) {
    digits.push(1);
  }

  digits.reverse();
  return digits;
};