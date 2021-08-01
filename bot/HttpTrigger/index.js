const next = require('../index');

module.exports = async function (context, req) {
    const content = (req.body && req.body.content);

    context.res = {
        // status: 200, /* Defaults to 200 */
        body: content ? next(content) || 200 : 'No data.',
    };
}