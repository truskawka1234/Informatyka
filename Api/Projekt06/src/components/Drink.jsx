import React from "react";

function Drink({ strDrink, strDrinkThumb, idDrink }) {
  const handleAddToFavorites = () => {
    const existing = JSON.parse(localStorage.getItem("favorites")) || [];
    const isAlready = existing.some((fav) => fav.idDrink === idDrink);

    if (!isAlready) {
      const updated = [
        ...existing,
        {
          idDrink,
          strDrink,
          strDrinkThumb,
        },
      ];
      localStorage.setItem("favorites", JSON.stringify(updated));
    }
  };

  return (
    <div className="drink-card">
      <h2 className="drink-card__name">{strDrink}</h2>
      <img
        src={strDrinkThumb}
        alt={strDrink}
        className="drink-card__image"
        loading="lazy"
      />
      <div className="drink-card__info">
        <p>ID: {idDrink}</p>
      </div>
      <button onClick={handleAddToFavorites} className="drink-card__fav-btn">
        Dodaj do ulubionych ❤
      </button>
    </div>
  );
}

export default Drink;

// import React from "react";

// function Drink({ strDrink, strDrinkThumb, idDrink }) {
//   const handleAddToFavorites = () => {
//     const existing = JSON.parse(localStorage.getItem("favorites")) || [];
//     const isAlready = existing.some((fav) => fav.name === idDrink);
//     if (!isAlready) {
//       const updated = [...existing, { idDrink, strDrink, strDrinkThumb }];
//       localStorage.setItem("favorites", JSON.stringify(updated));
//     }
//   };

//   return (
//     <div className="drink-card">
//       <h2 className="drink-card__name">{strDrink}</h2>
//       <img
//         src={strDrinkThumb}
//         alt={strDrink}
//         className="drink-card__image"
//         loading="lazy"
//       />
//       <div className="drink-card__info">
//         <p>ID; {idDrink}</p>
//       </div>
//       <button onClick={handleAddToFavorites} className="drink-card__fav-btn">
//         {" "}
//         Dodaj do ulubionych❤
//       </button>
//     </div>
//   );
// }

// export default Drink;
