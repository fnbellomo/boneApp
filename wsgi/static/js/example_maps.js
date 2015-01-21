/***********************************
    1 plot: heat map
 **********************************/

$(function () {

    $(document).ready(function() {

	$.get('/static/data/heat_map_data.csv', function(csv){

	    $('#map3').highcharts({

		data: {
		    csv: csv
		},

		chart: {
		    type: 'heatmap',
		    inverted: true
		},


		title: {
		    text: 'Highcharts heat map study',
		    align: 'left'
		},

		subtitle: {
		    text: 'Temperature variation by day and hour through April 2013',
		    align: 'left'
		},

		xAxis: {
		    tickPixelInterval: 50,
		    min: Date.UTC(2013, 3, 1),
		    max: Date.UTC(2013, 3, 30)
		},

		yAxis: {
		    title: {
			text: null
		    },
		    labels: {
			format: '{value}:00'
		    },
		    minPadding: 0,
		    maxPadding: 0,
		    startOnTick: false,
		    endOnTick: false,
		    tickPositions: [0, 6, 12, 18, 24],
		    tickWidth: 1,
		    min: 0,
		    max: 23
		},

		colorAxis: {
		    stops: [
			[0, '#3060cf'],
			[0.5, '#fffbbc'],
			[0.9, '#c4463a']
		    ],
		    min: -5
		},

		series: [{
		    borderWidth: 0,
		    colsize: 24 * 36e5, // one day
		    tooltip: {
			headerFormat: 'Temperature<br/>',
			pointFormat: '{point.x:%e %b, %Y} {point.y}:00: <b>{point.value} ℃</b>'
		    }
		}]

	    });
	});

    });
});

/***********************************
    2 plot: density of each state
 **********************************/
$(function () {

    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=us-population-density.json&callback=?', function (data) {

        // Make codes uppercase to match the map data
        $.each(data, function () {
            this.code = this.code.toUpperCase();
        });

        // Instanciate the map
        $('#map2').highcharts('Map', {

            chart : {
                borderWidth : 1
            },

            title : {
                text : 'US population density (/km²)'
            },

            legend: {
                layout: 'horizontal',
                borderWidth: 0,
                backgroundColor: 'rgba(255,255,255,0.85)',
                floating: true,
                verticalAlign: 'top',
                y: 25
            },

            mapNavigation: {
                enabled: true
            },

            colorAxis: {
                min: 1,
                type: 'logarithmic',
                minColor: '#EEEEFF',
                maxColor: '#000022',
                stops: [
                    [0, '#EFEFFF'],
                    [0.67, '#4444FF'],
                    [1, '#000022']
                ]
            },

            series : [{
                animation: {
                    duration: 1000
                },
                data : data,
                mapData: Highcharts.maps['countries/us/us-all'],
                joinBy: ['postal-code', 'code'],
                dataLabels: {
                    enabled: true,
                    color: 'white',
                    format: '{point.code}'
                },
                name: 'Population density',
                tooltip: {
                    pointFormat: '{point.code}: {point.value}/km²'
                }
            }]
        });
    });
});

/***********************************
    3 plot 
 **********************************/
$(function () {

    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=world-population.json&callback=?', function (data2) {

        var mapData = Highcharts.geojson(Highcharts.maps['custom/world']);

        // Correct UK to GB in data
        $.each(data2, function () {
            if (this.code === 'UK') {
                this.code = 'GB';
            }
        });

        $('#map1').highcharts('Map', {
            chart : {
                borderWidth : 1
            },

            title: {
                text: 'World population 2010 by country'
            },

            subtitle : {
                text : 'Demo of Highcharts map with bubbles'
            },

            legend: {
                enabled: false
            },

            mapNavigation: {
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'bottom'
                }
            },

            series : [{
                name: 'Countries',
                mapData: mapData,
                color: '#E0E0E0',
                enableMouseTracking: false
            }, {
                type: 'mapbubble',
                mapData: mapData,
                name: 'Population 2010',
                joinBy: ['iso-a2', 'code'],
                data: data2,
                minSize: 4,
                maxSize: '12%',
                tooltip: {
                    pointFormat: '{point.code}: {point.z} thousands'
                }
            }]
        });

    });
});