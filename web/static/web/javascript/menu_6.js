$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

  href = window.location.href.replace("http://127.0.0.1:8000/menu_6/","");

  if (href == "notice"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }
  else if (href == "information"){
    selector = '#content_menu > ul > a:nth-child(2) > li'
    change_color(selector);
  }

});
