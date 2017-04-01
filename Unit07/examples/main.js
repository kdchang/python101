var button = document.getElementById('abttuon');
var result = document.getElementById('result');

button.addEventListener('click', function() {
	var xhr = new XMLHttpRequest();
	var handleLoad = function() {
	  var htmlStr = '';
	  var data = JSON.parse(xhr.responseText);
	  data.forEach(function(value, index) {
	    htmlStr += '<div>Name: ' + value['Name'] + ' Variety: ' + value['Variety'] +  '<img class="thumbnail" src="' + value['ImageName'] + '"/></div>';
	  });
	  result.innerHTML = htmlStr;
	};

	xhr.open('GET', 'http://163.29.157.32:8080/dataset/6a3e862a-e1cb-4e44-b989-d35609559463/resource/f4a75ba9-7721-4363-884d-c3820b0b917c/download/393625397fc043188a3f8237c1da1c6f.json', true);
	xhr.send();
	xhr.onload = handleLoad;
});