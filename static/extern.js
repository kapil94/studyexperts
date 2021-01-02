$('.btn').click(function(){
    $('.nave-align').toggle();

  });

  $(".text-action")
      .attr('unselectable', 'on')
      .css({
          'user-select': 'none',
          'MozUserSelect': 'none'
      })
      .on('selectstart', false)
      .on('mousedown', false);


  $(".carousel-control-next").click(function(){
    $(".item1").addClass("active");
    $(".item0").removeClass("active");
  });

  $('.carousel-control-prev').click(function(){

    if($(".item1").hasClass("active"))
    {
      $(".item0").addClass("active");
      $(".item1").removeClass("active");
    }
  });

$("#pol-prev").click(function(){


console.log("Hello");
});

$(".dropdown-toggle").click(function(){

$(".drop_down").toggle();

});

$(document).click(function(){
  $("").hide();
});

