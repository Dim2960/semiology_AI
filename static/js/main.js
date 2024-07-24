const mrc = document.getElementById("mrc");
const heart = document.getElementById("heart");
const diabete = document.getElementById("diabete");
const cancer = document.getElementById("cancer");
const liver = document.getElementById("liver");
const diseaseId = document.getElementById("diseaseId");



function updateValue() {
    let value = this.dattaset.value;
    diseaseId.setAttribute("value", value);
    console.log("updateValue");
}