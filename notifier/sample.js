var googlehome = require('google-home-notifier');
var language = 'ja';

googlehome.device('テスト', language);
googlehome.ip('192.168.0.27');// IPアドレスは自分の環境のGoogleHomeの設定に合わせてください

var text = 'みなさんは岐阜にはどういった観光スポットがあるかご存知ですか？岐阜は実は美濃地方と飛騨地方に分かれており、観光スポットや温泉、旅館が多くあるのは、飛騨地方です。そのため、岐阜に行こうと思ったときは、 まず飛騨地方で探してください。飛騨地方には高山、下呂温泉、白川郷（世界遺産）といった観光スポットが多くあります。高山は昔ながらの街並みが有名で、「さるぼぼ」という人形がおみやげの定番です';

try {
        googlehome.notify(text, function(notifyRes) {
                console.log(notifyRes);
        });
} catch(err) {
        console.log(err);
}
