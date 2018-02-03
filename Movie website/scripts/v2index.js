var change = 45;
var clicked = 1;

var $w = $(window).scroll(function(){
    if ( $w.scrollTop() > change ) {
      $('.logo').css('font-size','25px');
      $('.logo ').css('line-height','20px');
      $('.logo ').css('bottom','4px');
      $('.NaviCon').removeClass('navMargin');
      $('.NaviCon').css('padding-top','0px');
      $('.NaviBar').css('position', 'fixed');
      $('.NaviBar').css('height', '50px');
      $('.gapfil').css('height', '100px');
    } else {
      $('.logo').css('font-size','43px');
      $('.logo ').css('line-height','34px');
      $('.logo ').css('bottom','13px');
      $('.NaviCon').addClass('navMargin');
      $('.NaviCon').css('padding-top','50px');
      $('.NaviBar').css('position', 'relative');
      $('.NaviBar').css('height', '100px');
      $('.gapfil').css('height', '0px');
    }
});

$('.menuHam').on('click',function(){
  console.log('click');
  if(clicked == 0){
    $('.part').css('background-color','rgba(255,255,255,1)');
    $('.NaviCon').addClass('hideBlock');
  } else {
    $('.part').css('background-color','rgba(235,235,235,1)');
    $('.NaviCon').removeClass('hideBlock');
    clicked = -1;
  }
  clicked++;
});


$("img.lazy").lazyload();