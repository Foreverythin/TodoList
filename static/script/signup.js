$(document).ready(function() {

});

function validateEmail(email) {
    var re = /^[A-Za-z0-9\u4e00-\u9fa5]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/;
    return re.test(email);
}

function getCaptcha() {
    var usermail = $("input[name='usermail']").val();
    if (!usermail) {
        alert("Please input your email address first!");
        return;
    } else {
        if (!validateEmail(usermail)) {
            alert("Please input a valid email address!");
            return;
        } else {
            $.ajax({
                url: '/user/captcha',
                type: 'POST',
                data: {
                    usermail: usermail
                },
                success: function(res) {
                    if (res['status'] === 200) {
                        alert(res['msg']);
                        var count = 60;
                        var timer = setInterval(function() {
                            if (count > 0) {
                                count--;
                                $('#captcha-btn').text(count + 's');
                            } else {
                                clearInterval(timer);
                                $('#captcha-btn').text('Get Captcha');
                            }
                        }, 1000);
                    } else {
                        alert(res['msg']);
                    }
                }
            })
        }
    }
}

function signup() {
    var usermail = $("input[name='usermail']").val();
    var password = $("input[name='password']").val();
    var confirm = $("input[name='confirm']").val();
    var captcha = $("input[name='captcha']").val();
    if (!usermail || !password || !captcha || !confirm) {
        alert("Please fill in all the blanks!");
        return;
    } else {
        if (!validateEmail(usermail)) {
            alert("Please input a valid email address!");
            return;
        } else if (password !== confirm) {
            alert("The passwords you input are not the same!");
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
                success: function(res) {
                    if (res['status'] === 200) {
                        // wait for 1 second and then redirect to the login page
                        alert(res['msg']);
                        setTimeout(function() {
                            window.location.href = '/user/login';
                        }, 1000);
                    } else {
                        alert(res['msg']);
                    }
                }
            })
        }
    }
}