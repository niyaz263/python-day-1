greenlyt = document.getElementById("green");
orangelyt = document.getElementById("orange");
redlyt = document.getElementById("red");

function green(){
    greenlyt.classList.add("green");
    orangelyt.classList.add("orange");
    redlyt.classList.add("red");
}

function orange(){
    orangelyt.classList.add("orange");
    greenlyt.classList.remove("green");
    redlyt.classList.remove("red");
}
function red(){
    orangelyt.classList.remove("orange");
    greenlyt.classList.remove("green");
    redlyt.classList.add("red");
}
function green(){
    greenlyt.classList.add("green");
    orangelyt.classList.remove("orange");
    redlyt.classList.remove("red");
}