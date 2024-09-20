#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a request to the Star Wars API for the movie details
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body to JSON
  const filmData = JSON.parse(body);

  // Get the list of character URLs
  const characterUrls = filmData.characters;

  // For each character URL, make a request to get character details
  characterUrls.forEach((url) => {
    request(url, (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});

