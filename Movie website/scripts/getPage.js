var params = window.location.pathname.split('/').slice(1); // ["1", "my-event"]
var id = parseInt(params[1]);
console.log(params, id);
$.ajax({
	url: '/phpScripts/getPage.php',
	type: "post", //request type,
	dataType: 'json',
	data: {id:id},
	success:function(output){
		var page = output['movie'];
		var suggests = [];
		console.log(JSON.stringify(output));
		for (var i = 0; i < Object.keys(output).length - 1; i++) {
			suggests.push('<a href="/Movie/' + output[i]['id'] +'/' + output[i]['title'] + '"><img class="movie" src="/Cool/movieImages_med/' + (output)[i]['thumb'] + '"/></a>');
		}
		$('.gridSystem').append(' 	<div class="contentCon">\
										<div class="poster">\
											<div class="part-left">\
												<img src="/Cool/movieImages_med/' + page['poster'] + ' ">\
											</div>\
											<div class="part-right">\
												<img src="">\
											</div>\
										</div>\
										<div class="top-text">\
											<div class="top-text-1">\
												<h1>' + page["title"] + '<small><q>' + page['tagline'] + '</q></small></h1>\
												<h4>' + $.map(page['genres'], function(val) { return ' ' + val  }) + ' | ' + page['runtime'] + ' | ' + page['released'] + '</h4>\
											</div>\
											<div class="top-text-2">\
												<div class="rating">' + page['metascore'] + '</div>\
											</div>\
										</div>\
										<div class="storyline">\
											<h2>Storyline</h2>\
											<h3>' + page['story']+ '</h3>\
										</div>\
										<div class="actorsCon">\
											<h2> Actors </h2>\
											<h3>' + page['actors']+ '</h3>\
										</div>\
										<div class="moviesLike">\
											<h2>Movies you might like</h2>\
											<div class="movieCon">\
											'+suggests.join('')+'\
											</div>\
										</div>\
									</div>\
									')
			$('head').append('<title>' + page['title'] + '</title>');
			infobar();
			slideShow();
			console.log('beginning of the action');
			
			$('.loader').remove();
			if($('.slidesjs-pagination-item').length == 1){
				console.log('activated');
				
			}
			},
	error: function (request, status, error) {
		console.log(request.responseText, status, error);
            console.log('error?')
	}
});
console.log('second');


function infobar(){
	var bar = $('div.infobar')
	var dataset = []
	bar.each(function() {
	    var number = $(this).attr('data-value')
	    if (number < 0) {
	        number = 0;
	    }
	    if (isInt(number)) {
	        dataset.push(parseInt(number));
	    }
	});
	var total = dataset.reduce(function(a, b) {
	    return a + b
	}, 0);
	var totalLength = 760;
	var maxLength = totalLength - 100;
	var colors = ['#ffb34e', '#ff734e', '#4c9cd9']
	dataSet();
	$(window).on('click', function() {
	    dataSet();
	});
	bar.on('click', function() {
	    event.stopPropagation();
	    bar.css('width', '5%');
	    $(this).css('width', '79%');
	})
	bar.mouseover(function() {
	    $('body').append('<div class="toolInfo"></div>')
	});
	bar.mouseout(function() {
	    $('.toolInfo').remove();
	});
	bar.mousemove(function() {
	    var x = event.pageX + 20;
	    var y = event.pageY - 40;
	    var money = '$' + numberWithCommas($(this).attr('data-value'));
	    if ($(this).attr('data-value') == 0) {
	        money = 'NaN';
	    }
	    if (event.pageX > $(window).width() - 160) {
	        x = event.pageX - 150
	    }
	    $('.toolInfo').css({
	        'top': y,
	        'left': x
	    });
	    $('.toolInfo').html('<div class="cate">' + $(this).attr('data-title') + '</div> <div class="num"> ' + money + '</div>');
	});
	function dataSet() {
	    bar.each(function(index) {
	    	var num = Math.round((dataset[index] / total) * 100) - 2 ;
	        $(this).css('width', (num) + '%');
	        $(this).css('background-color', colors[index]);
	    });
	}
	function isInt(n) {
	    return parseInt(n) % 1 === 0;
	}
	function numberWithCommas(x) {
	    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	}
}

function slideShow(){
	$(function(){
		$("#slides").slidesjs({
			width: 960,
			height: 551.469,
			navigation:{
				active: false,
			},
			callback: {
				loaded: function(number){

					$( '.slidesjs-pagination-item' ).each( function( index, element ) {
						var target = $( element ).find( 'a' ),
						src = $('.allImg img:eq('+index+')').attr('src')
						$(target).html('<div class="pagina" style="background-image:url(\''+src+'\');"></div>')
					});
					if($('.pagina').length == 1){
						$('.imga.slidesjs-slide').css('position', 'static');
					}
				}
			},
		});
	});
	console.log('end of slideshow');
}