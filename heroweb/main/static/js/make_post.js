function add_tab(element) {
    var iter = document.getElementsByClassName('tab_form').length;
    var tab = document.getElementById('tab')
    document.getElementById('indicator').value = parseInt(document.getElementById('indicator').value) + 1;

    if (tab.style.display == 'none') {
        tab.style.display = 'block'
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