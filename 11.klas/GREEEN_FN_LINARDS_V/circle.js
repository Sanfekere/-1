function drawCircle() {
    var canvas = document.getElementById('myCanvas');
    var ctx = canvas.getContext('2d');
    var radius = document.getElementById('radiusInput').value;
    
    ctx.clearRect(0, 0, canvas.width, canvas.height); 
    ctx.beginPath();
    ctx.arc(canvas.width/2, canvas.height/2, radius, 0, 2 * Math.PI);
    ctx.stroke();
  }