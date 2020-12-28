function addEmailToAirtable(theForm) {
  const data = {"Email": theForm.email.value};
  fetch("https://36077.wayscript.io/", {
    method: "POST",
    headers: new Headers({"Content-Type": "application/json"}),
    mode: "cors",
    body: JSON.stringify(data),
  }).then(resp => {
    if (resp.status === 500) {
      console.log("Oops! Invalid Email")
    } else {
      console.log("You're in! Valid Email")
    }
  });
}
