const $recipe = document.getElementById('recipe');
const $result = document.getElementById('result');

const typeHandler = function(e) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/");
  xhr.send(e.target.value);
  xhr.onreadystatechange = (e) => {
    res = xhr.responseText;
    res = res.replace(/(?:\r\n|\r|\n)/g, '<br>');
    $result.innerHTML = res;
  }
}

$recipe.addEventListener('input', typeHandler)
$recipe.addEventListener('propertychange', typeHandler)
