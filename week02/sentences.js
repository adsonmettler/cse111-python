// Author: Adson Mettler do Nascimento

// ---- Program: Turing Test -----

// Description: Basically this program gets randomly pieces of a sentence from a datatable
// and, by using functions, the program returns a sentence. It is a sentence generator.



function main() {
    let sentence_a = make_sentence(1, "past")
    console.log(`${sentence_a}.`)

}


function get_determiner(quantity) {
    let words;
    if (quantity === 1) {
        words = ["a", "one", "the"];
    }
    else {
        words = ["some", "many", "the"]
    }
        
    let word = words[Math.floor(Math.random() * words.length)];
    return word;
}

