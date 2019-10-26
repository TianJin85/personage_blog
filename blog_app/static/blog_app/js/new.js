$(document).ready(function () {
    hide_conmment_content()

    $("#font span").click(function () {
        if ($('#conmment-content').hide()) {
            show_conmment_content();
        }
        if ($('#conmment-content').show()){
            hide_conmment_content();
        }

    });

});
function show_conmment_content() {
    $('#conmment-content').fadeIn();
}
function hide_conmment_content() {
    $('#conmment-content').hide();
}