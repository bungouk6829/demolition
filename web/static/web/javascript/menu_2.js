$(document).ready(function(){
  function change_color(selector){
    $(selector).css('color', 'white');
    $(selector).css('background', '#2a4ed4');
    $(selector).css('border-radius', '5px');
    $(selector).css('opacity', '0.7');
  }

  href = window.location.href.replace("http://127.0.0.1:8000/menu_2/","");

  if (href == "structure"){
    selector = '#content_menu > ul > a:nth-child(1) > li'
    change_color(selector);
  }
  else if (href == "asbestos"){
    selector = '#content_menu > ul > a:nth-child(2) > li'
    change_color(selector);
  }
  else if (href == "civil"){
    selector = '#content_menu > ul > a:nth-child(3) > li'
    change_color(selector);
  }
  else if (href == "waste"){
    selector = '#content_menu > ul > a:nth-child(4) > li'
    change_color(selector);
  }
  else if (href == "rental"){
    selector = '#content_menu > ul > a:nth-child(5) > li'
    change_color(selector);
  }
});
