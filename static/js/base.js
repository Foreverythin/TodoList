$(document).ready(function() {
    // change the saying every 5 seconds
    $.get('/static/sayings.txt', function(data) {
        sayings = data.split("\n");
        // set interval before reload a new saying
        var now = 0; // current reading line
        setInterval(function() {
            $("#saying").html(sayings[now++%sayings.length]);
        }, 5000); // in ms.
    });

    $(".topnav-left>button:first-child").on("click", function() {
        var sidebarLeft = $("#sidebar").css('left');
        if (sidebarLeft == '0px') {
            $("#sidebar").css('left', '-250px');
            $("#mainContent").css('margin-left', '0px');
            $("#mainContent").css('width', '100%');
        } else {
            $("#sidebar").css('left', '0px');
            $("#mainContent").css('margin-left', '250px');
            $("#mainContent").css('width', calc(100%-sidebarLeft));
        }
    });
});