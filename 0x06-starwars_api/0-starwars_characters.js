#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.log('Erreur: Utilisez ce format: ./0-starwars_characters.js <ID du film>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const fetchFromApi = (url) => {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
};

const displayCharacters = async () => {
  try {
    const filmDetails = await fetchFromApi(apiUrl);
    const characterEndpoints = filmDetails.characters;

    for (let endpoint of characterEndpoints) {
      const characterDetails = await fetchFromApi(endpoint);
      console.log(characterDetails.name);
    }
  } catch (error) {
    console.error('Erreur lors de la récupération:', error);
  }
};

displayCharacters();
