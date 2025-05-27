import React from "react";

function Home() {
  return (
    <div className="home">
      <h1 className="home__title">Witaj na najelpszej stronce o drinkach!</h1>
      <p className="home__description">
        Znajdziesz tutaj informacje o różnych napojach, galerię zdjęć, quiz i
        wiele więcej.
      </p>
      <div className="home__image-wrapper">
        <img
          src="https://miksologia.pl/wp-content/uploads/2023/05/drink-californication-obraz-1-min.jpg"
          alt="Pieski"
          className="home__image"
          loading="lazy"
        />
      </div>
    </div>
  );
}

export default Home;
