/*
 * テキストエディタと，ソースの送受信，答え合わせ
 */
$(function() {
		$.getScript("https://cdnjs.cloudflare.com/ajax/libs/ace/1.2.0/ace.js");
		var editor = ace.edit("editor");
		editor.setTheme("ace/theme/monokai");
		editor.setFontSize(14);
		editor.getSession().setMode("ace/mode/python");
		editor.getSession().setUseWrapMode(true);
		editor.getSession().setTabSize(2);

		$('#judge').click(function () {alert("let's judge!")});

		function my_func() {
				var src = editor.getValue();
				var id = '0';
				var send_data = {id:id, src:src};
				
				$.ajax({
						contentType: 'application/json',
						type: 'POST',
						url: "/answer/",
						data: JSON.stringify(send_data),
						success: function(responce_data) {
						alert(responce_data);
								console.log(responce_data);
								
								if (responce_data['user_problem_ans'] == true) {
										alert("responce: true");
								} else {
										alert("responce: false");
								}
						},
						dataType: "json"
				});

		}
 });
