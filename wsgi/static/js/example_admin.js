/***************************************************************
*	Plot 5: Login users
***************************************************************/

$(function () {

    $(document).ready(function () {

        // Build the chart
        $('#plot5').highcharts({
            chart: {
                plotBackgroundColor: null,
                plotBorderWidth: null,
                plotShadow: false
            },
            title: {
                text: 'Cantidad de login en la aplicacion de cada grupo'
            },
            tooltip: {
                pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
            },
            plotOptions: {
                pie: {
                    allowPointSelect: true,
                    cursor: 'pointer',
                    dataLabels: {
                        enabled: false
                    },
                    showInLegend: true
                }
            },
            series: [{
                type: 'pie',
                name: 'Login',
                data: [
                    ['Grupo 1',   45.0],
                    ['Grupo 2',   26.8],
                    ['Admin',    11],
                    ['Ayudantes',  8.5],
                    ['Otros',   0.7]
                ]
            }]
        });
    });

});