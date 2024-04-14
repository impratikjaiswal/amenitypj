const copy_button = document.querySelector("#process_copy_clipboard");

copy_button.addEventListener("click", copyToClipboard, false);
//copy_button.addEventListener("mouseout", copyToClipboardToolTip, false);
//copy_button.addEventListener("mousedown", logEvent);
//copy_button.addEventListener("mouseup", logEvent);
//copy_button.addEventListener("mouseenter", logEvent);
//copy_button.addEventListener("mouseleave", logEvent);

function alertMsg() {
    alert("Hello! I am an alert box!!");
}

function copyToClipboard(event) {
    event.preventDefault();
    let msg = "";
    // ID of the object, working fine with div
    const element = document.querySelector("#output_statement");
    // represents inner tags
    // let data_text_content = element.textContent
    // represents exactly how text appears on the page
    let data_inner_text = element.innerText
    navigator.clipboard.writeText(data_inner_text)

    //  var tooltip = document.getElementById("copy_clipboard_tool_tip");
    //  tooltip.innerHTML = "Text Copied";

    // Uncomment for Debugging
    //  msg += "preventDefault()!<br>";
    //  msg += "data_inner_text: " + data_inner_text + "<br>";
    //  msg += "data_text_content: " + data_text_content + "<br>";
    //  document.getElementById("debug_data").innerHTML += msg;
}


//function copyToClipboardToolTip() {
//  var tooltip = document.getElementById("copy_clipboard_tool_tip");
//  tooltip.innerHTML = "Copy to clipboard";
//}

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