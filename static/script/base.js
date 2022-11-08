$(document).ready(function () {
    adaptive();
    var moduleID_need_to_be_changed;

    var dayMode = localStorage.getItem('dayMode');

    // whether the dayMode is null
    if (dayMode == null) {
        localStorage.setItem('dayMode', 'light');
    }

    var root = $(':root');
    if (dayMode === 'light') {
        root.css('--color-primary', '#D1E7EA');
        root.css('--color-nav-sayings-font', 'rgb(110, 131, 150)');
        root.css('--color-secondary', '#F7F7F7');
        root.css('--color-sidebar-line', '#E6E4E4');
        root.css('--color-modal-content', '#ffffff');
        // root.css('--color-sidebar-clicked', '#EDEDED');
        $('#flatpickrDark')[0].href = '';
    } else {
        root.css('--color-primary', '#000000');
        root.css('--color-nav-sayings-font', '#000000');
        root.css('--color-secondary', '#839AA8');
        root.css('--color-sidebar-line', '#839AA8');
        root.css('--color-modal-content', '#839AA8');
        // root.css('--color-sidebar-clicked', '#99C4C8');
        $('#flatpickrDark')[0].setAttribute('href', '../static/style/flatpickr-dark.css');
    }

    $("#datepicker").flatpickr({
        time: (new Date()).getTime()
    });

    // Toastify({
    //     text: "This is a toast",
    //     duration: 3000,
    //     destination: "https://github.com/apvarun/toastify-js",
    //     newWindow: true,
    //     close: true,
    //     gravity: "top", // `top` or `bottom`
    //     position: "left", // `left`, `center` or `right`
    //     stopOnFocus: true, // Prevents dismissing of toast on hover
    //     style: {
    //         background: "linear-gradient(to right, #00b09b, #96c93d)",
    //     },
    //     onClick: function () {
    //     } // Callback after click
    // }).showToast();

    // change the saying every 5 seconds
    $.get('/static/sayings.txt', function (data) {
        sayings = data.split("\n");
        // set interval before reload a new saying
        let now = 0; // current reading line
        setInterval(function () {
            $("#saying").html(sayings[now++ % sayings.length]);
        }, 5000); // in ms.
    });

    // make the side bar expandable and collapsible
    $(".topnav-left>button:first-child").on("click", function () {
        let sidebarLeft = $("#sidebar").css('left');
        if (sidebarLeft === '0px') {
            $('#sidebar').css('position', 'fixed');
            $("#sidebar").css('left', '-250px');
            $("#mainContent").css('margin-left', '0px');
            $("#mainContent").css('width', '100%');
            $("#sidebar").css('box-shadow', 'none');
        } else {
            if ($(window).width() >= 700) {
                let mainContentWidth = $(window).width() - 250;
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

    $("#day-night").on("click", function () {
        let nav_color = root.css('--color-primary');
        if (nav_color === '#D1E7EA') {
            root.css('--color-primary', '#000000');
            root.css('--color-nav-sayings-font', '#000000');
            root.css('--color-secondary', '#839AA8');
            root.css('--color-sidebar-line', '#839AA8');
            root.css('--color-modal-content', '#839AA8');
            // root.css('--color-sidebar-clicked', '#99C4C8');
            $('#flatpickrDark')[0].setAttribute('href', '../static/style/flatpickr-dark.css');
            localStorage.setItem('dayMode', 'dark');
        } else {
            root.css('--color-primary', '#D1E7EA');
            root.css('--color-nav-sayings-font', 'rgb(110, 131, 150)');
            root.css('--color-secondary', '#F7F7F7');
            root.css('--color-sidebar-line', '#E6E4E4');
            root.css('--color-modal-content', '#ffffff');
            // root.css('--color-sidebar-clicked', '#EDEDED');
            $('#flatpickrDark')[0].href = '';
            localStorage.setItem('dayMode', 'light');
        }
    });

    // make it suitable for small devices
    $(window).resize(function () {
        adaptive();
    });

    // have some ids correct "on" when the page is updated
    let pageName = window.location.pathname.split('/')[1];
    if (pageName === 'module') {
        className = window.location.pathname.split('/')[2];
        $("#" + className).addClass("on");
    } else {
        $("#" + pageName).addClass("on");
    }

    // go to today page when clicking the home button
    $("#home").on("click", function () {
        $("#sidebar-top-table>tbody>tr:first-child").click();
    });

    // go to the page when clicking the sidebar module item
    $("#sidebar-bottom-table").each(function () {
        let trs = $(this).find("tr");
        trs.each(function () {
            $(this).on("click", function () {
                let className = $(this).attr("id");
                if (className !== undefined) {
                    window.location.href = "/module/" + className;
                    $(this).addClass("on");
                }
            });
        });
    });

    // show the modal when clicking the sidebar class items
    let little_button_deletes = $('.little-button.delete');
    let little_button_edits = $('.little-button.edit');
    for (let i = 0; i < little_button_deletes.length; i++) {
        little_button_deletes[i].addEventListener('click', function (event) {
            event.stopPropagation();
            $('#little-button-delete').modal('show');
        })
    }
    for (let i = 0; i < little_button_edits.length; i++) {
        little_button_edits[i].addEventListener('click', function (event) {
            event.stopPropagation();
            $('#little-button-edit').modal('show');
        })
    }

    // color-selector in the modal
    $(".color-selector>ul>li").on("click", function () {
        let color = $(this).children("a").children("span")[0].style.backgroundColor;
        let colorName = $(this).children("a").children("span")[1].innerText;
        let showButton = $(".selected-color-button>span");
        let showButtonColor = showButton[0];
        let showButtonColorName = showButton[1];

        showButtonColor.style.backgroundColor = color;
        showButtonColorName.innerText = colorName;
    })
    $(".color-selector-2>ul>li").on("click", function () {
        let color = $(this).children("a").children("span")[0].style.backgroundColor;
        let colorName = $(this).children("a").children("span")[1].innerText;
        let showButton = $(".selected-color-button-2>span");
        let showButtonColor = showButton[0];
        let showButtonColorName = showButton[1];

        showButtonColor.style.backgroundColor = color;
        showButtonColorName.innerText = colorName;
    })

    $(".little-button.delete").on("click", function () {
        let moduleID = this.parentNode.parentNode.id;
        let moduleName = this.parentNode.nextElementSibling.nextElementSibling.innerText;
        $('#little-button-delete-module').text(moduleName);
        moduleID_need_to_be_changed = moduleID;
    })
    $(".little-button.edit").on("click", function () {
        let moduleID = this.parentNode.parentNode.id;
        let moduleName = this.parentNode.previousElementSibling.innerText;
        $('#little-button-edit-module>input').attr("placeholder", moduleName);
        moduleID_need_to_be_changed = moduleID;
    })

    $("#edit_module_submit").on("click", function () {
        console.log(moduleID_need_to_be_changed);
        let newModuleName = $("#module-edit-input").val();
        if (newModuleName === "") {
            newModuleName = $("#module-edit-input").attr("placeholder");
        }
        let newModuleColor = $("#module-edit-color").css("background-color");
        $.ajax({
            url: '/module/edit_module',
            type: 'POST',
            data: {
                'moduleID': moduleID_need_to_be_changed,
                'new_module': newModuleName,
                'new_color': newModuleColor
            },
            success: function (res) {
                console.log(res);
                if (res['status'] === 200) {
                    alert("Successfully edited!");
                    window.location.reload();
                } else {
                    alert("Failed to edit!");
                }
            }
        })
    });

    $("#delete_module_submit").on("click", function () {
        let location = '/' + window.location.pathname.split('/')[1] + '/' + window.location.pathname.split('/')[2];
        $.ajax({
            url: '/module/delete_module',
            type: 'POST',
            data: {
                'moduleID': moduleID_need_to_be_changed
            },
            success: function (res) {
                console.log(res);
                if (res['status'] === 200) {
                    alert("Successfully deleted!");
                    if (location === "/module/" + moduleID_need_to_be_changed) {
                        window.location.href = "/today";
                    } else {
                        window.location.reload();
                    }
                } else {
                    alert("Failed to delete!");
                    window.location.reload();
                }
            }
        })
    });

    // add a new module
    $("#new_module_submit").on("click", function () {
        let newModuleName = $("#newModuleName-input").val();
        let newModuleColor = $("#newModuleColor-input").css("background-color");
        if (newModuleName === "") {
            alert("Please enter a module name!");
        } else {
            $.ajax({
                url: '/module/add_module',
                type: 'POST',
                async: true,
                data: {
                    'new_module': newModuleName,
                    'new_color': newModuleColor
                },
                success: function (res) {
                    console.log(res);
                    if (res['status'] === 200) {
                        alert(res['msg']);
                        window.location.reload();
                        // Toastify({
                        //     text: "This is a toast",
                        //     duration: 3000
                        // }).showToast();
                    } else {
                        alert(res['msg']);
                    }
                }
            });
        }
    });

    let unclassified_modules = $(".Unclassified");
    for (let i = 0; i < unclassified_modules.length; i++) {
        unclassified_modules[i].children[0].children[0].style.visibility = "hidden";
        unclassified_modules[i].children[3].children[0].style.visibility = "hidden";
    }

    $(".modules").on('click', function () {
        let module = this.childNodes[0].innerText;
        $("#module-selected").text(module);
    });
    $("#new_task_submit").on("click", function () {
        let fullDate = $("#datepicker").val();
        let module = $("#module-selected").text();
        let title = $("#new_task_title").val();
        let description = $("#new_task_description").val();
        if (fullDate === "" || module === "" || title === "") {
            alert("Please fill in all the fields! (Description is optional)");
        } else if (title.length > 50) {
            alert("The task title is too long!");
        } else {
            let date = $("#datepicker").val().split(" ")[0];
            let time = $("#datepicker").val().split(" ")[1];
            $.ajax({
                url: '/all/newTask',
                type: 'POST',
                data: {
                    'date': date,
                    'time': time,
                    'module': module,
                    'title': title,
                    'description': description
                },
                success: function (res) {
                    if (res['status'] === 200) {
                        alert(res['msg']);
                        window.location.reload();
                    } else {
                        alert(res['msg']);
                    }
                }
            })
        }

    });
});

function adaptive() {
    let sidebarLeft = $("#sidebar").css('left');
    // let sidebarLeft = $("#sidebar").getComputedStyle('left');
    // let sidebarLeft = getComputedStyle("#sidebar").getPropertyValue("left");
    if (sidebarLeft == '0px') {
        if ($(window).width() < 700) {
            $('#sidebar').css('position', 'fixed');
            $("#sidebar").css('left', '-250px');
            $("#mainContent").css('margin-left', '0px');
            $("#mainContent").css('width', '100%');
            $("#sidebar").css('box-shadow', 'none');
        }
    }
    if ($(window).width() < 625) {
        $("#saying").css('display', 'none');
    } else {
        $("#saying").css('display', '');
    }
}

function logout() {
    $.ajax({
        url: '/user/logout',
        type: 'POST',
        success: function (res) {
            if (res['status'] === 200) {
                window.location.href = '/user/login';
            } else {
                alert(res['msg']);
            }
        }
    })
}