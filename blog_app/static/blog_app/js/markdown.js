function md_show(){

    $('#myModal').modal('show')

}
$(document).ready(function(){

  $("#but_submit").click(function(){
      md_show()


  });
});

function show_label(){

    /*
        文章标签
     */
    $("#add_label_val").hide()
    $("#add_label").click(function(){
        $("#add_label_val").show()
        $("#la_value").hide()
    });

    $("#add_label_val").blur(function(){
           var value_la = $(this).val();
            $(this).hide();
            $("#la_value").text(value_la).show()
    })

}

function show_class(){

    /*
        文章类别
    */
    // 隐藏输入框
    $("#add_value").hide()
    $("#add_class").click(function(){
        // 显示input标签
        $("#add_value").show()
        // 隐藏span标签
         $("#cl_value").hide()

    });

    $("#add_value").blur(function(){
        //获取input标签输入的值
        var values_cl = $(this).val();
        // 隐藏标签
        $(this).hide();
        // 把值显示在span标签上
        $("#cl_value").text(values_cl).show();
    });
}

$(document).ready(function(){

      // 调用show_label
      show_label();

      // 调用show_class
      show_class();


});

