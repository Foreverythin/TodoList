$(document).ready(function () {
    var chartDom1 = document.getElementById('chart1');  // the first chart
    var chartDom2 = document.getElementById('chart2');  // the second chart
    var chartDom3 = document.getElementById('chart3');  // the third chart

    var numTasks = $("#numOfCompleted").text();  // the number of completed tasks
    var numCompleted = numTasks.split("/")[0];  // the number of completed tasks
    var numTotal = numTasks.split("/")[1];  // the number of total tasks
    // convert to int
    numCompleted = parseInt(numCompleted);
    var numUncompleted = parseInt(numTotal) - numCompleted;
    var chart2_data;

    var myChart1 = echarts.init(chartDom1);  // the first chart
    var myChart2 = echarts.init(chartDom2);  // the second chart
    var myChart3 = echarts.init(chartDom3);  // the third chart
    var option1, option2, option3;

    // the configuration of the first chart
    option1 = {
        title: {
            text: 'Task Completion Status',
            show: true,
            x: 'center',
            y: 'bottom',
            textStyle: {
                fontSize: 18,
            }
        },
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
                    {value: numUncompleted, name: 'Uncompleted Tasks'}
                ]
            }
        ]
    };

    option1 && myChart1.setOption(option1);  // set the configuration of the first chart
    $(window).resize(myChart1.resize);  // resize the first chart

    // get the data the second chart needs
    $.ajax({
        url: '/statistics/numTasksInEachModule',
        type: 'GET',
        success: function (res) {
            chart2_data = res;
            // the configuration of the second chart
            option2 = {
                title: {
                    text: 'Tasks in each module',
                    show: true,
                    x: 'center',
                    y: 'bottom',
                    textStyle: {
                        fontSize: 18,
                    }
                },
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

            option2 && myChart2.setOption(option2);  // set the configuration of the second chart
            $(window).resize(myChart2.resize);  // resize the second chart
        }
    })

    // get the data the third chart needs
    $.ajax({
        url: '/statistics/numCompletedEachDay',
        type: 'GET',
        success: function (res) {
            console.log(res);
            var dateArray = [];
            // get the date array
            for (let i = 0; i < res.length; i++) {
                dateArray.push(res[i].date);
            }
            var valueArray = [];
            // the number of tasks completed on each day
            for (let i = 0; i < res.length; i++) {
                valueArray.push(res[i].value);
            }

            // the configuration of the third chart
            option3 = {
                title: {
                    text: 'Daily completion',
                    show: true,
                    x: 'center',
                    y: 'bottom',
                    textStyle: {
                        fontSize: 18,
                    }
                },
                xAxis: {
                    type: 'category',
                    data: dateArray
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: valueArray,
                        type: 'line'
                    }
                ]
            };

            option3 && myChart3.setOption(option3);  // set the configuration of the third chart
            $(window).resize(myChart3.resize);  // resize the third chart
        }
    })
});
