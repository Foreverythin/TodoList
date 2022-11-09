function validateEmail(email) {
    var re = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    return re.test(email);
}

$(document).ready(function () {
    $("#login-submit").on("click", function () {
        var email = $("#email").val();
        var password = $("#password").val();
        if (!validateEmail(email)) {
            Toastify({
                text: "Please input a valid email address!",
                duration: 1200
            }).showToast();
            return;
        } else {
            $.ajax({
                url: "/user/login",
                type: "POST",
                data: {
                    email: email,
                    password: password
                },
                success: function (res) {
                    if (res['status'] === 400) {
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    } else {
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        setTimeout(function () {
                            window.location.href = "/today";
                        }, 1200);
                    }
                }
            });
        }
    });
});