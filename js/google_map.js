var google;

function init() {
    // Coordenadas del Hotel Riu Palace Maspalomas
    var myLatlng = new google.maps.LatLng(27.7428591, -15.5787575);
    
    var mapOptions = {
        // Zoom inicial
        zoom: 15,

        // Centro del mapa (Hotel Riu Palace Maspalomas)
        center: myLatlng,

        // Opciones adicionales del mapa
        scrollwheel: false,
        styles: [
            {"featureType":"administrative.land_parcel","elementType":"all","stylers":[{"visibility":"off"}]},
            {"featureType":"landscape.man_made","elementType":"all","stylers":[{"visibility":"off"}]},
            {"featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]},
            {"featureType":"road","elementType":"labels","stylers":[{"visibility":"simplified"},{"lightness":20}]},
            {"featureType":"road.highway","elementType":"geometry","stylers":[{"hue":"#f49935"}]},
            {"featureType":"road.highway","elementType":"labels","stylers":[{"visibility":"simplified"}]},
            {"featureType":"road.arterial","elementType":"geometry","stylers":[{"hue":"#fad959"}]},
            {"featureType":"road.arterial","elementType":"labels","stylers":[{"visibility":"off"}]},
            {"featureType":"road.local","elementType":"geometry","stylers":[{"visibility":"simplified"}]},
            {"featureType":"road.local","elementType":"labels","stylers":[{"visibility":"simplified"}]},
            {"featureType":"transit","elementType":"all","stylers":[{"visibility":"off"}]},
            {"featureType":"water","elementType":"all","stylers":[{"hue":"#a1cdfc"},{"saturation":30},{"lightness":49}]}
        ]
    };

    // Obtén el elemento DOM para el mapa
    var mapElement = document.getElementById('map');

    // Crear el mapa de Google con las opciones anteriores
    var map = new google.maps.Map(mapElement, mapOptions);
    
    // Añadir un marcador en la ubicación del hotel
    new google.maps.Marker({
        position: myLatlng,
        map: map,
        icon: 'images/loc.png' // Cambia esto por la URL del ícono que prefieras o quítalo si no tienes uno
    });
}

// Inicializa el mapa cuando la ventana carga
google.maps.event.addDomListener(window, 'load', init);
