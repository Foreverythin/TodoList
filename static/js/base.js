$(document).ready(function() {
    // read txt one line by one line
    $.get('/static/sayings.txt', function(data) {
        alert(data);
    });
});