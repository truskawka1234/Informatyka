import React from "react";
import ReactDOM from "react-dom/client";
import "./scss/main.css";

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./components/Home";
import Drinks from "./components/Drinks";
import Gallery from "./components/Gallery";
import Quiz from "./components/Quiz";
import Favorites from "./components/Favorites";
import Recipe from "./components/Recipe";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Header />

    <BrowserRouter>
      <nav className="menu">
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/drinks">Drinki</Link>
          </li>
          <li>
            <Link to="/gallery">Galeria</Link>
          </li>
          <li>
            <Link to="/quiz">Test</Link>
          </li>
          <li>
            <Link to="/favorites">Ulubione</Link>
          </li>
          <li>
            <Link to="/recipe">Przepisy</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/drinks" element={<Drinks />} />
        <Route path="/gallery" element={<Gallery />} />
        <Route path="/quiz" element={<Quiz />} />
        <Route path="/favorites" element={<Favorites />} />
        <Route path="/recipe" element={<Recipe />} />
      </Routes>
    </BrowserRouter>

    <Footer />
  </React.StrictMode>
);
