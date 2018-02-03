var params = window.location.pathname.split('/').slice(1); // ["1", "my-event"]
var actt = 'imdb';
var genre = params[1];
var year = parseInt(params[1]);
var currentPage = parseInt(params[2]); //This has to be parsed as int otherwise it will add string with int
var totalPages = 0;



if(Number.isInteger(year)){
	genre = 'none';
} else if(!Number.isInteger(genre)){
	year = 'none';
}


function act(x){
	actt = x;
	datab(actt,currentPage, genre, year,0,0);
	$('.pagination').empty();
	$('.movieRef').remove();
}

function datab(ac,cu,ge,ye,search,rand){
      console.log(ac,cu,ge,ye,search, rand);
	$('.movies').empty();
      ac = '0';
      if(genre == 'Science-Fiction'){ console.log('lol')}
      console.log(ac.length);
	if(ac.length >= -200){
            console.log(ac.length);
		$.ajax({
	      url: '/phpScripts/getmovies.php',
            type: "post", //request type,
            dataType: 'json',
            data: {action: ac, currentPage: cu, genre: ge, year: ye, query: search, random: rand},
            success:function(output){
                  console.log(JSON.stringify(output));
                  console.log('Why u no show this');
            	for(i=0; i<Object.keys(output).length-5;i++){
            		mainMovies(output)
            	}
            	totalPages = Math.ceil(output['all_result']/36);
            	var pag = getPagination(cu,totalPages,5);
                  console.log(output['all_result'], '/36');
                  console.log('pag[0]=',pag[0],'pag[1]=',pag[1],'pag[2]=',pag[2]);
                  console.log(totalPages);
            	if(genre == 'Science Fiction'){genre='Science_Fiction'}
                        if(rand == 0){
            		for(i=pag[1];i<pag[2]+1;i++){
            			if(i == cu){
                                    
            				if(ye=='none' && ge != 'none'){
            					$('.paginati').append('<a class="page" id="selected" href="/Genre/'+ge+'/'+i+'" >'+i+'</a>');
            				} else if(ge=='none' && ye != 'none'){
            					$('.paginati').append('<a class="page" id="selected" href="/Year/'+ye+'/'+i+'" >'+i+'</a>');
            				} else {
                                          search = search.replace(/ /g,'+')
                                          $('.paginati').append('<a class="page" id="selected" href="/search/movie?query='+search+'&page='+i+'" >'+i+'</a>');
                                    }
            			} else {
            				if(ye=='none' && ge != 'none'){
            					$('.paginati').append('<a class="page" href="/Genre/'+ge+'/'+i+'">'+i+'</a>');
            				} else if(ge=='none' && ye != 'none'){
            					$('.paginati').append('<a class="page" href="/Year/'+ye+'/'+i+'">'+i+'</a>');
            				} else{
                                          search = search.replace(/ /g,'+')
                                          $('.paginati').append('<a class="page" href="/search/movie?query='+search+'&page='+i+'" >'+i+'</a>');
                                    }
                                    console.log(output['query'].length);
            			}
            		}         
                        } else {
                              $('.caption').css({"min-height:":"100%","display":'flex', "justify-content":"center","align-items":"center"})
                              $('.caption').addClass('randCaption');
                              $('.movie img').css('display','none');
                              $('.capGenre').css('display','none');
                              $('.caption h2').css('text-align','center');
                        }  
            	},
            	error: function (request, status, error) {
            		console.log(request.responseText, status, error);
                        console.log('error?')
            	}
            });
	}
}


function getPagination(currentPage, maxPages, sizePagination){
	var paginationMin = 1;
	var paginationMax = 0;
	if(currentPage >= 3){
		paginationMin = currentPage - 2;
		if(maxPages >= (currentPage + sizePagination / 2)){
			paginationMax = parseInt(currentPage) + parseInt(sizePagination)/2 - 0;
                  console.log('paginationMax',paginationMax,'currentPage',currentPage,'sizePagination',sizePagination);
		} else {
			paginationMin = maxPages - (sizePagination-1);
			paginationMax = maxPages;

		}
	} else {
		paginationMin = 1;
		paginationMax = sizePagination;
	}
	var paginat = [currentPage,paginationMin,paginationMax];
	return paginat;
}

function mainMovies(output){
      try{var replaced = output[i]['movie_title'].replace(/ /g,'-')}
      catch(err){
            console.log(output[i]['movie_title'])
            var replaced = 'error';
      }
$('.movieBody').append('<a class="movieRef" href="/Movie/' + output[i]['id'] + '/' + replaced + '">\
                        <div class="movie">\
                        <img src="/Cool/movieImages_med/' + output[i]['movie_image'] + '" alt="' + output[i]['movie_title'] + '" class="movieImage lazyload"/>\
                        <div class="link"></div>\
                        <div class="caption" id="capt">\
                        <h2 class="capTitle">' + output[i]['movie_title'] + '</h2>\
                        <h3 class="capGenre">' + output[i]['movie_genre'] + '</h3>\
                        </div>\
                        </div>\
                        </a>');
}