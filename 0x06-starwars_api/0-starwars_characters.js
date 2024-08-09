#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, { json: true }, (err, res, body) => {
  if (err) { return console.log(err); }
  let characters = body.characters;
  characters.forEach(character => {
    request(character, { json: true }, (err, res, body) => {
      if (err) { return console.log(err); }
      console.log(body.name);
    });
  });
});
