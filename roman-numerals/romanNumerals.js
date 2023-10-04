// create an object of key value pairs to represent roman numerals
const romanNumeralToArabic = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

const romanNumeralPriority = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

function toRomanLazy(num) {
  let output = ""
  
  for (key of romanNumeralPriority) {
    console.log(Math.floor(num/romanNumeralToArabic[key]))
    // Math.floor(num/romanNumeralToArabic[key])
    // suntract that amount from num
  }
}

toRomanLazy(23)







function toRoman(num) {
  return "";
}

module.exports = { toRoman, toRomanLazy };
