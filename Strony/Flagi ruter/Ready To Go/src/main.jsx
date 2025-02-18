import React from "react";
import ReactDOM from "react-dom/client";
import "./scss/main.css";

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Header from "./components/Header";
import A1 from "./components/A1";
import A2 from "./components/A2";
import A3 from "./components/A3";
import A4 from "./components/A4";
import A5 from "./components/A5";
import Footer from "./components/Footer";

function Navigation() {
  return (
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/a1">Przejdź do A1</Link>
          </li>
          <li>
            <Link to="/a2">Przejdź do A2</Link>
          </li>
          <li>
            <Link to="/a3">Przejdź do A3</Link>
          </li>
          <li>
            <Link to="/a4">Przejdź do A4</Link>
          </li>
          <li>
            <Link to="/a5">Przejdź do A5</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Header />
    <BrowserRouter>
      <Navigation />
      <Routes>
        <Route path="/a1" element={<A1 />} />
        <Route path="/a2" element={<A2 />} />
        <Route path="/a3" element={<A3 />} />
        <Route path="/a4" element={<A4 />} />
        <Route path="/a5" element={<A5 />} />
      </Routes>
    </BrowserRouter>
    <Footer />
  </React.StrictMode>
);
