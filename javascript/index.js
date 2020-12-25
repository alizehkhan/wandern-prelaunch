var xmlHttp = new XMLHttpRequest();
var url = "https://api.airtable.com/v0/" + base +  "/Emails/";
var propValue = {
  "records": [
    {
      "fields": {
        "Email": email
      }
    }
  ]
};

xmlHttp.open('POST', url, true);
xmlHttp.setRequestHeader('Content-type', 'application/json');
xmlHttp.setRequestHeader('Authorization', "Bearer " + KEY);

xmlHttp.onreadystatechange = function() {
  if(xmlHttp.readyState == 4 && xmlHttp.status == 200) {
    console.log(xmlHttp.responseText);
  }
  console.log(xmlHttp.status)
};

xmlHttp.send(JSON.stringify(propValue));

console.log(xmlHttp);
