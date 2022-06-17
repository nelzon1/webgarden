const drawBackgroundColor = {
    id: 'custom_canvas_background_color',
    beforeDraw: (chart) => {
        const ctx = chart.canvas.getContext('2d');
        ctx.save();
        ctx.globalCompositeOperation = 'destination-over';
        ctx.fillStyle = 'lightGreen';
        ctx.fillRect(0, 0, chart.width, chart.height);
        ctx.restore();
    }
};

var config = {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Temperature',
            backgroundColor: 'rgb(0, 0, 0)',
            borderColor: 'rgb(0, 0, 0)',
            pointRadius: 1,
            fill: {
                target: { value: 24.5 },
                above: window.chartColors.orange, // Area will be red above the origin
                below: window.chartColors.blue // And blue below the origin
            }
        }]
    },
    //plugins: [drawBackgroundColor],
    options: {
        responsive: true,
        plugins: {
            title: {
                display: true,
                text: 'Grow Chamber Temperature',
                color: 'black'
            },
            legend: {
                display: false
            }
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
            x: {
                title: {
                    display: true,
                    text: 'Time',
                    color: 'black'
                },
                grid: {
                    color: 'black'
                },
                ticks: {
                    color: 'black'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Temperature (C)',
                    color: 'black'
                },
                grid: {
                    color: 'black'
                },
                ticks: {
                    color: 'black'
                }
            }
        }
    }
};

function getMaxTemp(temperatures) {
    let curMax = 0;
    temperatures.forEach(temp => {
        if (Number(temp) > curMax) {
            curMax = Number(temp);
        }
    });
    return curMax;
}

function updateData() {

    var tempData = JSON.parse(document.getElementById('temps').innerText);
    var temps = [];
    var times = [];
    tempData.data.forEach(function(row) {
        temps.push(Number(row.temp))
        times.push(row.time)
    })
    temps.reverse();
    times.reverse();
    config.data.datasets[0].data = temps;
    config.data.labels = times;
    window.sessionStorage.curTemp = Number(temps.slice(-1)[0]).toFixed(2);
    window.sessionStorage.avgTemp = Number(temps.reduce((a, b) => a + b, 0) / temps.length).toFixed(2);
    window.sessionStorage.maxTemp = getMaxTemp(temps).toFixed(2);

}

function getLatestImage() {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) { // XMLHttpRequest.DONE == 4
            if (xmlhttp.status == 200) {
                document.getElementById("latestImage").src = xmlhttp.responseURL;
            } else if (xmlhttp.status == 400) {
                alert('There was an error 400');
            } else {
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
        if (xmlhttp.readyState == XMLHttpRequest.DONE) { // XMLHttpRequest.DONE == 4
            if (xmlhttp.status == 200) {
                document.getElementById("temps").innerHTML = xmlhttp.responseText;
                updateData();
                document.getElementById("curTemp").innerHTML = window.sessionStorage.curTemp + "&deg";
                document.getElementById("avgTemp").innerHTML = window.sessionStorage.avgTemp + "&deg";
                document.getElementById("maxTemp").innerHTML = window.sessionStorage.maxTemp + "&deg";
                window.myLine.update();
            } else if (xmlhttp.status == 400) {
                alert('There was an error 400');
            } else {
                //alert('something else other than 200 was returned');
            }
        }
    };
    let URL = config.days ? '/dash/update?days=' + config.days : '/dash/update'
    xmlhttp.open('GET', URL, true);
    xmlhttp.send();
}


document.getElementById('buttonRefresh').addEventListener('click', function() {
    loadTempData({});
    getLatestImage();
    window.sessionStorage.days = 0;
});

document.getElementById('buttonRefresh24h').addEventListener('click', function() {
    let curDate = new Date();
    curDate.setDate(curDate.getDate() - 1);
    loadTempData({
        startDate: curDate,
        days: 1
    });
    getLatestImage();
    window.sessionStorage.days = 1;
});
document.getElementById('buttonRefresh2d').addEventListener('click', function() {
    let curDate = new Date();
    curDate.setDate(curDate.getDate() - 2);
    loadTempData({
        startDate: curDate,
        days: 2
    });
    getLatestImage();
    window.sessionStorage.days = 2;
});
document.getElementById('buttonRefresh7d').addEventListener('click', function() {
    let curDate = new Date();
    curDate.setDate(curDate.getDate() - 7);
    loadTempData({
        startDate: curDate,
        days: 7
    });
    getLatestImage();
    window.sessionStorage.days = 7;
});
document.getElementById('buttonRefreshAll').addEventListener('click', function() {
    let curDate = new Date();
    curDate.setDate(curDate.getDate() - 1);
    loadTempData({
        startDate: curDate,
        days: -1
    });
    getLatestImage();
    window.sessionStorage.days = -1;
});

function fetchImage() {
    let oldSelected = document.querySelector('.imageList .active');
    if (oldSelected && !!oldSelected) {
        oldSelected.classList.remove('active');
    }
    this.classList.add('active');
    filename = this.innerText
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) { // XMLHttpRequest.DONE == 4
            if (xmlhttp.status == 200) {
                document.getElementById("latestImage").src = xmlhttp.responseURL;
            } else if (xmlhttp.status == 400) {
                alert('There was an error 400');
            } else {
                //alert('something else other than 200 was returned');
            }
        }
    };
    if (filename === 'Quality Image') {
        filename = 'quality'
    }
    xmlhttp.open("GET", "/dash/fetchImage/" + filename, true);
    xmlhttp.send();
}




function initialize() {
    window.sessionStorage.curTemp = 0;
    window.sessionStorage.avgTemp = 0;
    window.sessionStorage.maxTemp = 0;
    document.querySelectorAll('.imageList li')
        .forEach(e => e.addEventListener("click", fetchImage));
    document.querySelector('.imageList :nth-child(2)').classList.add('active');
};

window.onload = function() {
    window.sessionStorage.days = 0;
    loadTempData({ days: window.sessionStorage.days });
    getLatestImage();
    var ctx = document.getElementById('canvas').getContext('2d');
    window.myLine = new Chart(ctx, config);
    initialize();
};

function refreshData() {
    loadTempData({ days: window.sessionStorage.days })
}

setInterval(refreshData, 60000);

setInterval(getLatestImage, 60000 * 5);