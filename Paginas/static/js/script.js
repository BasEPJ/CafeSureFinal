


// Initialize and add the map
function initMap() {
  // The location you want to center the map on
  const coords = { lat: -39.809249, lng: -73.2580214 };

  // Create a new map centered on the specified coordinates
  const map = new google.maps.Map(document.getElementById('map'), {
    zoom: 17,
    center: coords,
  });

  // Optionally, add a marker to the map at the specified coordinates
  const marker = new google.maps.Marker({
    position: coords,
    map: map,
  });
}