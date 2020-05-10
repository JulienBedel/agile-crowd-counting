window.addEventListener('load', loadImage2);

function loadImage2(){
    console.log("test2")
    const canvas = document.getElementById("canvas")
    const context = canvas.getContext("2d")
    const img = new Image()
    img.src = "{{url_for('main.show_image', filename=image.path)}}"
    img.onload = () => {
        console.log("test")
        context.drawImage(img, 0, 0,700,500)
    }
}