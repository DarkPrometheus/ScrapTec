const next = require('./ntf.js');

module.exports = function (data) {
    /*
    data = [
        {
            title: '2021 Febrero - Junio',
            url: 'https://www.google.com/url?q=https%3A%2F%2Fsites.google.com%2Ftectijuana.edu.mx%2Fdsc-depto-de-sistemas-y-comp%2Fdscinicio%2Fcalendario-2021-febrero-julio%3Fauthuser%3D0&sa=D&sntz=1&usg=AFQjCNG_M4TlsttYlTxqkRn8g6P30UNwOw'
        },
    ]
    */
    
    return new Promise(resolve => {
        next(data).then(resolve);
    });
}