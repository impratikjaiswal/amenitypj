$(document).ready(function () {
    // alert("DOM is ready");
    $('#asn1_schemas').change(function () {
        // alert("asn1_schemas has been changed.");
        $.getJSON('/asn1Play/asn1Objects', {
            selected_asn1_schema_js: $('#asn1_schemas').val()
        }).done(function (data) {
            // let msg = "";
            // msg = data.html_string_selected;
            // document.getElementById("debug_data").innerHTML += msg;
            $('#asn1_objects').html(data.html_string_selected);
        })
    });
    $('#process_input').bind('click', function () {
        $.getJSON('/_process_data', {
            selected_asn1_schema_js: $('#asn1_schemas').val(),
            selected_asn1_object_js: $('#asn1_objects').val(),
        }).success(function (data) {
            $('#debug_data').text(data.random_text);
        })
        return false;
    });
});