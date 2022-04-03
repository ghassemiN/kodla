(function($) {
  
  "use strict";  

  $(window).on('load', function() {

  /*Page Loader active
  ========================================================*/
  $('#preloader').fadeOut();

    /* Back Top Link active
    ========================================================*/
      var offset = 200;
      var duration = 500;
      $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
          $('.back-to-top').fadeIn(400);
        } else {
          $('.back-to-top').fadeOut(400);
        }
      });

      $('.back-to-top').on('click',function(event) {
        event.preventDefault();
        $('html, body').animate({
          scrollTop: 0
        }, 600);
        return false;
      });

  });

  $("#kodla").submit(function(e){
    e.preventDefault();
    var data = {
		my_word:  $(this).find("input[name=words]").val()
    }
	$(".audio-player").hide();
	$(".kodla-text").text('');
	$("#waiting").show();
    $.ajax({
        type:'POST',
        url:'/api',
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(data),
        success:function(data){
			$(".audio-player").show();
            $("#kodla-player").attr("src", data.audio_file_path);
            $(".kodla-text").text( data.coded_string );
			var context = document.querySelector(".kodla-text");
			var instance = new Mark(context);
			instance.mark("TİRE");
			instance.mark("ALT TİRE");
			instance.mark("BOŞLUK");
        },
        error:function(data){
          alert(data.responseJSON.message);
        },
		complete:function(){
			$("#waiting").hide();
		}
    });
});


}(jQuery));
