function factorial(num) {
  let ans = 1

  for (num; num > 0; num--) {
    ans = ans * num
  }
  return ans
}

module.exports = factorial;
