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