function deleteTask() {
    $("#deleteTaskModel").modal("show");
}


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

$(document).ready(function () {
    todayAdaptive();
    $(window).resize(function () {
        todayAdaptive();
    });

    // get today's date
    let now = new Date();
    let today = now.getFullYear() + "-" + (now.getMonth() + 1) + "-" + now.getDate();
    let day = now.getDay();
    let dayName = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    $("#today-date").text(today);
    $("#today-day").text("-" + dayName[day]);

    $(".editTask-td").on("click", function () {
        $("#editTaskModel").modal("show");
        let previousTask = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].textContent;
        let previousTaskModuleName = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].attributes[0].value;
        let previousTaskModuleColor = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].attributes[1].value;
        let previousDescription = this.parentNode.parentNode.parentNode.parentNode.parentNode.children[1].innerText;
        $("#edit-task-title-placeholder-in-modal").val(previousTask);
        $("#edit-task-description-in-modal").val(previousDescription);
        $("#module-selected-editing-task").text(previousTaskModuleName);
    });

    var taskID;
    $(".deleteTask-td").on("click", function () {
        taskID = this.attributes[0].value;
        $("#deleteTaskModel").modal("show");
    });

    $("#delete_task_submit").on("click", function () {
        $.ajax({
            url: "/all/deleteTask",
            type: "POST",
            data: {
                taskID: taskID
            },
            success: function (res) {
                if (res["status"] === 200) {
                    alert(res["msg"]);
                    location.reload();
                } else {
                    alert(res["msg"]);
                }
            }
        });
    });
})