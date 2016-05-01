$(document).ready(function(){
	$(".tree_node").click(function(){
		var catid; 
		var href;
		var change;
		catid = $(this).attr("data-catid");
		href = "/tree/show_node_context/";
		
		$.get(href, {node_id: catid}, function (data)
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
	
	$(".edit_node").click(function(){
		var todo; 
		todo = $(this).attr("todo");
		if(todo == "add_love")
			{
				href = "/tree/add_love/";
				change = "#node_context";				
				$.get(href, function (data)
						{$(change).html(data);
				});	
			}
		if(todo == "add_node")
		{
			href = "/tree/add_node/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
		if(todo == "del_node")
		{
			href = "/tree/del_node/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
		if(todo == "level_up")
		{
			href = "/tree/level_up/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
		if(todo == "level_down")
		{
			href = "/tree/level_down/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
		if(todo == "edit_node")
		{
			href = "/tree/edit_node/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
		if(todo == "key_up")
		{
			href = "/tree/key_up/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
		if(todo == "key_down")
		{
			href = "/tree/key_down/";
			change = "#node_context";
			var catid = 13;
			$.get(href, {node_id: catid}, function (data)
					{$(change).html(data);
			});	
		}
				
	});
});