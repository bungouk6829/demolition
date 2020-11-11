$(document).ready(function(){
  $('.main_menu>li').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','#528afa');
    $(this).find('ul').slideDown(100);
    $(this).find('ul').css('display','flex');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
    $(this).find('ul').slideUp(100);
  });
  $('.sub_menu>ul>li').hover(function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','#528afa');
  },function(){
    $(this).css('transition','.1s ease');
    $(this).css('color','white');
  });
});
