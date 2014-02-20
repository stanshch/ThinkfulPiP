var re = (/\w/);
var myArray = [];
var azWord = "";
var longWord = "";

function largestWord(str) {
    myArray = str.split(" ");
    for (var x = 0, i = myArray.length - 1; i >= x; x++) {
        word = myArray[x];
        azWord = "";
        for (var y = 0, j = word.length; j > y; y++) {
            if (re.test(word.charAt(y)) === true) {
                azWord = azWord + word.charAt(y);
            }
        }
        if (azWord.length > longWord.length) {
            longWord = azWord;
        }
    }
    return longWord;
}


var answer = largestWord("he my &name is tanya#### andwhois");

console.log(answer);


