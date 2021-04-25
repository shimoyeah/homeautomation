const googlehome = require('google-home-notifier');
const language = 'ja';
googlehome.device("リビング", language);
googlehome.ip("192.168.0.32");
message = process.argv[2];
googlehome.notify(message, function(res) {
      console.log(res);
});
