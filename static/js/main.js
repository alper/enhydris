// ready, go
$(document).ready(function(){

	// give input type a label
	$("input[type='text'].label").each(function(){
		var defaultVal = $(this).attr("title");
		$(this).focus(function(){
			if ($(this).val() === defaultVal){
				$(this).removeClass("active").val("");
			}
		})
		.blur(function(){
			if ($(this).val() === ""){
				$(this).addClass("active").val(defaultVal);
			}
		})
		.blur().addClass("active");
	});
	
	// fancify logo
	$(".logo h1").lettering();

});