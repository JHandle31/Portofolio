<style type="text/css">
    
.logo{
    padding-left: 20px;
    color: white;
    transition: all 0.3s ease;
    position: absolute;
    bottom: 13px;
    font-family: Segoe UI;
    font-size: 43px;
    letter-spacing: -1.95px;
    font-weight: 400;
    line-height: 34px;
    text-align: right;
    cursor: pointer;
    z-index: 2;
}

.thi{
    font-weight: 100;
    padding-left: 5px;
}

.bol{
    font-weight: 700;
}


</style>
<div class="NaviBar" style="top: 0;">
    <div class='imgCon'>
        <div class='logo'>
                MOVIE<span class='thi'>TO</span><br><span class='bol'>WATCH</span>
        </div>
    </div>
    <div class="NaviCon hideBlock navMargin">
        <a href="/Home"><span class="item">Home</span></a>
        <div class="drop" id="genre">
            <span class="item">Genre</span>
            <div class="dropDown" id="genreDropDown">
                <a href='/movies.php?genre=Action&page=1' class="dropItem">Action</a>
                <a href='/Genre/Adventure/1' class="dropItem">Adventure</a>
                <a href='/Genre/Animation/1' class="dropItem">Animation</a>     
                <a href='/Genre/Comedy/1' class="dropItem">Comedy</a>
                <a href='/Genre/Crime/1' class="dropItem">Crime</a>
                <a href='/Genre/Drama/1' class="dropItem">Drama</a>
                <a href='/Genre/Documentary/1' class="dropItem">Documentary</a>
                <a href='/Genre/Family/1' class="dropItem">Family</a>
                <a href='/Genre/Fantasy/1' class="dropItem">Fantasy</a>
                <a href='/Genre/History/1' class="dropItem">History</a>
                <a href='/Genre/Horror/1' class="dropItem">Horror</a>
                <a href='/Genre/Music/1' class="dropItem">Music</a>
                <a href='/Genre/Romance/1' class="dropItem">Romance</a>
                <a href='/Genre/Science_Fiction/1' class="dropItem">Sci-fi</a>
                <a href='/Genre/Thriller/1' class="dropItem">Thriller</a>
                <a href='/Genre/War/1' class="dropItem">War</a>
                <a href='/Genre/Western/1' class="dropItem">Western</a>
            </div>
        </div>
        <div class="drop" id="year">
            <span class="item">Year</span>
            <div class="dropDown" id="yearDropDown">
                <?php 
                  for($i=2017; $i>=1914; $i--){
                    echo '<a href="/Year/' . $i . '/1" class="dropItem">'. $i . '</a>'; 
                  }
                ?>
            </div>
        </div>
        <a href="/movies/random"><span class="item">Random</span></a>
        <form action='/search/movie' method="get">
		  <input name='query' type="text" id="searchInput" class="inputItem" placeholder="Search for a movie">
          <input type="hidden" name="page" value="1" >
			<button type='submit' id="search"><span class="item"><span class="glyphicon glyphicon-search" aria-hidden="true"></span></span></button>
        </form>
    </div>
	<div class="menuHam"><span class="part"></span><span class="part"></span><span class="part"></span></div>
	
</div>
<div class="gapfil"></div>