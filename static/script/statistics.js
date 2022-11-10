$(document).ready(function () {
    var chartDom1 = document.getElementById('chart1');
    var chartDom2 = document.getElementById('chart2');
    var chartDom3 = document.getElementById('chart3');

    var numTasks = $("#numOfCompleted").text();
    var numCompleted = numTasks.split("/")[0];
    var numTotal = numTasks.split("/")[1];
    // convert to int
    numCompleted = parseInt(numCompleted);
    numTotal = parseInt(numTotal);
    var chart2_data;

    $.ajax({
        url: '/statistics/numTasksInEachModule',
        type: 'GET',
        success: function (res) {
            console.log(res);
            chart2_data = res;
            option2 = {
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    top: '5%',
                    left: 'center'
                },
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        avoidLabelOverlap: false,
                        label: {
                            show: false,
                            position: 'center'
                        },
                        emphasis: {
                            label: {
                                show: true,
                                fontSize: '40',
                                fontWeight: 'bold'
                            }
                        },
                        labelLine: {
                            show: false
                        },
                        data: res
                    }
                ]
            };

            option2 && myChart2.setOption(option2);
            $(window).resize(myChart2.resize);
        }
    })

    $.ajax({
        url: '/statistics/numCompletedEachDay',
        type: 'GET',
        success: function (res) {
            console.log(res);
        }
    })



    var myChart1 = echarts.init(chartDom1);
    var myChart2 = echarts.init(chartDom2);
    var myChart3 = echarts.init(chartDom3);
    var option1, option2, option3;

    option1 = {
        tooltip: {
            trigger: 'item'
        },
        legend: {
            top: '5%',
            left: 'center'
        },
        series: [
            {
                name: 'Access From',
                type: 'pie',
                radius: ['40%', '70%'],
                avoidLabelOverlap: false,
                label: {
                    show: false,
                    position: 'center'
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '40',
                        fontWeight: 'bold'
                    }
                },
                labelLine: {
                    show: false
                },
                data: [
                    {value: numCompleted, name: 'Completed Tasks'},
                    {value: numTotal, name: 'Total Tasks'}
                ]
            }
        ]
    };

    option3 = {
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                data: [150, 230, 224, 218, 135, 147, 260],
                type: 'line'
            }
        ]
    };

    option1 && myChart1.setOption(option1);
    option3 && myChart3.setOption(option3);
    $(window).resize(myChart1.resize);

    $(window).resize(myChart3.resize);
});
