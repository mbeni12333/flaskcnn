var canvas = document.getElementById("canvas");
var ctx = canvas.getContext("2d");

$("#predict_btn").click(function(){
    var data = canvas.toDataURL("image/jpeg");
    data = data.substr(data.indexOf(',') + 1);
    $.ajax({
    type:'POST',     
    url: '../../predict',
    dataType:'json',
    contentType: 'application/json',
    data: JSON.stringify({"data":data}),

    success:function(res) {
      console.log(res)
    },
    error:function(err) {
      console.log('Error: ' + err.status);
    }
})})