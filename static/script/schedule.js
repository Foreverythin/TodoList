function renderCalendar() {
    var tasks;
    $.ajax({
        url: '/schedule/getTasks',
        type: 'GET',
        success: function (res) {
            tasks = JSON.parse(res);
            console.log(tasks);
            console.log(tasks[0].task_name);
            var allEvents = [];
            for (let i = 0; i < tasks.length; i++) {
                allEvents.push({
                    title: tasks[i].task_name,
                    start: tasks[i].date,
                    backgroundColor: tasks[i].color
                });
            }
            console.log(allEvents);

            var calendarEl = document.getElementById('calendar');
            var calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',
                events: allEvents
            });
            calendar.render();
        }
    })
}

$(document).ready(function () {
    renderCalendar();
})