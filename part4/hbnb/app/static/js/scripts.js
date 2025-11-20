#!usr/bin/node
document.addEventListener('DOMContentLoaded', () => {

  /*
  ───────────────────────────────
  SECTION : LISTE DES PLACES
  ───────────────────────────────
  */

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
      button.addEventListener('click', () => {
        window.location.href = `/place?id=${place.id}`;
      });
      card.appendChild(button);
      container.appendChild(card);
    });
  }

  async function getPlaceByID(placeid) {
    try {
      const response = await fetch(`/api/v1/places/${placeid}`);
      if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

      const place_detail = await response.json();
      renderPlaceDetail(place_detail);

    } catch (error) {
      console.error('Erreur lors de la récupération du place:', error);
    }
  }

  function renderPlaceDetail(place) {
    const container = document.getElementById('places-list');
    container.innerHTML = '';

    const detail = document.createElement('div');
    detail.className = 'place-details';

    const title = document.createElement('h3');
    title.textContent = place.title;
    detail.appendChild(title);

    const host = document.createElement('h4');
    host.textContent = `${place.owner.first_name} ${place.owner.last_name}`;
    detail.appendChild(host);

    const desc = document.createElement('p');
    desc.textContent = place.description;
    detail.appendChild(desc);

    const price = document.createElement('p');
    price.textContent = place.price;
    detail.appendChild(price);

    if (Array.isArray(place.amenities)) {
      const ul = document.createElement('ul');
      place.amenities.forEach(a => {
        const li = document.createElement('li');
        li.textContent = a;
        ul.appendChild(li);
      });
      detail.appendChild(ul);
    }

    container.appendChild(detail);
  }

  const params = new URLSearchParams(window.location.search);
  const id = params.get("id");

  if (id) {
    getPlaceByID(id);
  } else {
    getPlaces();
  }

  /*
  ───────────────────────────────
  SECTION : LOGIN
  ───────────────────────────────
  */

  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();

      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value.trim();

      if (!email || !password) {
        alert("Veuillez remplir tous les champs.");
        return;
      }

      try {
        const response = await fetch('/api/v1/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, password })
        });

        if (response.ok) {
          const data = await response.json();

          document.cookie = `token=${data.access_token}; path=/; samesite=lax`;

          alert("Connexion réussie !");
          window.location.href = '/index';
        } else {
          const err = await response.json().catch(() => ({}));
          alert(err.error || "Identifiants invalides.");
        }

      } catch (error) {
        alert("Erreur serveur : " + error.message);
      }
    });
  }
});
