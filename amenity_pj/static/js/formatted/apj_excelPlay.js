$(document).ready(function () {
    // debugData("DOM is ready: apj_excelPlay.js");
    pageLoad_excelPlay();
    $('#process_input').click(function () {
        debugData("process_input has been clicked.");
        $.getJSON('/excelPlay/info', {}).done(function (data) {
            setTimeout(
                function () {
                    //do something special
                    $('#info_statement').text(data.html_string_selected);
                }, 1000);

        })
    });
    // debugData("Done apj_excelPlay.js");
});

function pageLoad_excelPlay() {
    // debugData("pageLoad: apj_excelPlay.js", alert_user=true);
}
