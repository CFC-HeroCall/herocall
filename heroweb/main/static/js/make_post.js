function add_tab(element) {
    var div = document.createElement("div")
    div.id = 'tab'
    document.getElementById('tabs').appendChild(div)

    var lab = document.createElement("label")
    lab.for = 'new_tab'
    lab.innerHTML = 'Title'
    var title = document.createElement("input")
    title.classList.add("mb-3")
    lab.classList.add("mt-3")
    title.id = 'new_tab'
    document.getElementById("tab").appendChild(lab)
    document.getElementById("tab").appendChild(document.createElement("br"))
    document.getElementById("tab").appendChild(title)
    console.log('works')
}