import React from "react";

function Recipe() {
  const topics = [
    {
      title: "Vodka Cranberry ",
      content:
        "45 ml wódki czystej lub żurawinowej/120 ml soku żurawinowego/2 plasterki limonki/sok z cytryny i cukier do wykonania crustu/lód",
    },
    {
      title: "Lemon Drop",
      content:
        "50 ml wódki cytrynowej/30 ml soku z cytryny/20 ml syropu cukrowego (20 ml wody z rozpuszczonymi 2 łyżeczkami cukru)/1 plaster z cytryny/sok z cytryny i cukier do wykonania crustu  /lód",
    },
    {
      title: "Mojito",
      content:
        "45 ml białego rumu/20 ml świeżego soku z limonki/6 szt. gałązek mięty/2 łyżeczki białego cukru trzcinowego/woda sodowa",
    },
    {
      title: "Aperol Spritz",
      content:
        "60 ml (2 oz) Aperol, /90 ml (3 oz) Prosecco lub innego musującego wina, schłodzone/30 ml (1 oz) wody gazowanej/lód/do dekoracji: plaster pomarańczy, słomka ",
    },
    {
      title: "Whisky Sour",
      content:
        "1 kieliszek whisky, bourbon lub rye/1 łyżka sproszkowanego białego cukru rozpuszczonego w odrobinie wody Seltzer lub Apollinaris./sok z połowy małej cytryny./Udekoruj jagodami. ",
    },
  ];

  return (
    <div className="recipe">
      <h1>TOP 5 przepisów na drinki</h1>
      <div className="recipe__list">
        {topics.map((topic, index) => (
          <div className="recipe__card" key={index}>
            <h2>{topic.title}</h2>
            <p>{topic.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Recipe;
