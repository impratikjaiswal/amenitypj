$(document).ready(function () {
    // alert("DOM is ready");
    $('#asn1_schema').change(function () {
        // alert("asn1_schema has been changed.");
        $.getJSON('/asn1Play/asn1Objects', {
            selected_asn1_schema_js: $('#asn1_schema').val(),
            selected_asn1_object_js: $('#asn1_object').val(),
        }).done(function (data) {
            // let msg = "";
            // msg = data.html_string_selected;
            // document.getElementById("debug_data").innerHTML += msg;
            $('#asn1_object').html(data.html_string_selected);
            $('#asn1_object').selectpicker('refresh');
        })
    });
    $('#swap_input_output_format').bind('click', function () {
        // alert("swap_input_output_format is pressed.");
        const selected_input_format_js = $('#input_format').val()
        const selected_output_format_js =  $('#output_format').val()
        // alert("selected_input_format_js: " +  selected_input_format_js + "\nselected_output_format_js: " +  selected_output_format_js);
        $("#input_format").val(selected_output_format_js);
        $("#output_format").val(selected_input_format_js);
        $('#input_format').selectpicker('refresh');
        $('#output_format').selectpicker('refresh');
    });
});