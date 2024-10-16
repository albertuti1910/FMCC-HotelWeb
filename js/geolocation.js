function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError);
  } else {
    alert("Geolocalización no es soportada por este navegador.");
  }
}

function showPosition(position) {
  const lat = position.coords.latitude;
  const lon = position.coords.longitude;
  document.getElementById("location-info").innerHTML = `Latitud: ${lat} <br> Longitud: ${lon}`;
}

function showError(error) {
  switch (error.code) {
    case error.PERMISSION_DENIED:
      alert("Permiso de geolocalización denegado.");
      break;
    case error.POSITION_UNAVAILABLE:
      alert("Información de ubicación no disponible.");
      break;
    case error.TIMEOUT:
      alert("La solicitud de ubicación ha caducado.");
      break;
    case error.UNKNOWN_ERROR:
      alert("Ocurrió un error desconocido.");
      break;
  }
}
