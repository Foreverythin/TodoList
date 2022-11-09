// function deleteTask() {
//     $("#deleteTaskModel").modal("show");
// }
//
//
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

    // var taskID;
    // $(".deleteTask-td").on("click", function () {
    //     taskID = this.attributes[0].value;
    //     $("#deleteTaskModel").modal("show");
    // });
    //
    // $(".editTask-td").on("click", function () {
    //     let previousTask = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].textContent;
    //     let previousTaskModuleName = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].attributes[0].value;
    //     // let previousTaskModuleColor = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].attributes[1].value;
    //     let previousDescription = this.parentNode.parentNode.parentNode.parentNode.parentNode.children[1].innerText;
    //     let previousDueDate = this.parentNode.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[0].innerText.substring(5);
    //     $("#datepicker-editTask").val(previousDueDate);
    //     $("#edit-task-title-placeholder-in-modal").val(previousTask);
    //     $("#edit-task-description-in-modal").val(previousDescription);
    //     $("#module-selected-editing-task").text(previousTaskModuleName);
    //
    //     taskID = this.attributes[0].value;
    //     $("#editTaskModel").modal("show");
    // });
    //
    // $("#delete_task_submit").on("click", function () {
    //     $.ajax({
    //         url: "/all/deleteTask",
    //         type: "POST",
    //         data: {
    //             taskID: taskID
    //         },
    //         success: function (res) {
    //             if (res["status"] === 200) {
    //                 Toastify({
    //                     text: res['msg'],
    //                     duration: 1200
    //                 }).showToast();
    //                 setTimeout(function () {
    //                     window.location.reload();
    //                 }, 1200);
    //             } else {
    //                 Toastify({
    //                     text: res['msg'],
    //                     duration: 1200
    //                 }).showToast();
    //             }
    //         }
    //     });
    // });
    //
    // $("#edit_task_submit").on("click", function () {
    //     let fullDate = $("#datepicker-editTask").val();
    //     let moduleName = $("#module-selected-editing-task").text();
    //     let taskTitle = $("#edit-task-title-placeholder-in-modal").val();
    //     let taskDescription = $("#edit-task-description-in-modal").val();
    //     if (fullDate === "" || moduleName === "" || taskTitle === "") {
    //         Toastify({
    //             text: "Please fill in all the fields! (Description is optional)",
    //             duration: 1200
    //         }).showToast();
    //     } else if (taskTitle.length > 50) {
    //         Toastify({
    //             text: "The task title is too long",
    //             duration: 1200
    //         }).showToast();
    //     } else {
    //         let date = fullDate.split(" ")[0];
    //         let time = fullDate.split(" ")[1];
    //         $.ajax({
    //             url: "/all/editTask",
    //             type: "POST",
    //             data: {
    //                 'taskID': taskID,
    //                 'date': date,
    //                 'time': time,
    //                 'moduleName': moduleName,
    //                 'taskTitle': taskTitle,
    //                 'taskDescription': taskDescription
    //             },
    //             success: function (res) {
    //                 if (res["status"] === 200) {
    //                     Toastify({
    //                         text: res['msg'],
    //                         duration: 1200
    //                     }).showToast();
    //                     setTimeout(function () {
    //                         window.location.reload();
    //                     }, 1200);
    //                 } else {
    //                     Toastify({
    //                         text: res['msg'],
    //                         duration: 1200
    //                     }).showToast();
    //                 }
    //             }
    //         })
    //     }
    // });
    //
    // $(".uncompleted.icon").on("click", function () {
    //     let taskID = this.attributes[0].value;
    //     $.ajax({
    //         url: "/all/completeTask",
    //         type: "POST",
    //         data: {
    //             taskID: taskID
    //         },
    //         success: function (res) {
    //             if (res["status"] === 200) {
    //                 Toastify({
    //                     text: res['msg'],
    //                     duration: 1200
    //                 }).showToast();
    //                 setTimeout(function () {
    //                     window.location.reload();
    //                 }, 1200);
    //             } else {
    //                 Toastify({
    //                     text: res['msg'],
    //                     duration: 1200
    //                 }).showToast();
    //             }
    //         }
    //     });
    // });
})