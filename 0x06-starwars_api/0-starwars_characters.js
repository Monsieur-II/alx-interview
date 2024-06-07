#!/usr/bin/node
const request = require('request');
const argv = require('process').argv;

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;
// console.log(url);
request({ url }, async (error, response, body) => {
  if (error) return console.error(error);

  const urlChars = JSON.parse(body).characters;
  // console.log(urlChar);
  for (const url of urlChars) {
    await new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) return console.log(error);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
