var Gpio = require('onoff').Gpio,
    led = new Gpio(17, 'out');

var iv = setInterval(function(){
    led.writeSync(led.readSync() === 0 ? 1 : 0)
}, 500);

// Stop blinking the LED and turn it off after 5 seconds.
setTimeout(function() {
    clearInterval(iv); // Stop blinking
    led.writeSync(0);  // Turn LED off.
    led.unexport();    // Unexport GPIO and free resources
}, 5000);


/*var five = require("johnny-five");
var Raspi = require("raspi-io");
*/
/*
var gpio = require("pi-gpio");

var intervalId;
var durationId;
var gpioPin = 11;    // header pin 16 = GPIO port 23

// open pin 16 for output
//
gpio.open(gpioPin, "output", function (err) {
    var on = 1;
    console.log('GPIO pin ' + gpioPin + ' is open. toggling LED every 100 mS for 10s');

    intervalId = setInterval(function () {
        gpio.write(gpioPin, on, function () { // toggle pin between high (1) and low (0)
            on = (on + 1) % 2;
        });
    }, 100);
});

durationId = setTimeout(function () {
    clearInterval(intervalId);
    clearTimeout(durationId);
    console.log('10 seconds blinking completed');
    gpio.write(gpioPin, 0, function () { // turn off pin 16
        gpio.close(gpioPin); // then Close pin 16
        process.exit(0); // and terminate the program
    });
}, 10000); // duration in mS

*/

/*
 var board = new five.Board({
 io: new Raspi()
 });

 board.on("ready", function() {
 var led = new five.Led("P1-11");
 led.blink();
 });
*/