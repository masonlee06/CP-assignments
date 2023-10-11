function linearSearch(searchTerm, arr) {
  // create a loop to iterate through the array
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === searchTerm) {
      return i
    }
    else{
      return undefined;
    }
  }
}

console.log(linearSearch(3, [1, 2, 3]))

function globalLinearSearch(searchTerm, arr) {
  return [];
}

module.exports = { linearSearch, globalLinearSearch };
