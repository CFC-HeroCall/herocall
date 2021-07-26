function focused(element) {
    arrows = document.querySelectorAll("#clicked");
    for (let i=0; i < arrows.length; i++) {
        arrows[i].style = 'display: none;'
    }
    arrow = element.querySelector("#clicked");
    arrow.style = 'display:block;';
}

function select_tab(element) {
    selected = element.value
    console.log(selected)
    found = document.getElementById(selected)
    console.log(found)
    options = document.getElementsByClassName("option_tab");
    console.log(options)
    for (let i=0; i < options.length; i++) {
        options[i].style = 'display: none;'
    }
    found.style.display = 'block'
}