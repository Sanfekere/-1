function searchURL() {
    var a = document.getElementById("izvelnee").value;

    if (a === "celsiums") {
        convertToF()
    } else {
        convertToC()
    }
}



function convertToC() {
    var fTempVal = parseFloat(document.getElementById('a').value);
var cTempVal = (fTempVal - 32) * (5/9);
document.getElementById('rezultats').value = cTempVal;
}

function convertToF() {
var cTempVal = parseFloat(document.getElementById('a').value);
var fTempVal = (cTempVal * (9/5)) + 32;
document.getElementById('rezultats').value = fTempVal;
}