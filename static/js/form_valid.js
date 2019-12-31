$('#fname').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#password').val() != "" && $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});


$('#lname').on('keyup', function () {
	if ($('#fname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#password').val() != "" && $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});


$('#mail').on('keyup', function () {
	if ($('#lname').val() != "" && $('#fname').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#password').val() != ""&& $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});


$('#dob').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#fname').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#password').val() != ""&& $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});


$('#mob1').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#fname').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#password').val() != ""&& $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});


$('#mob2').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#fname').val() != "" && $('#city').val() != "" && $('#password').val() != ""&& $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});


$('#city').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#fname').val() != "" && $('#password').val() != ""&& $('#confirm_password').val() != "") {
		$('#sub').show();
	}
	else {
		$('#sub').hide();	
	}
});



$('#password').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#fname').val() != "" ) {
		var pwd = $('#password').val()
		if (pwd.length > 8 && pwd.match(/[a-z]/) && pwd.match(/[A-Z]/) && pwd.match(/\d/) && pwd.match(/[~!@#$%^&*()]/)) {
			$('#mm').html('Password Strength : Strong').css('color', 'green').show();
		}
		else if (pwd.length > 8 && pwd.match(/[a-z]/) && pwd.match(/[A-Z]/) && pwd.match(/\d/)) {
			$('#mm').html('Password Strength : Good').css('color', 'green').show();
		}
		else if (pwd.length > 8 && pwd.match(/[a-z]/) && pwd.match(/[A-Z]/)) {
			$('#mm').html('Password Strength : Weak').css('color', 'red').show();
			$('#mn').html('Requires numbers and special character').css('color', 'red').show();
		}
		else {
			$('#mm').html('Requires atleast 8 characters, capital letters, numbers and special character').css('color', 'red').show();	
		}
	}
	else {
		$('#sub').hide();	
	}
});


$('#confirm_password').on('keyup', function () {
	if ($('#lname').val() != "" && $('#mail').val() != "" && $('#dob').val() != "" && $('#mob1').val() != "" && $('#mob2').val() != "" && $('#city').val() != "" && $('#password').val() != ""&& $('fname').val() != "") {
	  	
	  	if ($('#password').val() == $('#confirm_password').val()) {
	    	$('#message').html('MATCHING').css('color', 'green').show();
    		$('#sub').show();
  		} 
  		else {
    		$('#message').html('NOT MATCHING').css('color', 'red');
    		$('#sub').hide();
  		}

	}
	else {
		$('#sub').hide();	
	}
});


