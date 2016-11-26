/*
 * テキストエディタと，ソースの送受信，答え合わせ
 */
$(function() {
		var editor = ace.edit("editor");
		editor.setTheme("ace/theme/monokai");
		editor.setFontSize(14);
		editor.getSession().setMode("ace/mode/python");
		editor.getSession().setUseWrapMode(true);
		editor.getSession().setTabSize(2);

		var initSrc = 'if __name__ == "__main__":\n  print("Hello world")';
		editor.setValue(initSrc); 
		
		$('#back').click(function() {alert("back index pages")});
		$('#reset').click(function() {editor.setValue(initSrc)});
		$('#judge').click(function() {judgeSource();});

		function judgeSource() {
				var src = editor.getValue();
				var id = '0';
				var send_data = {id:id, src:src};

				// debug
				alert("ためすよ！");
				
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

				document.getElementById("dance").textContent = "評価したよ！";

		}
 });
