$(document).ready(function () {
    $(".completed.icon").on("click", function () {
        let taskID = this.attributes[0].value;
        $.ajax({
            url: "/all/uncompleteTask",
            type: "POST",
            data: {
                taskID: taskID
            },
            success: function (res) {
                if (res["status"] === 200) {
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                    setTimeout(function () {
                        window.location.reload();
                    }, 1200);
                } else {
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                }
            }
        })
    });
});