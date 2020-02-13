$('document').ready(function(){
	

		  $.ajax({
			url: "{% url 'getmypoint' %}",
		  type: "GET",
			dataType:'json',
 		  }).done(function( responce ) {
			  var status = responce.status;
			  
			  $('.alert').hide();
			  
			 if(status == '1'){
				   
				  
				  $(".points").html(responce.points)
			  }else{
				  
			  }
			  
		   // $('#successmsg').html('<strong>Success! Data saved successfully.');
		   // $("#successmsgdiv").fadeTo(3000, 500).slideUp(500, function() {
		    //  $("#successmsgdiv").slideUp(500);
		    })
			
			
			
			 $.ajax({
			url: '/getmynickname/',
		    type: "GET",
			dataType:'json',
 		  }).done(function( responce ) {
			  var status = responce.status;
			  
			  $('.alert').hide();
			  
			 if(status == '1'){
				   
				 
				  $("#nickname").val(responce.nickname)
			  }else{
				  
			  }
			  
		   // $('#successmsg').html('<strong>Success! Data saved successfully.');
		   // $("#successmsgdiv").fadeTo(3000, 500).slideUp(500, function() {
		    //  $("#successmsgdiv").slideUp(500);
		    })
		   
		   
		   
		   	// nickname submit start here 
	$( "#nicksave" ).submit(function( event ) {
	
		  event.preventDefault();
		  var nickname = $('#nickname').val();
 		 
		  $.ajax({
			url: '/updatenickname/',
		    type: "GET",
			dataType:'json',
		   data: {  nickname: nickname}
		  }).done(function( responce ) {
			  var status = responce.status;
			  
			  $('.alert').hide();
			  
			 if(status == '0'){
				  var message = responce.message;
				  $('#alertdiv').show();
				  $('#errmsg').text(message);
			  }else{
				  var message = responce.message;
				  $('#successdiv').show();
				  $('#successmsg').text(message);
				  
					var delay = 2000; 
					var url = '/dashboard/';
				  
				  setTimeout(function(){ window.location = url; }, delay);
			  }
			  
		   // $('#successmsg').html('<strong>Success! Data saved successfully.');
		   // $("#successmsgdiv").fadeTo(3000, 500).slideUp(500, function() {
		    //  $("#successmsgdiv").slideUp(500);
		    })
		  });
		   
		   // submit nickname end here 

		});