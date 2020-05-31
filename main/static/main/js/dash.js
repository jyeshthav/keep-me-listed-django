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

$(document).ready(function(){

    $('.status-btn').click(function(){
        var status = $(this).attr('task-status');
        var title = $(this).attr('title');
        var tlist = $(this).attr('list');
        var owner = $(this).attr('owner');
        // console.log(status);

        $.ajax({
            type: 'POST',
            url: '/status',
            beforeSend:function (request) {
                request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            data:{status, title, tlist, owner},
            success: function(result){
                // console.log(result);
                location.reload();
            },
        });
    });

    $("input[type=checkbox]").change(function() {
        if($(this).is(":checked")) {
            $.ajax({
                type: 'POST',
                url: '/sortby',
                beforeSend:function (request) {
                    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                },
                success: function(result){
                    $('.list-container').html(result)
                },
            });
        }
        else {
          $.ajax({
            type: 'POST',
            url: '/homepage',
            beforeSend:function (request) {
                request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            success: function(result){
                location.reload();                
            },
        });
        }
    });

    function status() {
        var stat = $(".collapsible-header");
    //        ---for adding class based on attribute---
        stat.each(function () {
          if ($(this).attr('task-status') == '1') {
              $(this).addClass("checked");
          }
          else{
              $(this).removeClass("checked");
          }
        });
    }
    status();

    $('.delete-btn').click(function(){
        var status = $(this).attr('task-status');
        var title = $(this).attr('title');
        var tlist = $(this).attr('list');
        var owner = $(this).attr('owner');
        console.log(status, title, tlist, owner);

        $.ajax({
            type: 'POST',
            url: '/delete_task',
            beforeSend:function (request) {
                request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },
            data:{status, title, tlist, owner},
            success: function(result){
                // console.log(result);
                location.reload();
            },
        });
    });

});





