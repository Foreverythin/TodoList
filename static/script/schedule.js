// the function to render the calendar through getting the data from the server
function renderCalendar() {
    var tasks;
    $.ajax({
        url: '/schedule/getTasks',
        type: 'GET',
        success: function (res) {
            tasks = JSON.parse(res);
            var allEvents = [];
            for (let i = 0; i < tasks.length; i++) {
                allEvents.push({
                    title: tasks[i].task_name,  // the title of the event
                    start: tasks[i].date,  // the time of the event
                    backgroundColor: tasks[i].color  // set the color of the event
                });
            }

            var calendarEl = document.getElementById('calendar');
            var calendar = new FullCalendar.Calendar(calendarEl, {
                initialView: 'dayGridMonth',  // set the initial view of the calendar
                events: allEvents  // set the events of the calendar
            });
            calendar.render();
        }
    })
}

// when the page is loaded, the function will be executed
$(document).ready(function () {
    renderCalendar();
})