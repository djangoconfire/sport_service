function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$('.selectpicker').selectpicker({
    style: 'btn-info',
    size: 4
});

$("#saveButton").on("click", function() {
    var buddies_ids = [],
        buddies_names = [];
    $("#buddies").find("option:selected").each(function(index) {
         buddies_ids.push($(this).attr("value"));
        buddies_names.push($(this).text());
    });
    // Create panel with saved task
    var spanHTML = "";
    for (var buddy of buddies_names) {
        spanHTML += '<span class="label label-success">' + buddy + '</span>'
    }
    panelHTML = '<div class="col-md-4"><div class="panel panel-primary">' +
        '<div class="panel-heading">' +
        '<h3 class="panel-title">' + $("#taskName").val() + '</h3>' +
        '</div><div class="panel-body">' + $("#focusedInput").val() + '<br />' + spanHTML + '</div>' +
        '</div></div>';

    $(".attachData .row").append(panelHTML);
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: window.location.origin + "/task/",
        data: {
            name: $("#taskName").val(),
            description: $("#focusedInput").val(),
            csrfmiddlewaretoken: csrftoken,
            buddies: buddies_ids
        },
        success: function(data) {
            $.notify(data.message, "info")
        }
    });
    // Reset modal
    $("#taskName").val("");
    $("#focusedInput").val("");
    $(".selectpicker").selectpicker("deselectAll")
    $("#assignment").modal("toggle");

});

// for buddy detail
$("#saveBuddy").on("click", function() {

    var csrftoken = getCookie('csrftoken');
    $.ajax({
        type: "POST",
        url: window.location.origin + "/buddy/create/",
        data: {
            buddy_id:   $("#buddy_id").val(),
            batch_id:   $("#batch_id").val(),
            batch_name: $("#batch_name").val(),
            batch_day:  $("#batch_day").val(),
            batch_time: $("#batch_time").val(),
            csrfmiddlewaretoken: csrftoken,
            
        },
        success: function(data) {
            $.notify(data.message, "info")
        }
    });
    // Reset modal
    
    $("#buddy_id").val("");
    $("#batch_id").val("");
    $("#batch_name").val("");
    $("#batch_day").val("");
    $("#batch_time").val("");
    $("#buddy").modal("toggle");

});
