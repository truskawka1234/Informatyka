import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./scss/main.css";
import Flag from "./components/Flag";
import Tlo from "./components/Tlo";
import Ostatni from "./components/Ostatni";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
    <Flag />
    <Tlo />
    <Ostatni />
  </React.StrictMode>
);
