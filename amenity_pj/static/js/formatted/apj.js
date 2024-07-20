const TIP_BUTTON_SWAP_IO = "Swap I/O Formats"
const TIP_BUTTON_COPY = "Copy to Clipboard"
const TIP_BUTTON_DOWNLOAD = "Download"
const TIP_BUTTON_COPY_SUCCESS = "Copied !!!"
const TIP_BUTTON_DOWNLOAD_SUCCESS = "Downloading !!!"
const TIP_BUTTON_COPY_EMPTY = "Nothing to Copy"
const TIP_BUTTON_DOWNLOAD_EMPTY = "Nothing to Download"

const btn_copy_input = document.querySelector("#copy_input_data");
const btn_copy_output = document.querySelector("#copy_output_data");
const btn_copy_info = document.querySelector("#copy_info_data");
const btn_download_output = document.querySelector("#download_output_data");

btn_copy_input.addEventListener("click", copyToClipboard, false);
btn_copy_input.source_field = "#input_data"
btn_copy_input.source_type = "textarea"

btn_copy_output.addEventListener("click", copyToClipboard, false);
btn_copy_output.source_field = "#output_statement"
btn_copy_output.source_type = "div"

btn_download_output.addEventListener("click", downloadData, false);
btn_download_output.source_field = "#output_statement"
btn_download_output.source_type = "div"

btn_copy_info.addEventListener("click", copyToClipboard, false);
btn_copy_info.source_field = "#info_statement"
btn_copy_info.source_type = "div"

//btn_copy_output.addEventListener("mouseout", copyToClipboardToolTip, false);
//btn_copy_output.addEventListener("mousedown", logEvent);
//btn_copy_output.addEventListener("mouseup", logEvent);
//btn_copy_output.addEventListener("mouseenter", logEvent);
//btn_copy_output.addEventListener("mouseleave", logEvent);

$(document).ready(function () {
    // debugData("DOM is ready: custom.js");
    pageLoad();
    $('#input_data').on('input', function () {
        // Attach an "input" event listener to input_data
        characterCounterInputData();
    });
    // navChangeActiveLinkOnClick();
    // navChangeActiveLinkOnScroll();
    // debugData("Done custom.js");
});

function htmlToJs(vars) {
    debugData(vars)
}

function pageLoad() {
    // debugData("pageLoad: custom.js");
    characterCounterInputData();
    characterCounterInfoData();
    characterCounterOutputData();
}

function characterCounterInputData() {
    $("#input_data_char_count").text($("#input_data").val().length);
}

function characterCounterInfoData() {
    const length_of_info_statement_initial_text = 14
    $("#info_data_char_count").text(($("#info_statement").text().length - length_of_info_statement_initial_text));
}

function characterCounterOutputData() {
    const length_of_output_statement_initial_text = 14
    $("#output_data_char_count").text(($("#output_statement").text().length - length_of_output_statement_initial_text));
}

function alertMsg() {
    alert("Hello! I am an alert box!!");
}

function debugData(msg, heading = "", div_ui = false, alert_user = false, append_mode = false) {
    const msg_label = "Debugging...";
    let previous = document.getElementById("debug_data").innerHTML
    if (!append_mode) {
        previous = "";
    }
    if (heading) {
        heading = heading + ": "
    }
    let content_curr = heading ? (heading + msg) : msg
    let content_prev = (heading && previous) ? previous.replace(heading, "") : previous
    let debug_msg_alert = [content_prev, content_curr].join("\n");
    let debug_msg_div = [content_prev, content_curr].join("<BR>");
    let console_log = content_curr
    console.log(console_log)
    if (div_ui) {
        document.getElementById("debug_data").innerHTML = debug_msg_div;
        document.getElementById("debug_data_label").innerHTML = msg_label;
    }
    if (alert_user) {
        alert(debug_msg_alert);
    }
}

/**
 *
 * @param event
 */
function copyToClipboard(event) {

    $(this).toggleClass("btn-image-rotate-y");
    event.preventDefault();
    let msg = "";
    let data_inner_text = getText(event)
    navigator.clipboard.writeText(data_inner_text)

    var tooltip = document.getElementById("copy_clipboard_tool_tip");
    tooltip.innerHTML = "";


    // Uncomment for Debugging
    //  msg += "preventDefault()!<br>";
    //  msg += "data_inner_text: " + data_inner_text + "<br>";
    //  msg += "data_text_content: " + data_text_content + "<br>";
    //  document.getElementById("debug_data").innerHTML += msg;
}

//const copyToClipboard = async () => {
//  try {
//    const element = document.querySelector(".user-select-all");
//    await navigator.clipboard.writeText(element.textContent);
//    console.log("Text copied to clipboard!");
//    // Optional: Display a success message to the user
//  } catch (error) {
//    console.error("Failed to copy to clipboard:", error);
//    // Optional: Display an error message to the user
//  }
//};

function navChangeActiveLinkOnClick() {
    // TODO: Not Working
    /* Code for changing active link on clicking */
    var btns = $("#navbarNav .navbar-nav .nav-item");
    for (let i = 0; i < btns.length; i++) {
        btns[i].addEventListener("click", function () {
            var current = document.getElementsByClassName("active");
            if (current.length > 0) {
                current[0].className = current[0].className.replace(" active", "");
            }
            this.className += " active";
        });
    }
}

function navChangeActiveLinkOnScroll() {
    // TODO: To validate
    /* Code for changing active link on Scrolling */
    $(window).scroll(function () {
        var distance = $(window).scrollTop();
        $('.page-section').each(function (i) {
            if ($(this).position().top <= distance + 250) {
                $('.navbar-nav a.active')
                    .removeClass('active');
                $('.navbar-nav a').eq(i)
                    .addClass('active');
            }
        });
    }).scroll();
}


/**
 *
 * @param files_format
 * @param native_only
 * @returns {*|string}
 */
function getTimeStamp(files_format = true, native_only = false) {
    // Target Format: _yyyymmdd_hhmmss_fff
    // Sample:        _20240719_094646_667
    if (native_only) {
        let stringDate = Date();
        // console.log(stringDate); // "Tue Aug 23 2022 14:47:12 GMT-0700 (Pacific Daylight Time)"
        let objDate = new Date();
        // console.log(objectDate); // Tue Aug 23 2022 14:47:12 GMT-0700 (Pacific Daylight Time)
        const formattedDate = `${objDate.getFullYear()}${objDate.getMonth()}${objDate.getDate()}_${objDate.getHours()}${objDate.getMinutes()}${objDate.getSeconds()}_${objDate.getMilliseconds()}`;
        return formattedDate
    } else {
        const formatNeeded = 'YYYYMMDD_HHmmss_SSS'
        return dayjs().format(formatNeeded)
    }
}

function getFileName() {
    let title_name = document.title
    let time_stamp_native = getTimeStamp(true, true)
    let time_stamp = getTimeStamp()
    // debugData(time_stamp, 'time_stamp')
    // debugData(time_stamp_native, 'time_stamp_native')
    return `${title_name}_${time_stamp}`.replace(" ", "_");
}

function downloadData(event) {
    $(this).toggleClass("btn-image-rotate-x");
    event.preventDefault();
    downloadDataActual(getFileName(), getText(event));
}

function downloadDataActual(file, text) {
    // Ref: https://www.geeksforgeeks.org/how-to-trigger-a-file-download-when-clicking-an-html-button-or-javascript/
    //creating an invisible element
    let element = document.createElement('a');
    element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
    element.setAttribute('download', file);
    document.body.appendChild(element);
    element.click();
    document.body.removeChild(element);
}

function getText(event) {
    let source_field = event.currentTarget.source_field
    let source_type = event.currentTarget.source_type
    let data_inner_text = "";
    if (source_type == "div") {
        // ID of the object
        const element = document.querySelector(source_field);
        // represents inner tags
        // let data_text_content = element.textContent
        // represents exactly how text appears on the page
        data_inner_text = element.innerText
    } else if (source_type == "textarea") {
        // ID of the object
        const element = $(source_field);
        data_inner_text = element.val()
    }
    return data_inner_text;
}