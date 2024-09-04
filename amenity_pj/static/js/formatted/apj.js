const LENGTH_OF_INFO_STATEMENT_INITIAL_TEXT = 14
// const LENGTH_OF_OUTPUT_STATEMENT_INITIAL_TEXT = 14
const LENGTH_OF_OUTPUT_STATEMENT_INITIAL_TEXT = 30
const SOURCE_TYPE_TEXT_AREA = 2
const SOURCE_TYPE_TEXT = 3
const SOURCE_TYPE_DIV = 4
const SOURCE_TYPE_COMBO_BOX = 5
const MAX_FILE_SIZE = 1024 * 1024 * 2

const TIP_BUTTON_SWAP_IO = "Swap I/O Formats"
const TIP_BUTTON_COPY = "Copy to Clipboard"
const TIP_BUTTON_DOWNLOAD = "Download"
const TIP_BUTTON_COPY_SUCCESS = "Copied !!!"
const TIP_BUTTON_DOWNLOAD_SUCCESS = "Downloading !!!"
const TIP_BUTTON_COPY_EMPTY = "Nothing to Copy for now !!!"
const TIP_BUTTON_DOWNLOAD_EMPTY = "Nothing to Download for now !!!"
const TIP_BUTTON_UPLOAD_EMPTY = "Nothing to Upload for now !!!"
const TIP_BUTTON_FILE_SIZE_EXCEEDS = "File Size must be less than 2 MB !!!\n\nUploaded File Size is: "

const btn_copy_input = document.querySelector("#copy_input_data");
if (btn_copy_input) {
    btn_copy_input.addEventListener("click", copyToClipboard, false);
    btn_copy_input.source_field = "#input_data"
    btn_copy_input.source_anchor = "#copy_input_data_a"
    btn_copy_input.source_type = SOURCE_TYPE_TEXT_AREA
}

const btn_download_input = document.querySelector("#download_input_data");
if (btn_download_input) {
    btn_download_input.addEventListener("click", downloadData, false);
    btn_download_input.source_field = "#input_data"
    btn_download_input.source_type = SOURCE_TYPE_TEXT_AREA
    btn_download_input.file_name_keyword = "input_data"
}

const btn_copy_output = document.querySelector("#copy_output_data");
if (btn_copy_output) {
    btn_copy_output.addEventListener("click", copyToClipboard, false);
//btn_copy_output.addEventListener("mouseout", copyToClipboardToolTip, false);
//btn_copy_output.addEventListener("mousedown", logEvent);
//btn_copy_output.addEventListener("mouseup", logEvent);
//btn_copy_output.addEventListener("mouseenter", logEvent);
//btn_copy_output.addEventListener("mouseleave", logEvent);
    btn_copy_output.source_field = "#output_statement"
    btn_copy_output.source_type = SOURCE_TYPE_DIV
}

const btn_download_output = document.querySelector("#download_output_data");
if (btn_download_output) {
    btn_download_output.addEventListener("click", downloadData, false);
    btn_download_output.source_field = "#output_statement"
    btn_download_output.source_type = SOURCE_TYPE_DIV
    btn_download_output.file_name_keyword = "output_data"
}

const btn_copy_info = document.querySelector("#copy_info_data");
if (btn_copy_info) {
    btn_copy_info.addEventListener("click", copyToClipboard, false);
    btn_copy_info.source_field = "#info_statement"
    btn_copy_info.source_type = SOURCE_TYPE_DIV
}

const btn_download_info = document.querySelector("#download_info_data");
if (btn_download_info) {
    btn_download_info.addEventListener("click", downloadData, false);
    btn_download_info.source_field = "#info_statement"
    btn_download_info.source_type = SOURCE_TYPE_DIV
    btn_download_info.file_name_keyword = "info"
}

const btn_input_data_file = document.querySelector("#input_data_file");
if (btn_input_data_file) {
// Process every time the user selects a new file
    btn_input_data_file.addEventListener("change", upload_input_file, false);
}

const btn_copy_sample = document.querySelector("#copy_sample");
if (btn_copy_sample) {
    btn_copy_sample.addEventListener("click", copyToClipboard, false);
    btn_copy_sample.source_field = "#sample"
    btn_copy_sample.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_remarks = document.querySelector("#copy_remarks");
if (btn_copy_remarks) {
    btn_copy_remarks.addEventListener("click", copyToClipboard, false);
    btn_copy_remarks.source_field = "#remarks"
    btn_copy_remarks.source_type = SOURCE_TYPE_TEXT
}

const btn_copy_scale = document.querySelector("#copy_scale");
if (btn_copy_scale) {
    btn_copy_scale.addEventListener("click", copyToClipboard, false);
    btn_copy_scale.source_field = "#scale"
    btn_copy_scale.source_type = SOURCE_TYPE_TEXT
}

const btn_copy_qr_code_version = document.querySelector("#copy_qr_code_version");
if (btn_copy_qr_code_version) {
    btn_copy_qr_code_version.addEventListener("click", copyToClipboard, false);
    btn_copy_qr_code_version.source_field = "#qr_code_version"
    btn_copy_qr_code_version.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_image_format = document.querySelector("#copy_image_format");
if (btn_copy_image_format) {
    btn_copy_image_format.addEventListener("click", copyToClipboard, false);
    btn_copy_image_format.source_field = "#image_format"
    btn_copy_image_format.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_input_format = document.querySelector("#copy_input_format");
if (btn_copy_input_format) {
    btn_copy_input_format.addEventListener("click", copyToClipboard, false);
    btn_copy_input_format.source_field = "#input_format"
    btn_copy_input_format.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_url_time_out = document.querySelector("#copy_url_time_out");
if (btn_copy_url_time_out) {
    btn_copy_url_time_out.addEventListener("click", copyToClipboard, false);
    btn_copy_url_time_out.source_field = "#url_time_out"
    btn_copy_url_time_out.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_output_format = document.querySelector("#copy_output_format");
if (btn_copy_output_format) {
    btn_copy_output_format.addEventListener("click", copyToClipboard, false);
    btn_copy_output_format.source_field = "#output_format"
    btn_copy_output_format.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_asn1_schema = document.querySelector("#copy_asn1_schema");
if (btn_copy_asn1_schema) {
    btn_copy_asn1_schema.addEventListener("click", copyToClipboard, false);
    btn_copy_asn1_schema.source_field = "#asn1_schema"
    btn_copy_asn1_schema.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_asn1_object_alternate = document.querySelector("#copy_asn1_object_alternate");
if (btn_copy_asn1_object_alternate) {
    btn_copy_asn1_object_alternate.addEventListener("click", copyToClipboard, false);
    btn_copy_asn1_object_alternate.source_field = "#asn1_object_alternate"
    btn_copy_asn1_object_alternate.source_type = SOURCE_TYPE_COMBO_BOX
}

const btn_copy_asn1_object = document.querySelector("#copy_asn1_object");
if (btn_copy_asn1_object) {
    btn_copy_asn1_object.addEventListener("click", copyToClipboard, false);
    btn_copy_asn1_object.source_field = "#asn1_object"
    btn_copy_asn1_object.source_type = SOURCE_TYPE_COMBO_BOX
}

$(document).ready(function () {
    // debugData("DOM is ready: apj.js");
    $('[data-toggle="tooltip"]').tooltip();
    pageLoad();
    inputDataLines();
    outputDataLines();
    $('#input_data').on('input', function () {
        // Attach an "input" event listener to input_data
        characterCounterInputData();
    });
    // navChangeActiveLinkOnClick();
    // navChangeActiveLinkOnScroll();
    // debugData("Done apj.js");
});


// document.addEventListener('DOMContentLoaded', () => {
//     inputDataHandling()
// outputDataHandling();
// });


function htmlToJs(vars) {
    debugData(vars)
}

function pageLoad() {
    // debugData("pageLoad: apj.js");
    characterCounterInputData();
    characterCounterInfoData();
    characterCounterOutputData();
}

function characterCounterInputData() {
    if ($("#input_data").val()) {
        $("#input_data_char_count").text($("#input_data").val().length);
    }
}

function characterCounterInfoData() {
    $("#info_data_char_count").text(($("#info_statement").text().length - LENGTH_OF_INFO_STATEMENT_INITIAL_TEXT));
}

function characterCounterOutputData() {
    $("#output_data_char_count").text(($("#output_statement").text().length - LENGTH_OF_OUTPUT_STATEMENT_INITIAL_TEXT));
}

function alertMsg(msg = "Hello! I am an alert box!!") {
    alert("Amenity Pj: " + msg);
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
    let data_inner_text = getText(event)
    if (data_inner_text) {
        navigator.clipboard.writeText(data_inner_text)
    } else {
        alertMsg(TIP_BUTTON_COPY_EMPTY)
    }
    // let source_anchor = event.currentTarget.source_anchor
    // let field = $(source_anchor)
    // $(source_anchor).tooltip("option", "content", "Awesome title!");
    // Uncomment for Debugging
    // let msg = "";
    //  msg += "preventDefault()!<br>";
    //  msg += "data_inner_text: " + data_inner_text + "<br>";
    //  msg += "data_text_content: " + data_text_content + "<br>";
    //  document.getElementById("debug_data").innerHTML += msg;
}

/**
 *
 * @param event
 */
function downloadData(event) {
    $(this).toggleClass("btn-image-rotate-x");
    event.preventDefault();
    let data_inner_text = getText(event)
    if (data_inner_text) {
        downloadDataActual(getFileName(event.currentTarget.file_name_keyword), data_inner_text);
    } else {
        alertMsg(TIP_BUTTON_DOWNLOAD_EMPTY)
    }
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

function getFileName(file_name_keyword) {
    let title_name = document.title
    let time_stamp_native = getTimeStamp(true, true)
    let time_stamp = getTimeStamp()
    // debugData(time_stamp, 'time_stamp')
    // debugData(time_stamp_native, 'time_stamp_native')
    return `${title_name}_${file_name_keyword}_${time_stamp}`.replace(" ", "_");
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
    if (source_type === SOURCE_TYPE_DIV) {
        // ID of the object
        const element = document.querySelector(source_field);
        // represents inner tags
        // let data_text_content = element.textContent
        // represents exactly how text appears on the page
        data_inner_text = element.innerText
    } else if (source_type === SOURCE_TYPE_TEXT_AREA || source_type === SOURCE_TYPE_COMBO_BOX || source_type === SOURCE_TYPE_TEXT) {
        // ID of the object
        const element = $(source_field);
        data_inner_text = element.val()
    } else { // Unknown Source Type Handling
        // ID of the object
        const element = $(source_field);
        data_inner_text = element.val()
    }
    return data_inner_text;
}

function upload_input_file(event) {
    // event.target points to the input element
    $("#upload_input_data").toggleClass("btn-image-rotate-360");
    const selectedFile = event.target.files[0]
    if (!selectedFile) {
        return
    }
    let file_name = selectedFile.name
    // Sample file_size (bytes): 937
    let file_size = selectedFile.size
    // Sample file_type: "text/plain"
    let file_type = selectedFile.type
    if (file_size > MAX_FILE_SIZE) {
        let size_in_mb = (file_size / 1024 / 1024).toFixed(2)
        alertMsg(TIP_BUTTON_FILE_SIZE_EXCEEDS + size_in_mb + " MB")
        return
    }
    const reader = new FileReader()
    reader.onload = (event) => {
        let textContent = setText(event)
        if (textContent) {
            // console.log(`The content of ${file_name} is ${textContent}`)
            $("#input_data").val(textContent);
            characterCounterInputData();
        } else {
            alertMsg(TIP_BUTTON_UPLOAD_EMPTY)
        }
    }
    reader.onerror = (event) => {
        const error = event.target.error
        console.error(`Error occurred while reading ${file_name}`, error)
    }
    reader.readAsText(selectedFile)
    /*
    reader.onchange = () => console.log(reader.result) // closure
reader.onchange = (e) => console.log(e.target.result) // event target
reader.onchange = function() => console.log(this.result) // 'this'
     */
}

function setText(event) {
    // event.target points to the reader
    let textContent = event.target.result
    return textContent ? textContent.trim() : textContent
}

function inputDataLines() {
    const textarea = document.getElementById("input_data");
    const lineNumbersEle = document.getElementById('input_data_line_numbers');
    if (textarea == null) {
        return
    }
    const textareaStyles = window.getComputedStyle(textarea, null);
    [
        'fontFamily',
        'fontSize',
        'fontWeight',
        'letterSpacing',
        'lineHeight',
        'padding',
    ].forEach((property) => {
        lineNumbersEle.style[property] = textareaStyles[property];
    });

    const parseValue = (v) => v.endsWith('px') ? parseInt(v.slice(0, -2), 10) : 0;
    const font = `${textareaStyles.fontSize} ${textareaStyles.fontFamily}`;
    const paddingLeft = parseValue(textareaStyles.paddingLeft);
    const paddingRight = parseValue(textareaStyles.paddingRight);

    const canvas = document.createElement('canvas');
    const context = canvas.getContext('2d');
    context.font = font;

    const calculateNumLines = (str) => {
        const textareaWidth = textarea.getBoundingClientRect().width - paddingLeft - paddingRight;
        const words = str.split(' ');
        let lineCount = 0;
        let currentLine = '';
        for (let i = 0; i < words.length; i++) {
            const wordWidth = context.measureText(words[i] + ' ').width;
            const lineWidth = context.measureText(currentLine).width;

            if (lineWidth + wordWidth > textareaWidth) {
                lineCount++;
                currentLine = words[i] + ' ';
            } else {
                currentLine += words[i] + ' ';
            }
        }

        if (currentLine.trim() !== '') {
            lineCount++;
        }

        return lineCount;
    };

    const calculateLineNumbers = () => {
        const lines = textarea.value.split('\n');
        const numLines = lines.map((line) => calculateNumLines(line));

        let lineNumbers = [];
        let i = 1;
        while (numLines.length > 0) {
            const numLinesOfSentence = numLines.shift();
            lineNumbers.push(i);
            if (numLinesOfSentence > 1) {
                Array(numLinesOfSentence - 1)
                    .fill('')
                    .forEach((_) => lineNumbers.push(''));
            }
            i++;
        }

        return lineNumbers;
    };

    const displayLineNumbers = () => {
        const lineNumbers = calculateLineNumbers();
        lineNumbersEle.innerHTML = Array.from({
            length: lineNumbers.length
        }, (_, i) => `<div>${lineNumbers[i] || '&nbsp;'}</div>`).join('');
    };

    textarea.addEventListener('input', () => {
        displayLineNumbers();
    });

    displayLineNumbers();

    const ro = new ResizeObserver(() => {
        const rect = textarea.getBoundingClientRect();
        lineNumbersEle.style.height = `${rect.height}px`;
        displayLineNumbers();
    });
    ro.observe(textarea);

    textarea.addEventListener('scroll', () => {
        lineNumbersEle.scrollTop = textarea.scrollTop;
    });
}

function outputDataLines() {
    const textarea = document.getElementById('output_statement');
    const lineNumbersEle = document.getElementById('output_statement_line_numbers');
    if (textarea == null) {
        return
    }
    const displayLineNumbers = () => {
        const lines = textarea.innerText.split('\n');
        let lines_data = Array.from({
            length: lines.length,
        }, (_, i) => `${i + 1}`).join('\n');
        debugData(lines_data, heading = "lines_data")
        lineNumbersEle.innerHTML = "<pre>" + lines_data + "<pre>";
    }
    displayLineNumbers();
}