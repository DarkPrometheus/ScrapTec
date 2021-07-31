const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bot listo`);
});

client.on('message', msg => {
    if (msg.content === 'ping') {
        msg.reply('pong');
    }
});

client.login('ODcxMTU2NTczMTAyMzAxMjQ1.YQXNyA.BI5JfAeYcokwQYI5IdNuscueCPU');

// Iniciar nodemon:
// npx nodemon index.js

// Tutorial bot:
// https://www.youtube.com/watch?v=EUB777JJT5E