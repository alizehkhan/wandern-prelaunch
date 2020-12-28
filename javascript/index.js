function addEmailToAirtable(theForm) {
  document.getElementById("email").style.cursor = "progress";

  const data = {"Email": theForm.email.value};
  fetch("https://36077.wayscript.io/", {
    method: "POST",
    headers: new Headers({"Content-Type": "application/json"}),
    mode: "cors",
    body: JSON.stringify(data),
  }).then(resp => {
    if (resp.status === 200) {
      console.log("You're in!")
    } else {
      console.log("Oops! Something went wrong")
    }
    document.getElementById("email").value = "";
    document.getElementById("email").style.cursor = "";
  });
}
