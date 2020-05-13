#!/usr/bin/node
 // status code
const request = require('request');
const info = process.argv[2];
request(info, function(err, response) {
    if (err) {
        console.log(err);
    } else {
        console.log('code: ' + response.statusCode);
    }
});