$('document').ready(function(){
    $('#loginhref').text('Logout');
    $('#loginhref').attr('href', '/logout');
    $.ajax({
        url: '/getmypoint/',
        type: "GET",
        dataType:'json',
    }).done(function( responce ) {
        var status = responce.status;

        $('.alert').hide();

        if(status == '1'){
            $("#points").html(responce.points)
        }
    });