// the function to validate the email address
function validateEmail(email) {
    var re = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    return re.test(email);
}

// the function to get the captcha
function getCaptcha() {
    var usermail = $("input[name='usermail']").val();  // get the email address
    if (!usermail) {  // if the email address is empty, show the tip information
        Toastify({
            text: "Please input your email address first!",
            duration: 1200
        }).showToast();
        return;
    } else {  // if the email address is not empty, send the request to the server
        if (!validateEmail(usermail)) {  // if the email address is invalid, show the tip information
            Toastify({
                text: "Please input a valid email address!",
                duration: 1200
            }).showToast();
            return;
        } else {
            $.ajax({
                url: '/user/captcha',
                type: 'POST',
                data: {
                    usermail: usermail
                },
                success: function (res) {
                    if (res['status'] === 200) {
                        // show the tip information
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        // resend the captcha after 60 seconds
                        var count = 60;
                        var timer = setInterval(function () {
                            if (count > 0) {
                                count--;
                                $('#captcha-btn').text(count + 's');
                            } else {
                                clearInterval(timer);
                                $('#captcha-btn').text('Get Captcha');
                            }
                        }, 1000);
                    } else {
                        // show the tip information
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    }
                }
            })
        }
    }
}

// the function which makes users sign up
function signup() {
    var usermail = $("input[name='usermail']").val();  // get the email address
    var password = $("input[name='password']").val(); // get the password
    var confirm = $("input[name='confirm']").val();  // get the confirmed password
    var captcha = $("input[name='captcha']").val();  // get the captcha
    if (!usermail || !password || !captcha || !confirm) {  // if the email address, password, captcha or confirmed password is empty, show the tip information
        Toastify({
            text: "Please fill in all the blanks!",
            duration: 1200
        }).showToast();
        return;
    } else {
        if (!validateEmail(usermail)) {  // if the email address is invalid, show the tip information
            Toastify({
                text: "Please input a valid email address!",
                duration: 1200
            }).showToast();
            return;
        } else if (password !== confirm) {  // if the password and confirmed password are not the same, show the tip information
            Toastify({
                text: "The passwords you input are not the same!",
                duration: 1200
            }).showToast();
            return;
        } else {
            $.ajax({
                url: '/user/signup',
                type: 'POST',
                data: {
                    usermail: usermail,
                    password: password,
                    captcha: captcha,
                    confirm: confirm
                },
                success: function (res) {
                    if (res['status'] === 200) {
                        // wait for 1 second and then redirect to the login page
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        setTimeout(function () {
                            window.location.href = '/user/login';
                        }, 1200);
                    } else {
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    }
                }
            })
        }
    }
}