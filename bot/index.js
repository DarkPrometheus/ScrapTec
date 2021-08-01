const Discord = require('discord.js');
const client = new Discord.Client();
const { token } = require('./secrets.js')

client.on('ready', () => {
    sendMessaje();
});

const sendMessaje = () => {
    const channel = client.channels.cache.find(ch => ch.name === 'tec');
    channel.send("Hola mundo").then(() => {
        client.destroy();
    });
}


module.exports = function (data) {
    /*
    data = [
        {
            title: '2021 Febrero - Junio',
            url: 'https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Ftectijuana.edu.mx%2Fdsc-depto-de-sistemas-y-comp%2Fdscinicio%2Fcalendario-2021-febrero-julio%3Fauthuser%3D0&sa=D&sntz=1&usg=AFQjCNG_M4TlsttYlTxqkRn8g6P30UNwOw'
        },
    ]
    */

    client.login(token);

    return 'Okay.'; // or any message
}

// Iniciar nodemon:
// npx nodemon index.js

// Tutorial bot:
// https://www.youtube.com/watch?v=EUB777JJT5E
