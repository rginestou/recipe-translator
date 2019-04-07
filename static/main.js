const $recipe = document.getElementById('recipe');
const $result = document.getElementById('result');

const typeHandler = function(e) {
  const xhr = new XMLHttpRequest();
  xhr.open("POST", "/");
  xhr.send(e.target.value);
  xhr.onreadystatechange = (e) => {
    data = xhr.responseText.split('\n');
    res = ""
    for (let d of data) {
      res += "<p class='text-grey-darker text-base mb-3'>\n"
      res += d
      res += "</p>\n"
    }
    $result.innerHTML = res;
  }
}

$recipe.addEventListener('input', typeHandler)
$recipe.addEventListener('propertychange', typeHandler)
