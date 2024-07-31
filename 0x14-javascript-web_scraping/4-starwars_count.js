#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

// Character ID for Wedge Antilles
const wedgeAntillesId = '18';

// Make the request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error making the request:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch the API. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the response body
  const data = JSON.parse(body);

  // Check the number of movies where Wedge Antilles is present
  const wedgeMoviesCount = data.results.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)
  ).length;

  // Print the number of movies
  console.log(wedgeMoviesCount);
});
