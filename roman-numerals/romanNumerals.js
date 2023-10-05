// create an object of key value pairs to represent roman numerals
const romanNumeralToArabicLazy = {
  'I': 1,
  'V': 5,
  'X': 10,
  'L': 50,
  'C': 100,
  'D': 500,
  'M': 1000,
}

const romanNumeralPriorityLazy = ['M', 'D', 'C', 'L', 'X', 'V', 'I']

function toRomanLazy(num) {
  let output = ""
  
  for (key of romanNumeralPriorityLazy) {
    let multiple = Math.floor(num/romanNumeralToArabicLazy[key])
    for (i = multiple; i > 0; i--) {
      output += key
      num -= romanNumeralToArabicLazy[key]
    }
    // Math.floor(num/romanNumeralToArabic[key])
    // subtract that amount from num
  }
  return output
}




const romanNumeralToArabic = {
  'I': 1,
  'IV': 4,
  'V': 5,
  'IX': 9,
  'X': 10,
  'XL': 40,
  'L': 50,
  'C': 100,
  'CD': 400,
  'D': 500,
  'CM': 900,
  'M': 1000,
}

const romanNumeralPriority = ['M', 'CM', 'D', 'CD', 'C', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']


function toRoman(num) {
  let output = ""
  
  for (key of romanNumeralPriority) {
    let multiple = Math.floor(num/romanNumeralToArabic[key])

    for (i = multiple; i > 0; i--) {
      output += key
      num -= romanNumeralToArabic[key]
    }
  }
  return output
}

module.exports = { toRoman, toRomanLazy };
