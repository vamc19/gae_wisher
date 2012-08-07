$(function(){
  var lightswitch = $("#switch");
  var lightbulb = $("#bulb");
  var container = $("#container");

  lightswitch.click(function(){
    if (lightbulb.hasClass("off")){
      lightbulb.removeClass("off");
      lightswitch.css("backgroundPosition", "0 0");
      lightbulb.css("backgroundPosition", "0 0");
      container.css({background: '-webkit-gradient(radial, 50% 30%, 0, 50% 30%, 700, from(#959047), to(#000000))'});
      container.css({background: '-moz-radial-gradient(circle, #959047, #000000)'});
      container.css({background: '-ms-radial-gradient(circle, #959047, #000000)'});
    }else{
      lightbulb.addClass("off");
      lightswitch.css("backgroundPosition", "-80 0");
      lightbulb.css("backgroundPosition", "-250 0");
      container.css({background: '#000000'});
      
      }
  });
});