function Open_Widget() {
  let name = document.getElementById("list_select").value;
  let link = window.open('http://127.0.0.1:8000/widget/'+name, '_blank');
};


function Show_Hide_Widget() {
    let name = document.getElementById('list_select').value;
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "http://127.0.0.1:8000/edit_status/"+name);
    xhr.send();
  };


function Delete() {
  let name = document.getElementById("list_select").value;
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "http://127.0.0.1:8000/delete/"+name);
  xhr.send();
  parent.location.reload();
};


function Show_Info(obj) {
  let name = obj.innerText;
  let xhr = new XMLHttpRequest();
  xhr.open("GET", "http://127.0.0.1:8000/about_widget/"+name);
  xhr.responseType = 'json';
  xhr.send();
  xhr.onload = function () {
    console.log("Widget:", name);
    console.log("Title:", xhr.response.title);
    console.log("Subtitle:", xhr.response.subtitle)
  }
};
