import React from "react";

function Hobby() {
  const topics = [
    {
      title: "spanie",
      content:
        "Odpoczynek i sen są ważnym elementem mojego życia. Dają mi energię, pomagają się zregenerować i lepiej myśleć w ciągu dnia. Lubię też czasem drzemać w wolnych chwilach, aby poczuć się odświeżonym.",
    },
    {
      title: "Programowanie",
      content:
        "Programowanie to hobby, które rozwija logiczne myślenie i kreatywność. Tworzę proste gry, strony internetowe i eksperymentuję z nowymi językami programowania. To satysfakcjonujące, gdy własny projekt działa tak, jak zaplanowałem.",
    },
    {
      title: "Gotowanie",
      content:
        "Gotowanie to dla mnie sposób na kreatywność i eksperymentowanie ze smakami. Lubię próbować nowe przepisy, przygotowywać posiłki dla rodziny i przyjaciół. To hobby uczy cierpliwości i dokładności, a przy tym daje dużo satysfakcji.",
    },
    {
      title: "Muzyka",
      content:
        "Muzyka to dla mnie sposób na relaks i wyrażenie emocji. Lubię słuchać różnych gatunków, a czasem sam gram na gitarze lub śpiewam. Muzyka poprawia nastrój i dodaje energii.",
    },
    {
      title: "Sport",
      content:
        "Uprawianie sportu pozwala mi zachować dobrą kondycję i zdrowie. Gram w piłkę nożną, biegam i czasem jeżdżę na rowerze. Sport uczy mnie dyscypliny, wytrwałości i pracy zespołowej.",
    },
  ];

  return (
    <div className="hobby">
      <h1>Moje zaintersowania</h1>
      <div className="hobby__list">
        {topics.map((topic, index) => (
          <div className="hobby__card" key={index}>
            <h2>{topic.title}</h2>
            <p>{topic.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Hobby;

// export default function Hobby() {
//   return (
//     <section className="hobby">
//       <h2>Moje hobby</h2>
//       <p>Lubię programować, grać w gry i podróżować.</p>
//     </section>
//   );
// }
