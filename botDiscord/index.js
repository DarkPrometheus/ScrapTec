const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bot listo`);
    sendMessaje();
});

client.on('message', msg => {
    if (msg.content === 'ping') {

    }
});

const sendMessaje = () => {
    const channel = client.channels.cache.find(ch => ch.name === 'tec');
    channel.send("Hola mundo")
}

client.login('ODcxMTU2NTczMTAyMzAxMjQ1.YQXNyA.bIWCUq4nozZWp4JTpID51tlKIbk');

// Iniciar nodemon:
// npx nodemon index.js

// Tutorial bot:
// https://www.youtube.com/watch?v=EUB777JJT5E