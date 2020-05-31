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
});