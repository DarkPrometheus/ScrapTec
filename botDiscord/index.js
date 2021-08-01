const Discord = require('discord.js');
const client = new Discord.Client();
const { token } = require('./secrets.js')

client.on('ready', () => {
  client.channels.cache.get('871179765825032243').
    send('Hola y adios').then(() => {
      client.destroy();
    });
});

client.login(token);
