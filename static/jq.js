

$(document).ready(function(){
    $("#btn-block").click(function(){
      if ($('select.form-control').children('option:selected').val()!=-1){
        
      $('#welcome-box').hide();
      $('#container').show();
      }
      else{
        $('.form-control').css('border-color','red');
        alert('Please Select one of the below Language !!');
      }
      
    });


    jQuery.fn.liScroll = function(settings) {
        settings = jQuery.extend({
            travelocity: 0.03
            }, settings);		
            return this.each(function(){
                    var $strip = jQuery(this);
                    $strip.addClass("newsticker")
                    var stripHeight = 1;
                    $strip.find("li").each(function(i){
                        stripHeight += jQuery(this, i).outerHeight(true); // thanks to Michael Haszprunar and Fabien Volpi
                    });
                    var $mask = $strip.wrap("<div class='mask'></div>");
                    var $tickercontainer = $strip.parent().wrap("<div class='tickercontainer'></div>");								
                    var containerHeight = $strip.parent().parent().height();	//a.k.a. 'mask' width 	
                    $strip.height(stripHeight);			
                    var totalTravel = stripHeight;
                    var defTiming = totalTravel/settings.travelocity;	// thanks to Scott Waye		
                    function scrollnews(spazio, tempo){
                    $strip.animate({top: '-='+ spazio}, tempo, "linear", function(){$strip.css("top", containerHeight); scrollnews(totalTravel, defTiming);});
                    }
                    scrollnews(totalTravel, defTiming);				
                    $strip.hover(function(){
                      jQuery(this).stop();
                    },
                    function(){
                      var offset = jQuery(this).offset();
                      var residualSpace = offset.top + stripHeight;
                      var residualTime = residualSpace/settings.travelocity;
                      scrollnews(residualSpace, residualTime);
                    });			
            });	
    };
    
    $(function(){
        $("ul#ticker01").liScroll();
    });
    

    
  });

var slideIndex = 1;
function myFun(){
  plusSlides(1);
}
setInterval(myFun, 5000);
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
 
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  
  slides[slideIndex-1].style.display = "block";  
  
}

//****************************** */
