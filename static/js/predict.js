
$("#predict_btn").click(function(){
    $.ajax({
    type:'POST',     
    url: '../../predict',
    

    success:function(res) {
      console.log($("#canvas").get(0).getContext('2d').toDataURL());
    },
    error:function(err) {
      console.log('Error: ' + err.status);
    }
})})