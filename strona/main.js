buttonRed.addEventListener("click", () => {
  changeColor("red");
});

buttonGreen.addEventListener("click", () => {
  changeColor("green");
});

buttonOrange.addEventListener("click", () => {
  changeColor("orange");
});

buttonPink.addEventListener("click", () => {
  changeColor("pink");
});

// buttonPink.addEventListener

// addEventListener to metoda,
// która dodaje nasłuchiwacza zdarzeń
// do elementu. W tym przypadku nasłuchujemy
// na zdarzenie typu "click". Oznacza to, że
// kiedy użytkownik kliknie przycisk o klasie
// .pink-button, zostanie uruchomiona określona funkcja.

// () => { ... }:

// To jest funkcja strzałkowa (arrow function) w
// JavaScript, która zostanie wywołana po kliknięciu na przycisk.
// Funkcje strzałkowe to skrócony zapis funkcji anonimowych.
// W tym przypadku, po kliknięciu, funkcja zostanie wywołana.
// changeColor('pink'):
