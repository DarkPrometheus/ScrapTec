const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log(`Bot listo`);
    sendMessaje();
});

const sendMessaje = () => {
    const channel = client.channels.cache.find(ch => ch.name === 'tec');
    channel.send("Ya lo encontre el chingado calendario alv")
}

client.login('ODcxMTU2NTczMTAyMzAxMjQ1.YQXNyA.bIWCUq4nozZWp4JTpID51tlKIbk');