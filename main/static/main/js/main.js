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

function getDistance(ele){
    var scrollTop = $('.messages').offset().top,
    elementOffset = ele.offset().top,
    distance      = (elementOffset - scrollTop);
    return distance;
}

function getBackground(){
    var ins = Math.abs(getDistance($('.introduction'))),
        fea = Math.abs(getDistance($('.features'))),
        cta = Math.abs(getDistance($('.cta')));

    if (ins < fea && ins < cta){
        return '1';
    }
    else if (fea < ins && fea < cta){
        return '2';
    }
    else if (cta < ins && cta < fea){
        return '3';
    }
}


$(document).ready(function(){

    $(function () {
        var $win = $(window);

        $win.scroll(function () {
            bg = getBackground();
            console.log(bg);
            if (bg == 1){
                // $('.introduction').css(
                //     {'background-attachment' : 'fixed'}
                // );
            }
            else if (bg == 2){
                // $('.features').css(
                //     {'background-attachment' : 'fixed'}
                // );
            }
            else if(bg == 3){
                // $('.cta').css(
                //     {'background-attachment' : 'fixed'}
                // );
            }
        });
    });


    $('.collection-item').click(function(){
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
        var stat = $(".collection-item");
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

});





