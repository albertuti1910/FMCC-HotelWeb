document.addEventListener("DOMContentLoaded", function() {
  // Función para obtener los parámetros de la URL
  function getQueryParam(param) {
      let params = new URLSearchParams(window.location.search);
      return params.get(param);
  }

  // Función para hacer un scroll suave hacia el elemento
  function scrollToElement(element) {
      window.scrollTo({
          top: element.offsetTop + 200,  // Ajusta el valor para el desplazamiento que necesites
          behavior: 'smooth'
      });
  }

  // Obtener el valor del parámetro 'tab'
  let activeTab = getQueryParam('tab');

  if (activeTab) {
      // Remover la clase 'active' de todas las pestañas
      document.querySelectorAll('.tabs-nav a').forEach((tabLink) => {
          tabLink.classList.remove('active');
      });
      document.querySelectorAll('.tab-content').forEach((tabContent) => {
          tabContent.classList.remove('active', 'show');
      });

      // Agregar la clase 'active' a la pestaña correcta y mostrar su contenido
      let tabLink = document.querySelector(`a[data-tab='${activeTab}']`);
      let tabContent = document.querySelector(`[data-tab-content='${activeTab}']`);
      
      if (tabLink && tabContent) {
          tabLink.classList.add('active');
          tabContent.classList.add('active', 'show');

          // Hacer scroll suave hacia la sección de hotel-facilities
          let hotelFacilitiesSection = document.querySelector('#hotel-facilities');  // Asegúrate de que el id del contenedor de las instalaciones sea correcto
          if (hotelFacilitiesSection) {
              scrollToElement(hotelFacilitiesSection);
          }
      }
  }

  // Evento para manejar los clics en las pestañas y hacer scroll a hotel-facilities
  document.querySelectorAll('.tabs-nav a').forEach((tabLink) => {
      tabLink.addEventListener('click', function(event) {
          event.preventDefault(); // Evitar que la página salte
          let targetTab = tabLink.getAttribute('data-tab');

          // Remover la clase 'active' de todas las pestañas
          document.querySelectorAll('.tabs-nav a').forEach((tabLink) => {
              tabLink.classList.remove('active');
          });
          document.querySelectorAll('.tab-content').forEach((tabContent) => {
              tabContent.classList.remove('active', 'show');
          });

          // Agregar la clase 'active' a la pestaña clicada y mostrar su contenido
          tabLink.classList.add('active');
          let tabContent = document.querySelector(`[data-tab-content='${targetTab}']`);
          if (tabContent) {
              tabContent.classList.add('active', 'show');
          }

          // Hacer scroll suave hacia la sección de hotel-facilities
          let hotelFacilitiesSection = document.querySelector('#hotel-facilities');
          if (hotelFacilitiesSection) {
              scrollToElement(hotelFacilitiesSection);
          }
      });
  });
});
