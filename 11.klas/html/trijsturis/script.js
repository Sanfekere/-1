function searchURL() {
    var a = Number(document.getElementById("a").value);
    var b = Number(document.getElementById("b").value);
    var c = Number(document.getElementById("c").value);

    if (a + b > c && a + c > b && b + c > a) {
        document.getElementById("rezultats").innerHTML = "Trijsturis ir iespējams";
    } else {
        document.getElementById("rezultats").innerHTML = "Trijsturis nav iespējams";
    }
}