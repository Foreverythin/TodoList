$(document).ready(function () {
    var chartDom1 = document.getElementById('chart1');
    var chartDom2 = document.getElementById('chart2');
    var chartDom3 = document.getElementById('chart3');
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
                    {value: 1048, name: 'Search Engine'},
                    {value: 735, name: 'Direct'}
                ]
            }
        ]
    };
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
                data: [
                    {value: 1048, name: 'Search Engine'},
                    {value: 735, name: 'Direct'},
                    {value: 580, name: 'Email'},
                    {value: 484, name: 'Union Ads'},
                    {value: 300, name: 'Video Ads'}
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
    option2 && myChart2.setOption(option2);
    option3 && myChart3.setOption(option3);
    $(window).resize(myChart1.resize);
    $(window).resize(myChart2.resize);
    $(window).resize(myChart3.resize);
});
