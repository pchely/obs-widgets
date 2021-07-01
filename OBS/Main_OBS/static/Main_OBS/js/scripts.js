function Widget(obj) {
  let name = document.getElementById(obj.id).innerText;
  // alert(name);
  let link = window.open('http://127.0.0.1:8000/widget/'+name, '_blank');
  link.onload = function () {
    global_value = link;
    console.log(global_value);
  }
}
