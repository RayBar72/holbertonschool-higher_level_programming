#!/usr/bin/node
/* Script prints the title of a Star Wars movie where the
    episode number matches a given integer.
*/

const axios = require('axios').default;
const starWars = 'https://swapi-api.hbtn.io/api/films/';
axios.get(starWars)
  .then(function (response) {
    const y = response.data.results[process.argv[2] - 1].characters;
    for (const x in y) {
      const ulriq = y[x];
      const minAxi = require('axios').default;
      minAxi.get(ulriq)
        .then(function (respuesta) {
          console.log(respuesta.data.name);
        });
    }
  })
  .catch(function (error) {
    console.log(error);
  });
