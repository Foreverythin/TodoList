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
                $("#sidebar").css('box-shadow', '0px 20px 40px 0px rgba(0,0,0,0.4)');
            }
        }
    });

    $("#day-night").on("click", function() {
        var root = $(':root');
        var nav_color = root.css('--color-primary');
        if (nav_color === '#D1E7EA') {
            root.css('--color-primary', '#000000');
            root.css('--color-nav-sayings-font', '#000000');
            root.css('--color-secondary', '#839AA8');
            root.css('--color-sidebar-line', '#FFF9D7');
        } else {
            root.css('--color-primary', '#D1E7EA');
            root.css('--color-nav-sayings-font', 'rgb(110, 131, 150)');
            root.css('--color-secondary', '#F7F7F7');
            root.css('--color-sidebar-line', '#E6E4E4');
        }
    });

    // make it suitable for small devices
    $(window).resize(function(){
        adaptive();
    });

    // make the sidebar item clicked to be highlighted
    $(".table-hover>tbody>tr").on("click", function() {
        // var trs = $(this).parent().find("tr");
        var trs = $(".table-hover>tbody>tr");
        if (trs.hasClass("on")) {
            trs.removeClass("on");
        }
        $(this).addClass("on");
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