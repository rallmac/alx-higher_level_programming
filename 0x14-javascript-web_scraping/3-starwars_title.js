#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Check if the movie ID is provided
if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

// Define the URL with the given movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make the request to the Star Wars API
request(url, (error, response, body) => {
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

  // Print the title of the movie
  console.log(data.title);
});
