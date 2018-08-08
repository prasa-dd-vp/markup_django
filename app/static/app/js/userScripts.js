function myFunction(data) {
	if(!data){
		document.getElementById("target").innerHTML = "";
	}
	else{	
	document.getElementById("target").innerHTML = data;
	}
}

$(document).ready(function(){
    $("#button1").click(function(){
		var para = $("#words").val();
		alert(para);
       
    });
	
	$("#words").on("input",function(){
		var para = $("#words").val();
		
			$.ajax({
				url: '/markup/',
				method: 'POST',
				data: {
				  'words': para
				},
				
				success: function (data) {
				  myFunction(data);  
				}
			  });
		
		
	});
});
