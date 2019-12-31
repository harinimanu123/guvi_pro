$(function(){
	$('button').click(function(){
		$.ajax({
			url: '/signedup',
			data: {
				firstname : $('#fname').val(),
				lastname : $('#lname').val(),
				mail: $('#mail').val(),
				dob: $('#date').val(),
				mobile1: $('#mob1').val(),
				mobile2: $('#mob2').val(),
				city : $('#city').val(),
				password: $('#password').val()
			},
			type: 'POST',
			success: function(response){
				alert("Successfully submitted");
			},
			error: function(error){
				alert(error);
			}
		});
	});
});

