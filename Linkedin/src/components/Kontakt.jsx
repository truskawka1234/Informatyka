import React from "react";

export default function Kontakt() {
  return (
    <section className="kontakt">
      <h1 className="kontakt__title">Kontakt :</h1>
      <p className="kontakt__description">
        Masz pytania lub chcesz się ze mną skontaktować? Znajdziesz mnie tutaj:
      </p>
      <div className="kontakt__links">
        <a
          href="https://www.linkedin.com/in/twoj-linkedin/"
          target="_blank"
          rel="noopener noreferrer"
          className="kontakt__link"
        >
          LinkedIn
        </a>
        <a
          href="https://discord.com/users/twoj-discord-id"
          target="_blank"
          rel="noopener noreferrer"
          className="kontakt__link"
        >
          Discord
        </a>
        <a href="mailto:twoj.email@example.com" className="kontakt__link">
          Email
        </a>
      </div>
    </section>
  );
}

// export default function Kontakt() {
//   return (
//     <section className="kontakt">
//       <h2>Kontakt</h2>
//       <form>
//         <label>
//           Imię:
//           <input type="text" name="name" />
//         </label>
//         <br />
//         <label>
//           Wiadomość:
//           <textarea name="message"></textarea>
//         </label>
//         <br />
//         <button type="submit">Wyślij</button>
//       </form>
//     </section>
//   );
// }
