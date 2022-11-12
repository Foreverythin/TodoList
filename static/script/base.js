$(document).ready(function () {
    // mainContent adaptive to window size
    adaptive();
    var moduleID_need_to_be_changed;  // moduleID need to be changed

    var dayMode = localStorage.getItem('dayMode');  // get dayMode from localStorage

    // whether the dayMode is null
    if (dayMode == null) {
        localStorage.setItem('dayMode', 'light');  // set dayMode to light
    }

    // toggle dayMode
    var root = $(':root');
    if (dayMode === 'light') {
        root.css('--color-primary', '#D1E7EA');
        root.css('--color-nav-sayings-font', 'rgb(110, 131, 150)');
        root.css('--color-secondary', '#F7F7F7');
        root.css('--color-sidebar-line', '#E6E4E4');
        root.css('--color-modal-content', '#ffffff');
        $('#flatpickrDark')[0].href = '';
    } else {
        root.css('--color-primary', '#000000');
        root.css('--color-nav-sayings-font', '#000000');
        root.css('--color-secondary', '#839AA8');
        root.css('--color-sidebar-line', '#839AA8');
        root.css('--color-modal-content', '#839AA8');
        $('#flatpickrDark')[0].setAttribute('href', '../static/flatpickr/flatpickr-dark.css');
    }
    $(".flatpickr.selector").flatpickr({
        time: (new Date()).getTime()  // set the default time to now
    });

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

    // make the side bar expandable and collapsible
    $("#day-night").on("click", function () {
        let nav_color = root.css('--color-primary');
        if (nav_color === '#D1E7EA') {
            root.css('--color-primary', '#000000');
            root.css('--color-nav-sayings-font', '#000000');
            root.css('--color-secondary', '#839AA8');
            root.css('--color-sidebar-line', '#839AA8');
            root.css('--color-modal-content', '#839AA8');
            $('#flatpickrDark')[0].setAttribute('href', '../static/flatpickr/flatpickr-dark.css');
            localStorage.setItem('dayMode', 'dark');
        } else {
            root.css('--color-primary', '#D1E7EA');
            root.css('--color-nav-sayings-font', 'rgb(110, 131, 150)');
            root.css('--color-secondary', '#F7F7F7');
            root.css('--color-sidebar-line', '#E6E4E4');
            root.css('--color-modal-content', '#ffffff');
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
                    window.location.href = "/module/" + className;  // go to the subpage about the module
                    $(this).addClass("on");  // set the current item to "on"
                }
            });
        });
    });

    // show the modal when clicking the sidebar class items
    let little_button_deletes = $('.little-button.delete');
    let little_button_edits = $('.little-button.edit');
    for (let i = 0; i < little_button_deletes.length; i++) {
        little_button_deletes[i].addEventListener('click', function (event) {
            event.stopPropagation();  // prevent the event from bubbling up
            $('#little-button-delete').modal('show');  // show the modal
        })
    }
    for (let i = 0; i < little_button_edits.length; i++) {
        little_button_edits[i].addEventListener('click', function (event) {
            event.stopPropagation();  // prevent the event from bubbling up
            $('#little-button-edit').modal('show');  // show the modal
        })
    }

    // color-selector in the modal
    $(".color-selector>ul>li").on("click", function () {
        let color = $(this).children("a").children("span")[0].style.backgroundColor;
        let colorName = $(this).children("a").children("span")[1].innerText;
        let showButton = $(".selected-color-button>span");
        let showButtonColor = showButton[0];
        let showButtonColorName = showButton[1];

        showButtonColor.style.backgroundColor = color;  // change the color of the button
        showButtonColorName.innerText = colorName;  // change the color name of the button
    })
    // color-selector in the modal
    $(".color-selector-2>ul>li").on("click", function () {
        let color = $(this).children("a").children("span")[0].style.backgroundColor;
        let colorName = $(this).children("a").children("span")[1].innerText;
        let showButton = $(".selected-color-button-2>span");
        let showButtonColor = showButton[0];
        let showButtonColorName = showButton[1];

        showButtonColor.style.backgroundColor = color;  // change the color of the button
        showButtonColorName.innerText = colorName;  // change the color name of the button
    })

    // make the sidebar expandable and collapsible
    $(".little-button.delete").on("click", function () {
        let moduleID = this.parentNode.parentNode.id;  // get the module id
        let moduleName = this.parentNode.nextElementSibling.nextElementSibling.innerText;  // get the module name
        $('#little-button-delete-module').text(moduleName);  // set the module name in the modal
        moduleID_need_to_be_changed = moduleID;
    })
    // make the sidebar expandable and collapsible
    $(".little-button.edit").on("click", function () {
        let moduleID = this.parentNode.parentNode.id;  // get the module id
        let moduleName = this.parentNode.previousElementSibling.innerText;  // get the module name
        $('#little-button-edit-module>input').attr("placeholder", moduleName);  // set the placeholder of the input
        moduleID_need_to_be_changed = moduleID;
    })

    // make the sidebar expandable and collapsible
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
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                    // refresh the page
                    setTimeout(function () {
                        window.location.reload();
                    }, 1200);
                } else {
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                }
            }
        })
    });

    // make the sidebar expandable and collapsible
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
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                    // refresh the page
                    setTimeout(function () {
                        if (location === "/module/" + moduleID_need_to_be_changed) {
                            window.location.href = "/today";
                        } else {
                            window.location.reload();
                        }
                    }, 1200);
                } else {
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
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
                    if (res['status'] === 200) {
                        // show the tip info
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        // refresh the page
                        setTimeout(function () {
                            window.location.reload();
                        }, 1200);
                    } else {
                        // show the tip info
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    }
                }
            });
        }
    });

    // make the unclassified modules unseen
    let unclassified_modules = $(".Unclassified");
    for (let i = 0; i < unclassified_modules.length; i++) {
        unclassified_modules[i].children[0].children[0].style.visibility = "hidden";
        unclassified_modules[i].children[3].children[0].style.visibility = "hidden";
    }

    // turn to the module page
    $(".modules").on('click', function () {
        let module = this.childNodes[0].innerText;
        $("#module-selected-basePage").text(module);
    });
    // submit the new module info
    $("#new_task_submit").on("click", function () {
        let fullDate = $("#datepicker-newTask").val();  // get the date
        let module = $("#module-selected-basePage").text();  // get the module
        let title = $("#new_task_title").val();  // get the title
        let description = $("#new_task_description").val();  // get the description
        if (fullDate === "" || module === "" || title === "") {
            // show the tip info
            Toastify({
                text: "Please fill in all the fields! (Description is optional)",
                duration: 1200
            }).showToast();
        } else if (title.length > 50) {
            // show the tip info
            Toastify({
                text: "The task title is too long",
                duration: 1200
            }).showToast();
        } else {
            let date = fullDate.split(" ")[0];  // get the date
            let time = fullDate.split(" ")[1];  // get the time
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
                        // show the tip info
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        // refresh the page
                        setTimeout(function () {
                            window.location.reload();
                        }, 1200);
                    } else {
                        // show the tip info
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    }
                }
            })
        }

    });


    var taskID;
    // edit the task
    $(".deleteTask-td").on("click", function () {
        taskID = this.attributes[0].value;
        $("#deleteTaskModel").modal("show");
    });
    // edit the task
    $(".editTask-td").on("click", function () {
        let previousTask = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].textContent;
        let previousTaskModuleName = this.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[2].attributes[0].value;
        let previousDescription = this.parentNode.parentNode.parentNode.parentNode.parentNode.children[1].innerText;
        let previousDueDate = this.parentNode.parentNode.parentNode.parentNode.parentNode.children[0].children[0].children[0].children[0].innerText;
        previousDueDate = previousDueDate.substring(previousDueDate.length - 16);
        $("#datepicker-editTask").val(previousDueDate);
        $("#edit-task-title-placeholder-in-modal").val(previousTask);
        $("#edit-task-description-in-modal").val(previousDescription);
        $("#module-selected-editing-task").text(previousTaskModuleName);

        taskID = this.attributes[0].value;
        $("#editTaskModel").modal("show");
    });

    // submit to delete the task
    $("#delete_task_submit").on("click", function () {
        $.ajax({
            url: "/all/deleteTask",
            type: "POST",
            data: {
                taskID: taskID
            },
            success: function (res) {
                if (res["status"] === 200) {
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                    // refresh the page
                    setTimeout(function () {
                        window.location.reload();
                    }, 1200);
                } else {
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                }
            }
        });
    });

    // submit to edit the task
    $("#edit_task_submit").on("click", function () {
        let fullDate = $("#datepicker-editTask").val();
        let moduleName = $("#module-selected-editing-task").text();
        let taskTitle = $("#edit-task-title-placeholder-in-modal").val();
        let taskDescription = $("#edit-task-description-in-modal").val();
        if (fullDate === "" || moduleName === "" || taskTitle === "") {
            Toastify({
                text: "Please fill in all the fields! (Description is optional)",
                duration: 1200
            }).showToast();
        } else if (taskTitle.length > 50) {
            // show the tip info
            Toastify({
                text: "The task title is too long",
                duration: 1200
            }).showToast();
        } else {
            let date = fullDate.split(" ")[0];
            let time = fullDate.split(" ")[1];
            $.ajax({
                url: "/all/editTask",
                type: "POST",
                data: {
                    'taskID': taskID,
                    'date': date,
                    'time': time,
                    'moduleName': moduleName,
                    'taskTitle': taskTitle,
                    'taskDescription': taskDescription
                },
                success: function (res) {
                    if (res["status"] === 200) {
                        // show the tip info
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                        // refresh the page
                        setTimeout(function () {
                            window.location.reload();
                        }, 1200);
                    } else {
                        // show the tip info
                        Toastify({
                            text: res['msg'],
                            duration: 1200
                        }).showToast();
                    }
                }
            })
        }
    });

    // to complete the task
    $(".uncompleted.icon").on("click", function () {
        let taskID = this.attributes[0].value;
        $.ajax({
            url: "/all/completeTask",
            type: "POST",
            data: {
                taskID: taskID
            },
            success: function (res) {
                if (res["status"] === 200) {
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                    // refresh the page
                    setTimeout(function () {
                        window.location.reload();
                    }, 1200);
                } else {
                    // show the tip info
                    Toastify({
                        text: res['msg'],
                        duration: 1200
                    }).showToast();
                }
            }
        });
    });
});

// the function to resize the height of the main content and the sidebar
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

// the function for users to logout
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