var $cards = $('.card');
var $movies = 0;
    
var checkk = setInterval(function(){
  if ($('.movie').length >= 1){
    $movies = $('.movie');
    $.each($movies, function(){
      var $movie = $(this);
      var card_top = ($movie.offset().top+50);
      if ($(window).scrollTop() + $(window).height() >= card_top && !$movie.hasClass('in-view')) {
          $movie.addClass('in-view');
      } 
    });
    clearInterval(checkk);
  }
}, 50);


$(window).scroll(function(){
  var scrollBottom = $(window).scrollTop() + $(window).height();
  $.each($cards, function(){
    var $card = $(this);
    var card_top = ($card.offset().top+50);
    if (scrollBottom >= card_top && !$card.hasClass('in-view')) {
      $card.addClass('in-view');
    }
  });
  $.each($movies, function(){
    var $movie = $(this);
    var card_top = ($movie.offset().top+50);
    if (scrollBottom >= card_top && !$movie.hasClass('in-view')) {
        $movie.addClass('in-view');
    } 
  });

});