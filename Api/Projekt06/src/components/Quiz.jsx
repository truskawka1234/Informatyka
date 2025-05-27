// import React, { useState, useEffect } from "react";

// const QUIZ_SIZE = 5; // ile pytań w quizie

// function Quiz() {
//   const [questions, setQuestions] = useState([]);
//   const [current, setCurrent] = useState(0);
//   const [selected, setSelected] = useState(null);
//   const [score, setScore] = useState(0);
//   const [loading, setLoading] = useState(true);
//   const [error, setError] = useState(null);

//   // Pobieramy pytania (rasy + zdjęcia + opcje)
//   useEffect(() => {
//     async function fetchQuiz() {
//       try {
//         setLoading(true);
//         const res = await fetch("https://dog.ceo/api/breeds/list/all");
//         const data = await res.json();

//         const allBreeds = Object.keys(data.message);
//         // Losujemy QUIZ_SIZE ras
//         const selectedBreeds = allBreeds
//           .sort(() => 0.5 - Math.random())
//           .slice(0, QUIZ_SIZE);

//         // Dla każdej rasy pobieramy zdjęcie
//         const quizQuestions = await Promise.all(
//           selectedBreeds.map(async (breed) => {
//             const resImg = await fetch(
//               `https://dog.ceo/api/breed/${breed}/images/random`
//             );
//             const imgData = await resImg.json();

//             // Tworzymy 3 losowe fałszywe odpowiedzi
//             const fakeAnswers = allBreeds
//               .filter((b) => b !== breed)
//               .sort(() => 0.5 - Math.random())
//               .slice(0, 3);

//             // Mieszamy poprawną odpowiedź z fałszywymi
//             const options = [...fakeAnswers, breed].sort(
//               () => 0.5 - Math.random()
//             );

//             return {
//               breed,
//               imageUrl: imgData.message,
//               options,
//             };
//           })
//         );

//         setQuestions(quizQuestions);
//         setLoading(false);
//       } catch (err) {
//         setError("Coś poszło nie tak podczas ładowania quizu.");
//         setLoading(false);
//       }
//     }

//     fetchQuiz();
//   }, []);

//   if (loading) return <p>Ładowanie quizu...</p>;
//   if (error) return <p>{error}</p>;

//   const question = questions[current];

//   function handleAnswer(option) {
//     setSelected(option);
//     if (option === question.breed) setScore(score + 1);
//   }

//   function nextQuestion() {
//     setSelected(null);
//     if (current < questions.length - 1) {
//       setCurrent(current + 1);
//     } else {
//       // quiz skończony, możesz tu rozwinąć wynik albo reset
//       alert(`Koniec quizu! Twój wynik to: ${score} / ${questions.length}`);
//       setCurrent(0);
//       setScore(0);
//       setSelected(null);
//     }
//   }

//   return (
//     <div className="quiz">
//       <h1>Quiz: Zgadnij co to za drink</h1>
//       <div className="quiz__question">
//         <img
//           src={question.imageUrl}
//           alt="Pies do zgadnięcia"
//           className="quiz__image"
//         />
//       </div>
//       <div className="quiz__options">
//         {question.options.map((option) => (
//           <button
//             key={option}
//             className={`quiz__option ${
//               selected
//                 ? option === question.breed
//                   ? "quiz__option--correct"
//                   : option === selected
//                   ? "quiz__option--wrong"
//                   : ""
//                 : ""
//             }`}
//             onClick={() => !selected && handleAnswer(option)}
//             disabled={!!selected}
//           >
//             {option}
//           </button>
//         ))}
//       </div>
//       {selected && (
//         <button className="quiz__next" onClick={nextQuestion}>
//           {current === questions.length - 1
//             ? "Zakończ quiz"
//             : "Następne pytanie"}
//         </button>
//       )}
//       <p>
//         Wynik: {score} / {questions.length}
//       </p>
//     </div>
//   );
// }

// export default Quiz;
import React, { useState, useEffect } from "react";

const QUIZ_SIZE = 5;

function Quiz() {
  const [questions, setQuestions] = useState([]);
  const [current, setCurrent] = useState(0);
  const [selected, setSelected] = useState(null);
  const [score, setScore] = useState(0);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchQuiz() {
      try {
        setLoading(true);
        const res = await fetch(
          "https://www.thecocktaildb.com/api/json/v1/1/filter.php?a=Alcoholic"
        );
        const data = await res.json();
        const drinks = data.drinks;

        // Losujemy 5 drinków jako pytania
        const selectedDrinks = drinks
          .sort(() => 0.5 - Math.random())
          .slice(0, QUIZ_SIZE);

        const quizQuestions = selectedDrinks.map((drink) => {
          const incorrect = drinks
            .filter((d) => d.idDrink !== drink.idDrink)
            .sort(() => 0.5 - Math.random())
            .slice(0, 3);

          const options = [
            ...incorrect.map((d) => d.strDrink),
            drink.strDrink,
          ].sort(() => 0.5 - Math.random());

          return {
            correctName: drink.strDrink,
            imageUrl: drink.strDrinkThumb,
            options,
          };
        });

        setQuestions(quizQuestions);
        setLoading(false);
      } catch (err) {
        console.error(err);
        setError("Nie udało się załadować quizu.");
        setLoading(false);
      }
    }

    fetchQuiz();
  }, []);

  const question = questions[current];

  function handleAnswer(option) {
    setSelected(option);
    if (option === question.correctName) setScore(score + 1);
  }

  function nextQuestion() {
    setSelected(null);
    if (current < questions.length - 1) {
      setCurrent(current + 1);
    } else {
      alert(`Quiz zakończony! Twój wynik to: ${score} / ${questions.length}`);
      setCurrent(0);
      setScore(0);
      setSelected(null);
    }
  }

  if (loading) return <p>Ładowanie quizu...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div className="quiz">
      <h1>Quiz: Zgadnij co to za drink</h1>
      <div className="quiz__question">
        <img
          src={question.imageUrl}
          alt="Drink"
          className="quiz__image"
          style={{ maxWidth: "300px", borderRadius: "10px" }}
        />
      </div>
      <div className="quiz__options">
        {question.options.map((option) => (
          <button
            key={option}
            className={`quiz__option ${
              selected
                ? option === question.correctName
                  ? "quiz__option--correct"
                  : option === selected
                  ? "quiz__option--wrong"
                  : ""
                : ""
            }`}
            onClick={() => !selected && handleAnswer(option)}
            disabled={!!selected}
          >
            {option}
          </button>
        ))}
      </div>
      {selected && (
        <button className="quiz__next" onClick={nextQuestion}>
          {current === questions.length - 1
            ? "Zakończ quiz"
            : "Następne pytanie"}
        </button>
      )}
      <p>
        Wynik: {score} / {questions.length}
      </p>
    </div>
  );
}

export default Quiz;
