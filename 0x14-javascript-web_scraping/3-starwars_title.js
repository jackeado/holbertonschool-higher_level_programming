#!/usr/bin/node
 // Star Wars API
const request = require('request');
const requestURL = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];
request(requestURL + episode, function(error, response, body) {
    if (error) {
        console.log(error);
    } else if (response.statusCode === 200) {
        const epi = JSON.parse(body);
        console.log(epi.title);
    } else {
        console.log('An error occured. Status code: ' + response.statusCode);
    }
});