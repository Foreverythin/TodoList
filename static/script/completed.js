// sort the tasks, and go to the result page
function sortTask(sort_by) {
    window.location.href = "/completed/" + sort_by;
}

// when the page is loaded, the function will be executed
$(document).ready(function () {
    // the function will be executed when the user needs to complete a task.
    $(".completed.icon").on("click", function () {
        let taskID = this.attributes[0].value;  // get the task id
        $.ajax({
            url: "/all/uncompleteTask",
            type: "POST",
            data: {
                taskID: taskID
            },
            success: function (res) {
                if (res["status"] === 200) {
                    // show the tip information
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                    // refresh the page
                    setTimeout(function () {
                        window.location.reload();
                    }, 1200);
                } else {
                    // show the tip information
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                }
            }
        })
    });
});