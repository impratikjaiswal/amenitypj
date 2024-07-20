const btn_swap_input_output_format = document.querySelector("#swap_input_output_format");
btn_swap_input_output_format.addEventListener("click", swapInputOutputFormat, false);

$(document).ready(function () {
    // debugData("DOM is ready: apj_asn1Play.js");
    pageLoad_asn1Play();
    $('#asn1_schema').change(function () {
        // debugData("asn1_schema has been changed.");
        $.getJSON('/asn1Play/asn1Objects', {
            selected_asn1_schema_js: $(this).val(),
            selected_asn1_object_js: $('#asn1_object').val(),
        }).done(function (data) {
            $('#asn1_object').html(data.html_string_selected);
            $('#asn1_object').selectpicker('refresh');
        })
    });
    $('#process_re_parse_output').bind('click', function () {
        // debugData("process_re_parse_output is pressed.");
        swapInputOutputFormatActual();
        $("#input_data").val($('#output_statement').text());
    });
    // debugData("Done apj_asn1Play.js");
});

function pageLoad_asn1Play() {
    // debugData("pageLoad: apj_asn1Play.js");
}

function swapInputOutputFormat(event) {
    // debugData("swap_input_output_format is pressed.");
    $(this).toggleClass("btn-image-rotate");
    event.preventDefault();
    swapInputOutputFormatActual();
}

function swapInputOutputFormatActual() {
    const selected_input_format_js = $('#input_format').val()
    const selected_output_format_js = $('#output_format').val()
    // debugData("selected_input_format_js: " +  selected_input_format_js + "\nselected_output_format_js: " +  selected_output_format_js);
    $("#input_format").val(selected_output_format_js);
    $("#output_format").val(selected_input_format_js);
    $('#input_format').selectpicker('refresh');
    $('#output_format').selectpicker('refresh');
}