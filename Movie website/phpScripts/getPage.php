<?php
 	include 'connect.php';
	/*$id = $_POST['id'];
  	$sql = 'SELECT * from movies WHERE id = '.$id;
  	$result = mysqli_query($conn,$sql);
  	while($row = mysqli_fetch_assoc($result)) {
		if(mysqli_num_rows($result) > 0) {
			$id = $row['id'];
			$title = utf8_decode($row['movie_title']);
			$thumbnail = $row['movie_image'];
			$released = $row['movie_released'];
			$description = utf8_decode($row['movie_full_story']);
			$actors = utf8_decode($row['movie_actors']);
			$genres = explode(', ',$row['movie_genre']);
			$meta_score = $row['movie_metaScore'];
			$limit = round(10 / count($genres));
			for ($i=0; $i < count($genres); $i++) {

				$sql2 = 'SELECT * from movies WHERE movie_genre LIKE "%'.$genres[$i].'%"  ORDER BY rand() LIMIT '.$limit.'';
				$result2 = mysqli_query($conn,$sql2);
				while($row2 = mysqli_fetch_assoc($result2)) {
					if(mysqli_num_rows($result2) > 0) {
						if($row2['id'] != $id){
							$data = array('id' => $row2['id'], 'title' => utf8_decode($row2['movie_title']), 'thumb' => $row2['movie_image']);
							$arr[] = $data;
						}
					}
				}
			}


			$screens = 'screens';
			$tagline = $row['movie_tagline'];
			$keywords = $row['movie_keywords'];
			$runtime = $row['movie_runtime'];
		
			$genre_final = implode(', ', $genres);
			$data = array('title' => $title, 'poster' => $thumbnail, 'metascore' => $meta_score, 'released' => $released, 'story' => $description, 'actors' => $actors, 'genres' => $genres, 'backdrops' => $screens, 'tagline' => $tagline, 'keywords' => $keywords, 'runtime' => $runtime);
			$arr['movie'] = $data;

			

		}
	}


echo json_encode($arr,JSON_FORCE_OBJECT);


*/

$movie = $_GET['id'];

$sql = "SELECT * from movies WHERE id = " . $movie;
$result = mysqli_query($conn,$sql);
while ($row = mysqli_fetch_assoc($result)) {
	if (mysqli_num_rows($result) > 0) {
		if ( intval($row['movie_metaScore']) >= 70){
			$color = '#66CC33';
		} elseif ( intval($row['movie_metaScore']) >= 40) {
			$color = '#FFCC33';
		} else {
			$color = 'FF0000';
		}
		# 
		# 
		# 
		$movie_backdrops = (int)$row['movie_backdrops'];
		$movie_back = '';

		for ($i=0; $i <$movie_backdrops ; $i++) {
			#/Cool/Movie-backdrops-official/e370772c83405e1ff4fae0fa89571557_bdrop0.jpg
			$link = '/Cool/Movie-backdrops-official/' . $row['movie_id'] . '_bdrop' . $i . '.jpg';
			$movie_back .= '<li><img src="'. $link .'"></li>';
		}

		echo '<div class="contentCon">';
		echo '	<div class="top-text">';
		echo '		<div class="top-text-1">';
		echo '			<h1>' . $row['movie_title'] . '</h1>';
		echo '			<h4>' . $row['movie_genre'] . ' | ' . $row['movie_runtime'] . ' | ' . $row['movie_released'] . '</h4>';
		echo '		</div>';
		echo '		<div class="top-text-2">';
		echo '			<div class="rating" style="background-color: ' . $color . '">' . $row['movie_metaScore'] . '</div>';
		echo '		</div>';
		echo '	</div>';
		echo '	<div class="poster">';
		echo '		<div class="part-left">';
		echo '			<img src="/Cool/movieImages_med/' . $row['movie_id'] . '.jpg' . '" alt="' . $row['movie_title'] . '">';
		echo '		</div>';
		echo '		<div class="part-right">';
		echo '			<div id="slider" class="flexslider">';
		echo '				<ul class="slides">';
		echo $movie_back;
		echo '				</ul>';
		echo '			</div>';
		echo '			<div id="carousel" class="flexslider">';
		echo '				<ul class="slides">';
		echo $movie_back;
		echo '				</ul>';
		echo '			</div>';
		echo '		</div>';
		echo '	</div>';

		echo '	<div class="storyline">';
		echo '		<h2> Storyline </h2>';
		echo '		<h3>' . $row['movie_story'] . '</h3>';
		echo '	</div>';
		echo ' 	<div class="actorsCon">';
		echo '		<h2> Actors </h2>';
		echo '		<h3>' . $row['movie_actors'] . '</h3>';
		echo '	</div>';
		echo '	<div class="moviesLike">';
		echo '		<h2> Movies you might like </h2>';
		echo '	</div>';
		echo '</div>';
	}
}



?>