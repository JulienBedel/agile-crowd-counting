$(document).click(function(e){
    getPosition(e); 
});

var pointSize = 3;

function getPosition(event){
    var rect = canvas.getBoundingClientRect();
    var x = event.clientX - rect.left;
    var y = event.clientY - rect.top;
       
    drawCoordinates(x,y);
}

function drawCoordinates(x,y){	
     var ctx = document.getElementById("canvas").getContext("2d");


     ctx.fillStyle = "#ff2626"; // Red color

   ctx.beginPath();
   ctx.arc(x, y, pointSize, 0, Math.PI * 2, true);
   ctx.fill();
}

function loadimage(){
    const canvas = document.getElementById("canvas")
    const context = canvas.getContext("2d")
    const img = new Image()
    img.src = "{{url_for('send_image',filename=image)}}"
    img.onload = () => {
        context.drawImage(img, 0, 0,700,500)
    }
}
        