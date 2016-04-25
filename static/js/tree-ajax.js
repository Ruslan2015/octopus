$(document).ready(function(){
	$(".tree_node").click(function(){
		var catid; 
		var href;
		var change;
		catid = $(this).attr("data-catid");
		href = "/tree/show_node_context/";
		change = "#node_context";
		$.get(href, {node_id: catid}, function (data)
				{$(change).html(data);
		});			
	});
	
	$(".edit_node").click(function(){
		var todo; 
		todo = $(this).attr("todo");
		if(todo == "add_love")
			{
				href = "/tree/show_node_context/";
				change = "#node_context";
				var catid = 13;
				$.get(href, {node_id: catid}, function (data)
						{$(change).html(data);
				});	
			}
				
	});
});