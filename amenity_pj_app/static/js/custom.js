const copy_button = document.querySelector("#process_copy_clipboard");

copy_button.addEventListener("click", copyToClipboard, false);

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
  // Uncomment for Debugging
//  msg += "preventDefault()!<br>";
//  msg += "data_inner_text: " + data_inner_text + "<br>";
//  msg += "data_text_content: " + data_text_content + "<br>";
//  document.getElementById("debug_data").innerHTML += msg;
  }

function alertMsg() {
    alert("Hello! I am an alert box!!");
}

