const { Client, MessageEmbed } = require('discord.js');
const client = new Client();
const { token } = require('./secrets.js')

module.exports = function(json) {
  client.on('ready', () => {
      console.log(`Bot listo`);
      sendMessaje();
  });

  const sendMessaje = () => {
      const channel = client.channels.cache.find(ch => ch.name === 'tec');
      const mensaje = new MessageEmbed()
          .setTitle(json[0].title)
          .setColor("#016E3E")
          .setAuthor("Tec Tijuana", "https://www.tijuana.tecnm.mx/wp-content/uploads/2018/09/logo-ITT-2018.jpg")
          .setDescription(json[0].url);

      channel.send("@everyone")
      channel.send("Ya encontre el chingado calendario alv")
      channel.send(mensaje)
  }

  client.login(token);
}