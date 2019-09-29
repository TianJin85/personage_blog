
$(document).ready(function () {

    $(".readmore").click(function () {
        $.post(this.href,
        {
          name:"Donald Duck",
          city:"Duckburg",
          csrfmiddlewaretoken:'{{ csrf_token  }}'
        },
        function(){
          window.location.href=this.href;
        });
    });

});
