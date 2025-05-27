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
    fetch("https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Cocktail")
      .then((res) => res.json())
      .then((data) => {
        setAllDrinks(data.drinks || []);
        setDisplayedDrinks(data.drinks.slice(0, LOAD_STEP));
        setLoading(false);
      });
  }, []);

  const handleLoadMore = () => {
    setLoadingMore(true);
    setTimeout(() => {
      const newCount = displayCount + LOAD_STEP;
      setDisplayedDrinks(allDrinks.slice(0, newCount));
      setDisplayCount(newCount);
      setLoadingMore(false);
    }, 500);
  };

  return (
    <div className="drinks-gallery">
      <h1>Typy drinków</h1>

      {loading ? (
        <p>Ładowanie drinków...</p>
      ) : (
        <>
          <div className="drinks-gallery__grid">
            {displayedDrinks.map((drink) => (
              <Drink
                key={drink.idDrink}
                strDrink={drink.strDrink}
                strDrinkThumb={drink.strDrinkThumb}
                idDrink={drink.idDrink}
              />
            ))}
          </div>
          {displayedDrinks.length < allDrinks.length && (
            <button
              onClick={handleLoadMore}
              disabled={loadingMore}
              className="drinks-gallery__load-more"
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
