function add_tab(element) {
    var iter = document.getElementsByClassName('tab_form').length;
    var tab = document.getElementById('tab')
    document.getElementById('indicator').value = parseInt(document.getElementById('indicator').value) + 1;

    if (tab.style.display == 'none') {
        tab.style.display = 'flex'
    } else {
        var cln = tab.cloneNode(true);
        cln.id = 'tab' + iter;
        cln.childNodes[9].value = '';
        cln.childNodes[9].name = 'tab_title' + iter;
        cln.childNodes[15].value = '';
        cln.childNodes[15].name = 'tab_text' + iter;
        document.getElementById("tabs").appendChild(cln)
    }
}

function delete_tab(element) {
    // document.getElementById('indicator').value = parseInt(document.getElementById('indicator').value) - 1;
    // var iter = document.getElementsByClassName('tab_form').length;
    // if (iter == 1) {
    //     tab.style.display = 'none'
    // } else {
    //     element.parentElement.parentElement.parentElement.remove()
    // }
}

function test(element) {
    selected = element.value
    found = document.getElementById(selected)
    options = document.getElementsByClassName("option_tab");
    console.log(options)
    for (let i=0; i < options.length; i++) {
        options[i].style = 'display: none;'
    }
    found.style.display = 'block'
}