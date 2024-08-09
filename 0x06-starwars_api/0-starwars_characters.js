#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

const makeRequest = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body));
      }
    });
  });
};

const fetchCharacters = async () => {
  try {
    const movieData = await makeRequest(apiUrl);
    const characterUrls = movieData.characters;

    for (const url of characterUrls) {
      const characterData = await makeRequest(url);
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

fetchCharacters();
