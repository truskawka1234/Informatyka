import React, { useEffect, useState } from "react";
import Drink from "./Drink";

const LOAD_STEP = 6;

function Drinks() {
  const [allDrinks, setAllDrinks] = useState([]);
  const [displayedDrinks, setDisplayedDrinks] = useState([]);
  const [displayCount, setDisplayCount] = useState(LOAD_STEP);
  const [loading, setLoading] = useState(true);
  const [loadingMore, setLoadingMore] = useState(false);

  useEffect(() => {
    // 1. Pobieramy wszystkie drinki z danej kategorii (np. "Cocktail")
    fetch("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
      .then((res) => res.json())
      .then((data) => {
        setAllDrinks(data.drinks || []);
      });
  }, []);

  useEffect(() => {
    if (allDrinks.length === 0) return;
    setLoading(true);

    const drinksToLoad = allDrinks.slice(0, displayCount);

    // 2. Dla każdego drinka pobieramy szczegóły
    const detailPromises = drinksToLoad.map((drink) =>
      fetch(
        `https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=${drink.idDrink}`
      )
        .then((res) => res.json())
        .then((data) => data.drinks[0])
    );

    Promise.all(detailPromises).then((fullDetails) => {
      setDisplayedDrinks(fullDetails);
      setLoading(false);
      setLoadingMore(false);
    });
  }, [allDrinks, displayCount]);

  const handleLoadMore = () => {
    setLoadingMore(true);
    setDisplayCount((prev) => Math.min(prev + LOAD_STEP, allDrinks.length));
  };

  return (
    <div className="gallery">
      <h1>Galeria drinków</h1>

      {loading ? (
        <p>Ładowanie drinków...</p>
      ) : (
        <>
          <div className="gallery__grid">
            {displayedDrinks.map((drink) => (
              <Drink key={drink.idDrink} {...drink} />
            ))}
          </div>

          {displayedDrinks.length < allDrinks.length && (
            <button
              onClick={handleLoadMore}
              disabled={loadingMore}
              className="gallery__load-more"
            >
              {loadingMore ? "Ładowanie..." : "Załaduj więcej"}
            </button>
          )}
        </>
      )}
    </div>
  );
}

export default Drinks;
