#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the Movie ID is provided
if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

// Define the API URL for the specified movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make the request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch the movie. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Extract the characters array
  const characters = data.characters;

  // Function to fetch and print character names in order
  function fetchCharacterNames (index) {
    if (index >= characters.length) return;

    request(characters[index], (error, response, body) => {
      if (error) {
        console.error('Error making the request:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Failed to fetch the character. Status code: ${response.statusCode}`);
        return;
      }

      // Parse the character response body
      const character = JSON.parse(body);

      // Print the character name
      console.log(character.name);

      // Fetch the next character name
      fetchCharacterNames(index + 1);
    });
  }

  // Start fetching character names from the first character in the list
  fetchCharacterNames(0);
});
