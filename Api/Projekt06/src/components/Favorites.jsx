import React, { useEffect, useState } from "react";

function Favorites() {
  const [favorites, setFavorites] = useState([]);

  useEffect(() => {
    const stored = localStorage.getItem("favorites");
    if (stored) {
      setFavorites(JSON.parse(stored));
    }
  }, []);

  const removeFavorite = (id) => {
    const updated = favorites.filter((item) => item.id !== id);
    localStorage.setItem("favorites", JSON.stringify(updated));
    setFavorites(updated);
  };

  if (favorites.length === 0) {
    return <p className="favorites__empty">Brak ulubionych drinków 😢</p>;
  }

  return (
    <div className="favorites">
      <h1>Twoje ulubione drinki</h1>
      <div className="favorites__list">
        {favorites.map((fav) => (
          <div key={fav.id} className="favorites__item">
            <img src={fav.strDrinkThumb} alt={fav.strDrink} />
            <h3>{fav.strDrink}</h3>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Favorites;
