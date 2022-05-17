#!/usr/bin/node
/* Script prints the title of a Star Wars movie where the
    episode number matches a given integer.
*/

const axios = require('axios').default;
const starWars = 'https://swapi-api.hbtn.io/api/films/';
axios.get(starWars)
  .then(function (response) {
    console.log(response.data.results.length)
    const xs = response.data.results[process.argv[2] - 1]
    console.log(xs)
  })
  .catch(function (error) {
    console.log(error);
  });
