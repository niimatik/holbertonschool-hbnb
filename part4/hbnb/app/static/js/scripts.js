#!usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  async function getPlaces() {
    try {
      const response = await fetch('/api/v1/places');
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

      const title = document.createElement('h3');
      title.className = 'place-title';
      title.textContent = place.title;
      card.appendChild(title);

      const price = document.createElement('p');
      price.className = 'place-price';
      price.textContent = place.price;
      card.appendChild(price);

      const button = document.createElement('button');
      button.className = 'details-button';
      button.textContent = 'View Details';
      card.appendChild(button);
      container.appendChild(card);
    });
  }
  getPlaces();
});
