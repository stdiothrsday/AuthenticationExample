$(document).ready(function(){

  //makes create profile button visible
  $("#seek").click(function(){
    $(".btn.btn-outline-danger.btn-lg").animate({
      height: 'toggle'
    });
  });

});