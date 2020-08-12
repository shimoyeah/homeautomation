const googlehome = require('google-home-notifier');
const language = 'ja';
googlehome.device("居間", language);
googlehome.ip("192.168.0.27");
message = process.argv[2];
googlehome.notify(message, function(res) {
      console.log(res);
});
