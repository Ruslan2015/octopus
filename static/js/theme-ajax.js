$(document).ready(function(){
	$(".theme_item").click(function(){
		var catid; 
		var href;
		var change;
		catid = $(this).attr("data-catid");
		href = "/themes/show_theme_active/";
		
		$.get(href, {theme_id: catid}, function (data)
				{
				console.log(data);
				json = eval("(" + data + ")");
				// alert(json.success)
				var obj = jQuery.parseJSON(data);
				alert(data);
				$("#node_context").html('Содержимое узла');
				$("#current_level").html('Текущий узел');
				
				});			
	});
});