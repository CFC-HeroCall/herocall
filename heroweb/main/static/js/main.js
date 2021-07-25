function focused(element) {
    arrows = document.querySelectorAll("#clicked");
    for (let i=0; i < arrows.length; i++) {
        arrows[i].style = 'display: none;'
    }
    arrow = element.querySelector("#clicked");
    arrow.style = 'display:block;';
}