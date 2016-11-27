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

  var initSrc = $('#hint').html();
  editor.setValue(initSrc);

  $('#back').click(function() { location.href='/'; });
  $('#reset').click(function() {editor.setValue(initSrc)});
  $('#judge').click(function() {judgeSource();});

  function judgeSource() {
    var src = editor.getValue();
    var id = '1';
    var send_data = {quiz_id:id, src:src};
    
    $.ajax({
      contentType: 'application/json',
      type: 'POST',
      url: "/answer/",
      data: JSON.stringify(send_data),
      success: function(responce_data) {
	console.info('answer: ok');
	console.info(responce_data);

	
	document.getElementById("phrase").textContent = "HelloWorld";
	$(function(){
	  $('#glcanvas').hide();
	  $('#dance img').attr('src', "/static/img/correct.gif");  
	});
	/*
	  if (responce_data['user_problem_ans'] == true) {
	  document.getElementById("phrase").textContent = "HelloWorld";
	  $(function(){
	  $('#glcanvas').hide();
	  $('#dance img').attr('src', "/static/img/correct.gif");  
	  });
	  } else {
	  document.getElementById("phrase").textContent = "しっぱい・・・";
	  $(function(){
	  $('#glcanvas').hide();
	  $('#dance img').attr('src', "/static/img/incorrect.gif");  
	  });

	*/
      }
    },
	   dataType: "json"
	  });
}
  $.ajax({
    contentType: 'application/json',
    type: 'POST',
    url: "/story/",
    data: JSON.stringify({quiz_id:'1'}),
    success: function(responce_data) {
      console.info('answer: ok');
      console.info(responce_data);
      $('#story').html(responce_data['story']);
    },
    dataType: "json"
  });
 });
