$(document).ready(function() {
    adaptive();

    // change the saying every 5 seconds
    $.get('/static/sayings.txt', function(data) {
        sayings = data.split("\n");
        // set interval before reload a new saying
        var now = 0; // current reading line
        setInterval(function() {
            $("#saying").html(sayings[now++%sayings.length]);
        }, 5000); // in ms.
    });

    // make the side bar expandable and collapsible
    $(".topnav-left>button:first-child").on("click", function() {
        var sidebarLeft = $("#sidebar").css('left');
        if (sidebarLeft == '0px') {
            $('#sidebar').css('position', 'fixed');
            $("#sidebar").css('left', '-250px');
            $("#mainContent").css('margin-left', '0px');
            $("#mainContent").css('width', '100%');
            $("#sidebar").css('box-shadow', 'none');
        } else {
            if ($(window).width() >= 700) {
                var mainContentWidth = $(window).width() - 250;
                $('#sidebar').css('position', 'fixed');
                $("#sidebar").css('left', '0px');
                $("#mainContent").css('margin-left', '250px');
                $("#mainContent").css('width', mainContentWidth);
            } else {
                $("#mainContent").css('margin-left', '0px');
                $("#mainContent").css('width', '100%');
                $('#sidebar').css('position', 'absolute');
                $("#sidebar").css('left', '0px');
                $("#sidebar").css('box-shadow', '4px 5px 5px #888888');
            }
        }
    });

    // make it suitable for small devices
    $(window).resize(function(){
        adaptive();
    });

});

function adaptive() {
    var sidebarLeft = $("#sidebar").css('left');
    if (sidebarLeft == '0px') {
        if ($(window).width() < 700) {
            $('#sidebar').css('position', 'fixed');
            $("#sidebar").css('left', '-250px');
            $("#mainContent").css('margin-left', '0px');
            $("#mainContent").css('width', '100%');
            $("#sidebar").css('box-shadow', 'none');
        }
    }
    if ($(window).width() < 625 ) {
        $("#saying").css('display','none');
    }else{
        $("#saying").css('display','');
    }
}