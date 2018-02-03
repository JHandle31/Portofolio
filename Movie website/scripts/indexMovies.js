/*var colors = ['#0099CC','#CCFFCC','#66CCFF','#003399','#FF3333','#999999','#669999','#003333','#005502','#CCFFBB']*/

$('.overlay').each( function(i) {
	$(this).css("background-color", 'rgb(' + getRandomInt(0,255) + ',' + getRandomInt(0,255) + ',' + getRandomInt(0,255) + ')')
});

$(window).scroll(function(){
	var scrollDown = $(window).scrollTop() + $(window).height();
	$('.inTh').each(function(i){
		if($(this).offset().top <= scrollDown){
			if($(this).parent().hasClass('PartL')){
				$(this).addClass('SIL')
			} else {
				$(this).addClass('SIR')
			}
		}
	})
});

function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min; //The maximum is exclusive and the minimum is inclusive
}
