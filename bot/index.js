const { Client, MessageEmbed } = require('discord.js');
const client = new Client();
const { token } = require('./secrets.js')

let json = require('./data.json');
const channel = client.channels.cache.find(ch => ch.name === 'tec');
let Title = json[0].title;

client.on('ready', () => {
    console.log(`Bot listo`);
});

client.on('message', msg => {
    if (msg.content === 'ping') {
        const mensaje = new MessageEmbed()
            .setTitle(Title)
            .setColor("#016E3E")
            .setAuthor("Tec Tijuana", "https://www.tijuana.tecnm.mx/wp-content/uploads/2018/09/logo-ITT-2018.jpg")
            .setDescription(des);
        msg.channel.send(mensaje)
    }
});

const sendMessaje = () => {
    channel.send("Hola mundo").then(() => {
        client.destroy();
    });
}

client.login(token);

// Iniciar nodemon:
// npx nodemon index.js

// Tutorial bot:
// https://www.youtube.com/watch?v=EUB777JJT5E
