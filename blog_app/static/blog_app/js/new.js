$(document).ready(function () {
    hide_conmment_content()

    $("#font span").click(function () {
        show_conmment_content();
    });

});
function show_conmment_content() {
    $('#conmment-content').show();
}
function hide_conmment_content() {
    $('#conmment-content').hide();
}