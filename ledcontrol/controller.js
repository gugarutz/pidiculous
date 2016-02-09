var PythonShell = require('python-shell');

PythonShell.run('toggleLed.py', function (err) {
    if (err) throw err;
    console.log('finished');
});