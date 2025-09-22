import React from "react";

export default function Experience() {
  const softSkills = [
    "Komunikacja interpersonalna",
    "Praca zespołowa",
    "Rozwiązywanie problemów",
    "Zarządzanie czasem",
    "Kreatywność",
  ];

  return (
    <section className="experience">
      <h1 className="experience__title">Moje Umiejętności Miękkie</h1>

      <div className="experience__box">
        <ul>
          {softSkills.map((skill, index) => (
            <li key={index}>{skill}</li>
          ))}
        </ul>
      </div>

      <div className="experience__projects">
        <h2>Moje Projekty</h2>
        <p>Wszystkie moje dotychczasowe projekty możesz zobaczyć na GitHub:</p>
        <a
          href="https://github.com/truskawka1234"
          target="_blank"
          rel="noopener noreferrer"
          className="experience__github"
        >
          GitHub
        </a>
      </div>
    </section>
  );
}

// export default function Experience() {
//   return (
//     <section className="experience">
//       <h2>Doświadczenie</h2>
//       <p>Opis mojego doświadczenia zawodowego i projektów.</p>
//     </section>
//   );
// }
