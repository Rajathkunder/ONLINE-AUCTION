$(function(){

    $('#portfolio').click(function(){
        $('.home').addClass('hide');
      $('.portfolio').removeClass('hide');
    });
    
    $('#home').click(function(){
        $('.portfolio').addClass('hide');
      $('.home').removeClass('hide');
    });
    
    })