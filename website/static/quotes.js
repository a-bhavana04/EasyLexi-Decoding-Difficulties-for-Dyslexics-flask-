var randomNumber ;
var quotes = ["Accomodate (A-c-c-o-m-o-d-a-t-e)","Answer (A-n-s-w-e-r)","Government (G-o-v-e-r-n-m-e-n-t)","Guarantee (G-u-a-r-a-n-t-e-e)","Achieve (A-c-h-i-e-v-e)","Sacrifice (S-a-c-r-i-f-i-c-e)","Everybody (E-v-e-r-y-b-o-d-y)","Queue (Q-u-e-u-e)","Sentence (S-e-n-t-e-n-c-e)","Harass (H-a-r-a-s-s)","Appreciate (A-p-p-r-e-c-i-a-t-e )","Possible (P-o-s-s-i-b-l-e)","Remember (R-e-m-e-m-b-e-r)","Community (C-o-m-m-u-n-i-t-y )","Foreign (F-o-r-e-i-g-n)","Conscious (C-o-n-s-c-i-o-u-s)","Competition (C-o-m-p-e-t-i-t-i-o-n)"];
function newQuote(){
    randomNumber = Math.floor(Math.random()*quotes.length);
    document.getElementById('quotes').innerHTML = quotes[randomNumber];
    word = quotes[randomNumber];
    window.speechSynthesis.speak(sp);

}

function newL(){
    let sp = new SpeechSynthesisUtterance(quotes[randomNumber]);
    sp.lang = "en";
    let voices = [];
    voices = window.speechSynthesis.getVoices();
    sp.voice = voices[1];
    sp.rate = 0.5;
    window.speechSynthesis.speak(sp);
}

function readQuote(){
    let sp = new SpeechSynthesisUtterance("Dyslexia is not due to a lack of intelligence, it’s a lack of access. It’s like, if you’re dyslexic, you have all the information you need, but find it harder to process.");
    sp.lang = "en";
    let voices = [];
    voices = window.speechSynthesis.getVoices();
    sp.voice = voices[1];
    sp.rate = 0.7;
    window.speechSynthesis.speak(sp);
}