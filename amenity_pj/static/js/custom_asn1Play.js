$(document).ready(function () {
    // debugData("DOM is ready");
    $('#asn1_schema').change(function () {
        // debugData("asn1_schema has been changed.");
        $.getJSON('/asn1Play/asn1Objects', {
            selected_asn1_schema_js: $('#asn1_schema').val(),
            selected_asn1_object_js: $('#asn1_object').val(),
        }).done(function (data) {
            $('#asn1_object').html(data.html_string_selected);
            $('#asn1_object').selectpicker('refresh');
        })
    });
    $('#swap_input_output_format').bind('click', function () {
        // debugData("swap_input_output_format is pressed.");
        swapInputOutputFormat();
    });
    $('#process_re_parse_output').bind('click', function () {
        // debugData("process_re_parse_output is pressed.");
        swapInputOutputFormat();
        $("#raw_data").val($('#output_statement').text());
    });
});

function swapInputOutputFormat() {
    const selected_input_format_js = $('#input_format').val()
    const selected_output_format_js = $('#output_format').val()
    // debugData("selected_input_format_js: " +  selected_input_format_js + "\nselected_output_format_js: " +  selected_output_format_js);
    $("#input_format").val(selected_output_format_js);
    $("#output_format").val(selected_input_format_js);
    $('#input_format').selectpicker('refresh');
    $('#output_format').selectpicker('refresh');
}

function debugData(msg, alert_user = true, clear_previous = true) {
    let msg_label = "Debugging...";
    let previous = document.getElementById("debug_data").innerHTML
    if (clear_previous) {
        previous = "";
    }
    let debug_msg_alert = [previous, msg].join("\n");
    let debug_msg_div = [previous, msg].join("<BR>");
    document.getElementById("debug_data").innerHTML = debug_msg_div;
    document.getElementById("debug_data_label").innerHTML = msg_label;
    if (alert_user) {
        alert(debug_msg_alert);
    }
}