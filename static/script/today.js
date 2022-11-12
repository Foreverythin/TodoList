// sort the tasks, and go to the result page
function sortTask(sort_by) {
    window.location.href = "/today/" + sort_by;
}

// the function to make the page adaptive
function todayAdaptive() {
    if ($(window).width() < 800) {
        $(".date").css('display', 'none');
    } else {
        $(".date").css('display', '');
    }
    if ($(window).width() < 435) {
        $("#today-mainContent").css('width', '100%');
    } else {
        $("#today-mainContent").css('width', '75%');
    }
}

// when the page is loaded, the function will be executed
$(document).ready(function () {
    todayAdaptive();  // make the page adaptive
    $(window).resize(function () {
        todayAdaptive();
    });

    // after clicking the button, the function will be executed to make the input's value filled with the current module
    $(".modules").on('click', function () {
        let module = this.childNodes[0].innerText;
        $("#module-selected-editing-task").text(module);
    });

    // get today's date
    let now = new Date();
    let today = now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate();
    let day = now.getDay();
    let dayName = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    $("#today-date").text(today);
    $("#today-day").text("-" + dayName[day]);
})