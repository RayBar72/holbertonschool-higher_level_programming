#!/usr/bin/node
/* Script prints the title of a Star Wars movie where the
    episode number matches a given integer.
*/

const axios = require('axios').default;
const starWars = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
axios.get(starWars)
  .then(function (response) {
    for (const x in response.data.characters) {
      const ulriq = response.data.characters[x];
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
