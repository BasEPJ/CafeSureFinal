
console.log("JavaScript cargado correctamente.");


//--------------------------FUNCIONES Y ALERTAS DEL CANJEO DE PUNTOS-------------------------

document.addEventListener('DOMContentLoaded', function() {
    // Obtener los elementos necesarios
    const puntosSpan = document.getElementById('puntos');
    const botonesCanjear = document.querySelectorAll('.canje-p button');

    // Función para canjear puntos
    function canjearPuntos(puntos) {
        // Obtener puntos actuales del usuario
        let puntosActuales = parseInt(puntosSpan.textContent);

        // Verificar si el usuario tiene suficientes puntos para canjear
        if (puntosActuales >= puntos) {
            // Restar los puntos canjeados
            puntosActuales = puntosActuales - puntos;
            // Actualizar puntos mostrados en la interfaz
            puntosSpan.textContent = puntosActuales;
            // Aquí puedes agregar la lógica para entregar el producto al usuario
            Swal.fire({
                title: "Canjeo efectivo!",
                text: "Disfruta de tu nuevo producto!",
                icon: "success"
              });
        } else {
            Swal.fire({
                icon: "error",
                title: "Oops...",
                text: "No tienes suficientes puntos :(",
              });
        }
    }

    // Agregar un event listener a cada botón de canje
    botonesCanjear.forEach(function(boton) {
        boton.addEventListener('click', function() {
            // Obtener los puntos del producto
            let puntosProducto = parseInt(this.parentNode.querySelector('.puntos').textContent);
            // Llamar a la función para canjear puntos
            canjearPuntos(puntosProducto);
        });
    });
});


