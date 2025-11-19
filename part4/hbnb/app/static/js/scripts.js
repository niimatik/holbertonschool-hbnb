#!usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  async function getPlaces() {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/v1/places');
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

      const places = await response.json();
      renderPlaces(places);
    }
    catch (error) {
      console.error('Erreur lors de la récupération des places:', error);
    }
  }

  function renderPlaces(places) {
    const container = document.getElementById('places-list');
    container.innerHTML = '';

    places.forEach(place => {
      const card = document.createElement('div');
      card.className = 'place-card';

      const content = document.createElement('div');
      content.className = 'place-content';

      const title = document.createElement('h3');
      title.className = 'place-title';
      title.textContent = place.title;
      content.appendChild(title);

      const desc = document.createElement('p');
      desc.className = 'place-description';
      desc.textContent = place.description;
      content.appendChild(desc);

      const price = document.createElement('p');
      price.className = 'place-price';
      price.textContent = place.price;
      content.appendChild(price);
      container.appendChild(card);
    });
  }
  getPlaces();
});
