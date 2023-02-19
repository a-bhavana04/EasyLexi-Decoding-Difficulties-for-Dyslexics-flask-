let speech = new SpeechSynthesisUtterance();
speech.lang = "en";
let voices = [];
voices = window.speechSynthesis.getVoices();
speech.voice = voices[1];


document.querySelector("#start").addEventListener("click", () => {
    speech.text = document.querySelector("textarea").value;
    window.speechSynthesis.speak(speech);

});
document.querySelector("#pause").addEventListener("click", () => {
    window.speechSynthesis.pause();
});

document.querySelector("#resume").addEventListener("click", () => {
    window.speechSynthesis.resume();
});

document.querySelector("#cancel").addEventListener("click", () => {
    window.speechSynthesis.cancel();
});

document.onload = window.speechSynthesis.cancel();