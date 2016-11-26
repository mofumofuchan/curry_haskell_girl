
var src = "print('hello world');"
var id = '0';

var send_data = {id:id, src:src};

function my_func() {

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
};
