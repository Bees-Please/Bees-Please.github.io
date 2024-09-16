var flickert = document.getElementById("flicker");
const symbols = ["?", "░", " "];
Math.floor(Math.random() * 2);
setTimeout(silly, getRandomIntInclusive(250, 1000));
function silly() {
    doSwap = getRandomInt(11); // if the text should swap
    symbol = symbols[getRandomInt(symbols.length)]// which symbol
    pos = getRandomInt(3)// what position

    if (doSwap > 5) {
        console.log(symbol)
        flickert.InnerHTML = "a";
    }
    else {
        console.log('ahoy!');
    }

    setTimeout(silly, getRandomIntInclusive(250, 1000));
}


function getRandomIntInclusive(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled + 1) + minCeiled);
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}