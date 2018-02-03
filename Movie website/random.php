<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="description" content="You can find the latest movies and backdrops here.">
  <title content='Good movies to watch'>New Movie Watcher - NMW</title>
  <link rel="stylesheet" href="/scripts/bootstrap/css/bootstrap.min.css">
  <script src="/scripts/jquery.min.js" type="text/javascript"></script>
  <script src="/scripts/lazyload/jquery.lazyload.min.js" type="text/javascript"></script>
  <script src="/scripts/bootstrap/js/bootstrap.min.js" type="text/javascript"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet">
  <script src="/scripts/getMovies.js"></script>
  <link rel='icon' type='image/png' href='http://www.newmoviewatcher.com/icon.png'>

  <link rel="stylesheet" href="/css/v2movies.css">
</head>
<body>
  <?php include 'navBar.php'; ?>

  <div class='movieBody'>
   <h2 style='width:100%; text-align: center;'> The best way to discover new good movies is to let is be a surprise! </h2>
  </div>
  <div class='paginationBody'>
    <div class="paginati">
    </div>
  </div>

  <script type="text/javascript">
    datab(0,1,'none','none',0,1);
  </script>
  <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'UA-97596193-1', 'auto');
    ga('send', 'pageview');

  </script>
  <script src="/scripts/v2index.js"></script>
  <script type="text/javascript">
    $('.caption').css({"display":'flex', "justify-content":"center","align-items":"center","height:":"100%"})
    $('.movie img').css('display','none');
    $('.capGenre').css('display','none');
    $('.caption h2').css('text-align','center');



  </script>
  <script src="/scripts/cards.js"></script>
  <?php include 'footer.php'; ?>
</body>
</html>

