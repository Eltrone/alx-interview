#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

function requestApi(url) {
  return new Promise((resolve, reject) => {
    request(url, { json: true }, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function getCharacters() {
  try {
    const movieResponse = await requestApi(baseUrl);
    const charactersList = movieResponse.characters;

    for (const characterUrl of charactersList) {
      const characterInfo = await requestApi(characterUrl);
      console.log(characterInfo.name);
    }
  } catch (error) {
    console.error('Fetch Error:', error);
  }
}

getCharacters();
