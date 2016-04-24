$(document).ready(function(){
	
	$(".tree_node").click(function(){
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/tree/show_node_context/', {node_id: catid}, function(data){
				   // $('#node_context').html(data); 
		});
	});
});