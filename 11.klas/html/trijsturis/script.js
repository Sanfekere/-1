function searchURL() {
    var a = Number(document.getElementById("a").value);
    var b = Number(document.getElementById("b").value);
    var c = Number(document.getElementById("c").value);

    if (a + b > c && a + c > b && b + c > a) {
        document.getElementById("rezultats").innerHTML = "Rezultāts: " + "Trijsturis ir iespējams";
        rezult()
    } else {
        document.getElementById("rezultats").innerHTML = "Rezultāts: " + "Trijsturis nav iespējams";
        document.getElementById("laukums").innerHTML ="Laukums: " + "Trijsturis nav laukuma, jo tas ir nēiespējams";
    }
}


function  rezult() {
    var a = Number(document.getElementById("a").value);
    var b = Number(document.getElementById("b").value);
    var c = Number(document.getElementById("c").value);

    let s = (a + b + c) / 2;
    let area = Math.sqrt(s * ((s - a) * (s - b) * (s - c)));


    document.getElementById("laukums").innerHTML ="Laukums: " + area + " cm2";
}