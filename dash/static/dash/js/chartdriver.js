

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

function loadTempData(config) {
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
    let URL = config.days ? '/dash/update?days=' + config.days : '/dash/update'
    xmlhttp.open('GET', URL, true);
    xmlhttp.send();
}


document.getElementById('buttonRefresh').addEventListener('click', function(){
	loadTempData({});
  getLatestImage();
  window.sessionStorage.days = 0;
});

document.getElementById('buttonRefresh24h').addEventListener('click', function(){
  let curDate = new Date();
  curDate.setDate(curDate.getDate() - 1);
	loadTempData({startDate : curDate,
                days: 1});
  getLatestImage();
  window.sessionStorage.days = 1;
});
document.getElementById('buttonRefresh2d').addEventListener('click', function(){
	let curDate = new Date();
  curDate.setDate(curDate.getDate() - 2);
	loadTempData({startDate : curDate,
                days: 2});
  getLatestImage();
  window.sessionStorage.days = 2;
});
document.getElementById('buttonRefresh7d').addEventListener('click', function(){
	let curDate = new Date();
  curDate.setDate(curDate.getDate() - 7);
	loadTempData({startDate : curDate,
                days: 7});
  getLatestImage();
  window.sessionStorage.days = 7;
});
document.getElementById('buttonRefreshAll').addEventListener('click', function(){
	let curDate = new Date();
  curDate.setDate(curDate.getDate() - 1);
	loadTempData({startDate : curDate,
                days: -1});
  getLatestImage();
  window.sessionStorage.days = -1;
});

window.onload = function() {
  window.sessionStorage.days = 0;
	loadTempData({days: window.sessionStorage.days});
  getLatestImage();
    var ctx = document.getElementById('canvas').getContext('2d');
	window.myLine = new Chart(ctx, config);
  };

function refreshData(){
  loadTempData({days: window.sessionStorage.days})
}

setInterval(refreshData, 60000);

setInterval(getLatestImage, 60000 * 5);