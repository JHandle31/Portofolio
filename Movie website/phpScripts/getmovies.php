<?php
/*
$action = $_POST['action'];
$genre = $_POST['genre'];
$currentPage = $_POST['currentPage'];
$year = $_POST['year'];
$query = $_POST['query'];
$random = $_POST['random'];
$moviesAmount = 36;
$index = ($currentPage-1) * 36;


if($genre == 'Science-Fiction'){$genre = 'Science_Fiction';}
include 'connect.php';

if(strlen($query) > 1){
	$sql = 'SELECT * from movies WHERE movie_title LIKE "%'.$query.'%" LIMIT '.$index.','.$moviesAmount.'';
	$count = 'SELECT * from movies WHERE movie_title LIKE "%'.$query.'%" ';
} else if($random == 1){
	$sql = 'SELECT * from movies order by rand() LIMIT '.$moviesAmount.'';
	$count = 'SELECT * from movies order by rand() LIMIT '.$moviesAmount.'';
}
else{
	if($year == 'none'){
		$count = 'SELECT * from movies WHERE movie_genre LIKE "%'.$genre.'%"';
		if($action == 'ZA')				{$sql = 'SELECT * from movies WHERE movie_genre LIKE "%'.$genre.'%" ORDER BY movie_title DESC LIMIT '.$index.','.$moviesAmount.'';}
		elseif($action == 'AZ')			{$sql = 'SELECT * from movies WHERE movie_genre LIKE "%'.$genre.'%" ORDER BY movie_title ASC LIMIT '.$index.','.$moviesAmount.'';}
		elseif($action == 'imdbd')		{$sql = 'SELECT * from movies WHERE movie_genre LIKE "%'.$genre.'%" ORDER BY movie_rating ASC LIMIT '.$index.','.$moviesAmount.'';}
		else 							{$sql = 'SELECT * from movies WHERE movie_genre LIKE "%'.$genre.'%" ORDER BY id DESC LIMIT '.$index.','.$moviesAmount.'';}
	} elseif($genre == 'none'){
		$count = 'SELECT * from movies WHERE movie_genre LIKE "%'.$year.'%"';
		if($action == 'ZA')				{$sql = 'SELECT * from movies WHERE movie_release_year LIKE "%'.$year.'%" ORDER BY movie_title DESC LIMIT '.$index.','.$moviesAmount.'';}
		elseif($action == 'AZ')			{$sql = 'SELECT * from movies WHERE movie_release_year LIKE "%'.$year.'%" ORDER BY movie_title ASC LIMIT '.$index.','.$moviesAmount.'';}
		elseif($action == 'imdbd')		{$sql = 'SELECT * from movies WHERE movie_release_year LIKE "%'.$year.'%" ORDER BY movie_rating ASC LIMIT '.$index.','.$moviesAmount.'';}
		else 							{$sql = 'SELECT * from movies WHERE movie_release_year LIKE "%'.$year.'%" ORDER BY id DESC LIMIT '.$index.','.$moviesAmount.'';}
	}
}
	

$result = mysqli_query($conn,$sql);
$resultCount = mysqli_query($conn,$count);
$allResult = array('all_result' => mysqli_num_rows($resultCount));
$arr['all_result'] = mysqli_num_rows($resultCount);
$arr['query'] = $query;
$arr['genre'] = $genre;
$arr['year'] = $year;
$arr['sql'] = $sql;
$count = 0;
while($row = mysqli_fetch_assoc($result)) {
	if(mysqli_num_rows($result) > 0) {
		$count += 1;
		$data = array('id' => $row['id'], 'movie_image' => $row['movie_id'] + '.jpg' , 'movie_title' => mb_convert_encoding($row['movie_title'], 'UTF-8', 'UTF-8') , 'movie_genre' => $row['movie_genre']);
		$arr[] = $data;
	}
}

$arr[] = $allResult;

echo json_encode($arr,JSON_FORCE_OBJECT);
mysqli_close($conn);



if ($_POST['random']){
	$random = $_POST['random'];
}
*/


include 'connect.php';

$page = $_GET['page'];
$index = ($page - 1) * 36;

if (isset($_GET['genre'])){
	$genre = $_GET['genre'];
	$sql = "SELECT * from movies WHERE movie_genre LIKE '%" . $genre . "%' ORDER BY id ASC LIMIT ".$index." , ". 36 ."";
}	elseif (isset($_GET['year']))	{
	$year = $_GET['year'];
	$sql = "SELECT * from movies WHERE movie_released LIKE '%" . $year . "%' ORDER BY id ASC LIMIT ".$index." , ". 36 ."";
}


$result = mysqli_query($conn,$sql);
while ($row = mysqli_fetch_assoc($result)) {
	if (mysqli_num_rows($result) > 0) {
		echo "<a class='movieRef' href='/Movie/" . $row['id'] . "'>";
		echo "	<div class='movie'>";
		echo "		<img src='/Cool/movieImages_med/" . $row['movie_id'] . ".jpg' alt='" .$row['movie_title'] . "' class='movieImage lazyload' />";
		echo "		<div class='link'></div>";
		echo "		<div class='caption' id='capt'>";
		echo "			<h2 class='capTitle'>" . $row['movie_title'] . "</h2>";
		echo "			<h3 class='capGenre'>" . $row['movie_genre'] . "</h2>";
		echo "		</div>";
		echo "	</div>";
		echo "</a>";

	}
}
mysqli_close($conn);



?>