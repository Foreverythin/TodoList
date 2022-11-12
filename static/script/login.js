// the function to validate email address
function validateEmail(email) {
    var re = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    return re.test(email);
}

// when the page is loaded, the function will be executed
$(document).ready(function () {
    // the function is executed when the user needs to log in
    $("#login-submit").on("click", function () {
        var email = $("#email").val();
        var password = $("#password").val();
        if (!validateEmail(email)) {  // if the email address is invalid, show the tip information
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
                        // show the tip information
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    } else {
                        // show the tip information
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        // refresh the page
                        setTimeout(function () {
                            window.location.href = "/today";
                        }, 1200);
                    }
                }
            });
        }
    });
});