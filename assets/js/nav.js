$(document).ready(function(){
  var scroll_start = 0;
  var startchange = $('.container-fluid');
  var offset = startchange.offset();
    if (startchange.length){
  $(document).scroll(function(){
    scroll_start = $(this).scrollTop();
    if(scroll_start >= offset.top) {
      $('#grad1').css('background', 'rgba(255,255,255,0.9)');
      $('#nav_rt').css('color', '#000000');
      $('.nav-link, h6').css('color', '#000000');
      $('.navbar-brand').css('color', '#000000');
      $('.nav-link.active').css('color', '#EB7C79');

    } else {
      $('#grad1').css('background', 'rgba(0,0,0,0)');
      $('#nav_rt').css('color', 'rgba(255,255,255,0.7)');
      $('.nav-link, h6').css('color', 'rgba(255,255,255,0.7)');
      $('.navbar-brand').css('color', 'rgba(255,255,255,0.7)');
      $('.nav-link.active').css('color', '#EB7C79');
    }
  });

    }
});
$(".main").onepage_scroll();
