// each module has to be wrapped in module.exports
// with function(io) i cann pass objects from other modules to this module
// to pass a object i have to call: var routes = require('./routes')(io);
module.exports = function (io) {
    return {
        // GET: /api
        index: function (req, res) {
            res.json({message: 'go to /api/message.'});
        },

        on: function (req, res) {
            //var PythonShell = require('python-shell');
            var pyshell = new PythonShell('my_script.py');

            // sends a message to the Python script via stdin
            pyshell.send('hello');

            pyshell.on('message', function (message) {
                // received a message sent from the Python script (a simple "print" statement)
                console.log(message);
            });

            // end the input stream and allow the process to exit
            pyshell.end(function (err) {
                if (err) throw err;
                console.log('finished');
            });
        },

        off: function (req, res) {

        }
    }
}