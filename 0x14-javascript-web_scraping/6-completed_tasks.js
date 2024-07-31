#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Check if the API URL is provided
if (!apiUrl) {
  console.error('Please provide the API URL as the first argument.');
  process.exit(1);
}

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
  const todos = JSON.parse(body);

  // Create an object to store the count of completed tasks for each user
  const userCompletedTasks = {};

  // Iterate over the todos and count completed tasks for each user
  todos.forEach(todo => {
    if (todo.completed) {
      if (userCompletedTasks[todo.userId]) {
        userCompletedTasks[todo.userId]++;
      } else {
        userCompletedTasks[todo.userId] = 1;
      }
    }
  });

  // Print the result in the desired format
  console.log(userCompletedTasks);
});
