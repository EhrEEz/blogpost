
$(document).ready(function(){
    $(window).bind('scroll', function() {
    var navHeight = $( window ).height() - 60;
          if ($(window).scrollTop() > navHeight) {
              $('#grad1').css('position', 'fixed');
              $("#grad1").css('bottom', '');
              $('#grad1').css('top', '0');
              $('#grad1').css('height', '60px');
              $('#grad1').css('z-index', '1000');
              $('#grad1').css('background', 'rgba(255,255,255,0.9)');
              $('#nav_rt').css('color', '#000000');
              $('.nav-link,#nav_rt h6').css('color', 'rgba(0,0,0,0.7)');
              $('.navbar-brand').css('color', 'rgba(0,0,0,0.7)');
              $('.nav-link.active').css('color', '#EB7C79');
              $('#search_input').css('color', 'rgba(0,0,0,0.7)');
          }
          else {
              $('#grad1').css('position', 'absolute');
              $("#grad1").css('top','');
              $('#grad1').css('bottom', '0');
              $('#grad1').css('height', '60px');
              $('#grad1').css('z-index', '1000');
              $('#grad1').css('background', 'rgba(0,0,0,0)');
              $('#nav_rt').css('color', 'rgba(255,255,255,0.7)');
              $('.nav-link,#nav_rt h6').css('color', 'rgba(255,255,255,0.7)');
              $('.navbar-brand').css('color', 'rgba(255,255,255,0.7)');
              $('.nav-link.active').css('color', '#EB7C79');
              $('#search_input').css('color', 'rgba(255,255,255,0.7)');
          }
     });
 });
