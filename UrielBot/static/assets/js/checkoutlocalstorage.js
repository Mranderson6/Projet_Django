$(document).ready(function(){
 

    $("#form").on("submit", function(e){
		//alert("garder les info");
		 			
		localStorage.setItem('name',  $("input[name=name]").val() );
		localStorage.setItem('surname',  $("input[name=surname]").val() );
 		localStorage.setItem('adress',   $("input[name=adress]").val() );
		localStorage.setItem('phone',  $("input[name=phone]").val() );
		localStorage.setItem('town',  $("input[name=town]").val() );
		localStorage.setItem('zip',  $("input[name=zip]").val() );
		localStorage.setItem('email',  $("input[name=email]").val() );
		localStorage.setItem('notes',  $("input[name=notes]").val() );
	})
	
	//alert("charger les info");
	$("input[name=name]").val( localStorage.getItem('name') )
	$("input[name=surname]").val( localStorage.getItem('surname') )
	$("input[name=adress]").val( localStorage.getItem('adress') )
	$("input[name=phone]").val( localStorage.getItem('phone') )
	$("input[name=email]").val( localStorage.getItem('email') )
	$("input[name=notes]").val( localStorage.getItem('notes') )
	$("input[name=zip]").val( localStorage.getItem('zip') )
	$("input[name=town]").val( localStorage.getItem('town') )
	
});