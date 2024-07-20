$(document).ready(function () {
    // debugData("DOM is ready: custom_asn1Play.js");
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
    $('#swap_input_output_format').bind('click', function () {
        // debugData("swap_input_output_format is pressed.");
        swapInputOutputFormat();
        $(this).toggleClass("btn-image-rotate");
    });
    $('#process_re_parse_output').bind('click', function () {
        // debugData("process_re_parse_output is pressed.");
        swapInputOutputFormat();
        $("#input_data").val($('#output_statement').text());
    });
    // debugData("Done custom_asn1Play.js");
});

function pageLoad_asn1Play() {
    // debugData("pageLoad: custom_asn1Play.js");
}

function swapInputOutputFormat() {
    const selected_input_format_js = $('#input_format').val()
    const selected_output_format_js = $('#output_format').val()
    // debugData("selected_input_format_js: " +  selected_input_format_js + "\nselected_output_format_js: " +  selected_output_format_js);
    $("#input_format").val(selected_output_format_js);
    $("#output_format").val(selected_input_format_js);
    $('#input_format').selectpicker('refresh');
    $('#output_format').selectpicker('refresh');
}