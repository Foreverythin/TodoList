$(document).ready(function() {
    adaptive();

    $("#datepicker").flatpickr({
        time: (new Date()).getTime()
    });

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
            root.css('--color-sidebar-line', '#839AA8');
            // root.css('--color-sidebar-clicked', '#99C4C8');
            $('#flatpickrDark')[0].setAttribute('href', '../static/style/flatpickr-dark.css');
        } else {
            root.css('--color-primary', '#D1E7EA');
            root.css('--color-nav-sayings-font', 'rgb(110, 131, 150)');
            root.css('--color-secondary', '#F7F7F7');
            root.css('--color-sidebar-line', '#E6E4E4');
            // root.css('--color-sidebar-clicked', '#EDEDED');
            $('#flatpickrDark')[0].href = '';
        }
    });

    // make it suitable for small devices
    $(window).resize(function(){
        adaptive();
    });

    // have some ids correct "on" when the page is updated
    var pageName = window.location.pathname.split('/')[1];
    if (pageName === 'module') {
        className = window.location.pathname.split('/')[2];
        $("#" + className).addClass("on");
    } else {
        $("#" + pageName).addClass("on");
    }

    // go to today page when clicking the home button
    $("#home").on("click", function() {
        $("#sidebar-top-table>tbody>tr:first-child").click();
    });

    // go to the page when clicking the sidebar module item
    $("#sidebar-bottom-table").each(function() {
        var trs = $(this).find("tr");
        trs.each(function() {
            $(this).on("click", function() {
                var className = $(this).attr("id");
                window.location.href = '/module/' + className;
                $(this).addClass("on");
            });
        });
    });

    // show the modal when clicking the sidebar class items
    var little_button_deletes = $('.little-button.delete');
    var little_button_edits = $('.little-button.edit');
    for (var i = 0; i < little_button_deletes.length; i++) {
        little_button_deletes[i].addEventListener('click', function (event) {
            event.stopPropagation();
            $('#little-button-delete').modal('show');
        })
    }
    for (var i = 0; i < little_button_edits.length; i++) {
        little_button_edits[i].addEventListener('click', function (event) {
            event.stopPropagation();
            $('#little-button-edit').modal('show');
        })
    }
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