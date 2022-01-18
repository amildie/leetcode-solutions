// https://leetcode.com/problems/can-place-flowers/

function canPlaceFlowers(flowerbed: number[], n: number): boolean {
  let remaining = n;

  // edge cases
  if(remaining === 0) {
    return true;
  }
  if(flowerbed.length === 1) {
    return (flowerbed[0] === 0 && remaining <= 1) || (flowerbed[0] === 1 && remaining === 0);
  }  

  for(let i = 0; i < flowerbed.length; ++i) {
    if(i === 0) {
      if(flowerbed[i] === 0 && flowerbed[i+1] === 0) {
        flowerbed[i] = 1;
        remaining--;
      }
    }
    if(i > 0 && i < flowerbed.length-1) {
      if(flowerbed[i-1] === 0 && flowerbed[i] === 0 && flowerbed[i+1] === 0) {
        flowerbed[i] = 1;
        remaining--;
      }
    }
    if(i === flowerbed.length-1) {
      if(flowerbed[i-1] === 0 && flowerbed[i] === 0){
        flowerbed[i] = 1;
        remaining--;  
      } 
    }
  }
  
  return remaining <= 0;
};