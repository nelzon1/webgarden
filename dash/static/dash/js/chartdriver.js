

var config = {
    type: 'line',
    data: {
      labels: [],
      datasets: [{
        label: 'Temperature',
        backgroundColor: window.chartColors.red,
        borderColor: window.chartColors.red,
        data: [],
        fill: false,
      }]
    },
    options: {
      responsive: true,
      title: {
        display: true,
        text: 'Chart.js Line Chart'
      },
      tooltips: {
        mode: 'index',
        intersect: false,
      },
      hover: {
        mode: 'nearest',
        intersect: true
      },
      scales: {
        xAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Time'
          }
        }],
        yAxes: [{
          display: true,
          scaleLabel: {
            display: true,
            labelString: 'Temperature (C)'
          }
        }]
      }
    }
  };

function updateData() {
	
	var tempData = JSON.parse(document.getElementById('temps').innerText);
	var temps = [];
	var times = [];
	tempData.data.forEach(function(row){
		temps.push(row.temp)
		times.push(row.time)
	})
	temps.reverse();
	times.reverse();
	config.data.datasets[0].data = temps;
	config.data.labels = times;
	

}
function getLatestImage() {
  var xmlhttp = new XMLHttpRequest();

  xmlhttp.onreadystatechange = function() {
      if (xmlhttp.readyState == XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
      if (xmlhttp.status == 200) {
    document.getElementById("latestImage").src = xmlhttp.responseURL;
      }
      else if (xmlhttp.status == 400) {
          alert('There was an error 400');
      }
      else {
          //alert('something else other than 200 was returned');
      }
      }
  };

  xmlhttp.open("GET", "/dash/getImage", true);
  xmlhttp.send();
};

function loadTempData() {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {   // XMLHttpRequest.DONE == 4
        if (xmlhttp.status == 200) {
			document.getElementById("temps").innerHTML = xmlhttp.responseText;
			updateData();
			window.myLine.update();
        }
        else if (xmlhttp.status == 400) {
            alert('There was an error 400');
        }
        else {
            //alert('something else other than 200 was returned');
        }
        }
    };

    xmlhttp.open("GET", "/dash/update", true);
    xmlhttp.send();
}


document.getElementById('buttonRefresh').addEventListener('click', function(){
	loadTempData();
  getLatestImage();
});

window.onload = function() {
	loadTempData();
  getLatestImage();
    var ctx = document.getElementById('canvas').getContext('2d');
	window.myLine = new Chart(ctx, config);
  };

setInterval(loadTempData, 60000);
setInterval(getLatestImage, 60000 * 5);