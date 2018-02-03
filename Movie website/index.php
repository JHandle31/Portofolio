<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title> New Movie Watcher - NMW What should i watch?</title>
  <meta name="description" content="Newmovieswatcher is a place where you can find the right (new)movies to watch for when you really don't know what to watch or you just want to get the inspiration to watch movies.">
  <link rel="stylesheet" href="scripts/bootstrap/css/bootstrap.min.css">
  <script src="scripts/jquery.min.js" type="text/javascript"></script>
  <script src="scripts/lazyload/jquery.lazyload.min.js" type="text/javascript"></script>
  <script src="scripts/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="css/v2index.css">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
  <link rel='icon' type='image/png' href='http://www.newmoviewatcher.com/icon.png'>
  <script type="text/javascript">
    $(function() {
      $("img.lazyload").lazyload({
        threshold : 200,
        effect: 'fadeIn'
      });

  });
  </script>
  
  <?php include 'phpScripts/connect.php';?>
</head>
<body>
 <?php include 'navBar.php'; ?>



<section class='sec1'>
  <h1> A PLACE TO DISCOVER MOVIES </h1>
  <div class='IndexCon'>
    
      <?php
      $sql = 'SELECT * from movies LIMIT 10';
      $result = mysqli_query($conn,$sql);
      $counted = 0;

      while($row = mysqli_fetch_assoc($result)) {
        if(mysqli_num_rows($result) > 0) {
          if ($counted == 0){
            echo '<div class="SideBlock Part1">';
          } elseif ($counted == 4) {
            echo '</div><div class="MainBlock">';
          } elseif ($counted == 6) {
            echo '</div><div class="SideBlock Part2">';
          } elseif ($counted == 10) {
            echo '</div>';
          }

          $counted++;
          $title = str_replace(' ', '-', $row['movie_title']);
          echo '  <div class="movie">';
          echo '    <a href="/Movie/'.$row['id'].'/'.$title.'">';
          echo '    </a>';
          echo '      <h3>'.$row['movie_title'].'</h3>';
          echo '    <div class="overlay"></div>';
          if ($counted > 4 && $counted <= 6) {
            echo '    <img src="/Cool/Movie-backdrops-official/'. $row['movie_id'] . '_bdrop0.jpg' .'" alt="'. $row['movie_title'] .'"/>';
          } else {
            echo '    <img src="/Cool/movieImages_med/'. $row['movie_id'] . '.jpg' .'" alt="'. $row['movie_title'] .'"/>';
          }
          
          echo '  </div>';
        }
      }


      
    ?>
  </div>
</section>
<section class='sec2'>
  <h1> NOW IN THEATHER </h1>
  <div class='IndexCon'>
    <?php
      $sql = 'SELECT * from movies LIMIT 10';
      $result = mysqli_query($conn,$sql);
      $countedIT = 0;

      while($row = mysqli_fetch_assoc($result)) {
        if(mysqli_num_rows($result) > 0) {
          $countedIT++;
          $random = rand(0,3);
          if($countedIT == 1){
            echo '<div class="PartL">';
          }
          elseif($countedIT == 6){
            echo '</div><div class="PartR">';
          }
          switch ($random) {
            case 0:
              echo "<div class='inTh'>";
              echo "  <div class='movie-block'>";
              echo "    <div class='item poster'><img class='lazyload' src='/Cool/movieImages_med/" . $row['movie_id'] . '.jpg' . "' alt='" . $row['movie_title'] . " poster'></div>";
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop0.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop1.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "    <div class='item text'><h2>" . $row['movie_title'] . "</h2></div>";
              echo "  </div>";
              echo "</div>";
              break;

            case 1:
              echo "<div class='inTh'>";
              echo "  <div class='movie-block'>";  
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop0.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "    <div class='item poster'><img class='lazyload' src='/Cool/movieImages_med/" . $row['movie_id'] . '.jpg' . "' alt='" . $row['movie_title'] . " poster'></div>";
              echo "    <div class='item text'><h2>" . $row['movie_title'] . "</h2></div>";
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop1.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "  </div>";
              echo "</div>";
              break;

            case 2:
              echo "<div class='inTh'>";
              echo "  <div class='movie-block'>";  
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop0.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "    <div class='item text'><h2>" . $row['movie_title'] . "</h2></div>";
              echo "    <div class='item poster'><img class='lazyload' src='/Cool/movieImages_med/" . $row['movie_id'] . '.jpg' . "' alt='" . $row['movie_title'] . " poster'></div>";
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop1.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "  </div>";
              echo "</div>";
              break;

            case 3:
              echo "<div class='inTh'>";
              echo "  <div class='movie-block'>";  
              echo "    <div class='item text'><h2>" . $row['movie_title'] . "</h2></div>";
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop0.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "    <div class='item screensh'><img class='lazyload' src='/Cool/Movie-backdrops-official/" . $row['movie_id'] . '_bdrop1.jpg' . "' alt='" . $row['movie_title'] . " backdrop'></div>  ";
              echo "    <div class='item poster'><img class='lazyload' src='/Cool/movieImages_med/" . $row['movie_id'] . '.jpg' . "' alt='" . $row['movie_title'] . " poster'></div>";
              echo "  </div>";
              echo "</div>";
              break;
          }
        }
      }
      echo '</div>';
      
    ?>
  </div>
</section>

</div>
<script src="scripts/v2index.js"></script>
<script src="scripts/indexMovies.js" type="text/javascript"></script>
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-97596193-1', 'auto');
  ga('send', 'pageview');
</script>
<?php include 'footer.php'; ?>
</body>
</html>

<script type="text/javascript">

function myFunction(){
  var genres = []
  var freq = {}
  $('#suggestion input:checked').each(function() {
    var list = $(this).attr('value').split(', ')
    list.forEach(function(v){genres.push(v)});
  });

  for (var amount in genres){
    freq[genres[amount]] = (freq[genres[amount]] || 0) +1;
    console.log(amount)
  }

  var items = Object.keys(freq).map(function(key){
    return [key, freq[key]];
  });

  items.sort(function(first,second){
    return second[1] - first[1];
  });
  console.log(items[0]);
}

</script>