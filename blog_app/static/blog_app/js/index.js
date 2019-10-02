
$(document).ready(function () {

    $(".readmore").click(function () {
      $.post('/20/new',
    {
      name:"Donald Duck",
      city:"Duckburg",
      csrfmiddlewaretoken:'{{ csrf_token  }}'
    },
    function(data,status){
      alert("数据：" + data + "\n状态：" + status);
    });

    });

})
