// let h1 = document.createElement("h1");
// let div = document.getElementById("root");
// let p = document.createElement('p');
// console.log(div)

// h1.textContent = "Hello World"
// p.textContent = "Hello"
// div.appendChild(h1);
// div.appendChild(p);
// console.log(h1)

function turnOn(color) {
    // Turn off all lights first
    document.getElementById("red").classList.remove("on");
    document.getElementById("yellow").classList.remove("on");
    document.getElementById("green").classList.remove("on");

    // Turn on the selected color
    document.getElementById(color).classList.add("on");
}

