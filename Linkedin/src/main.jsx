import React from "react";
import ReactDOM from "react-dom/client";
import "./scss/main.scss";

import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./components/Home";
import Hobby from "./components/Hobby";
import Experience from "./components/Experience";
import Kontakt from "./components/Kontakt";

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
            <Link to="/hobby">Hobby</Link>
          </li>
          <li>
            <Link to="/experience">Doświadczenie</Link>
          </li>
          <li>
            <Link to="/contact">Kontakt</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/hobby" element={<Hobby />} />
        <Route path="/experience" element={<Experience />} />
        <Route path="/contact" element={<Kontakt />} />
      </Routes>
    </BrowserRouter>

    <Footer />
  </React.StrictMode>
);
// import React from "react";
// import ReactDOM from "react-dom/client";
// import { BrowserRouter, Routes, Route } from "react-router-dom";
// import "./scss/main.scss";

// import Header from "./components/Header";
// import Footer from "./components/Footer";
// import Home from "./components/Home";
// import Hobby from "./components/Hobby";
// import Experience from "./components/Experience";
// import Kontakt from "./components/Kontakt";

// ReactDOM.createRoot(document.getElementById("root")).render(
//   <BrowserRouter>
//     <Header />
//     <main>
//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/hobby" element={<Hobby />} />
//         <Route path="/experience" element={<Experience />} />
//         <Route path="/contact" element={<Kontakt />} />
//       </Routes>
//     </main>
//     <Footer />
//   </BrowserRouter>
// );

// import React from "react";
// import ReactDOM from "react-dom/client";
// import "./scss/main.scss";

// import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

// import Header from "./components/Header";
// import Footer from "./components/Footer";
// import Home from "./components/Home";
// import Hobby from "./components/Hobby";
// import Experience from "./components/Experience";
// import Kontakt from "./components/Kontakt";

// ReactDOM.createRoot(document.getElementById("root")).render(
//   <React.StrictMode>
//     <Header />

//     <BrowserRouter>
//       <nav className="menu">
//         <ul>
//           <li>
//             <Link to="/">Home</Link>
//           </li>
//           <li>
//             <Link to="/experience">Umiejętności</Link>
//           </li>
//           <li>
//             <Link to="/contacts">Kontakt</Link>
//           </li>
//           <li>
//             <Link to="/kontakt">Hobby</Link>
//           </li>
//         </ul>
//       </nav>

//       <Routes>
//         <Route path="/" element={<Home />} />
//         <Route path="/hobby" element={<Hobby />} />
//         <Route path="/experience" element={<Experience />} />
//         <Route path="/kontakt" element={<Kontakt />} />
//       </Routes>
//     </BrowserRouter>
//     <Footer />
//   </React.StrictMode>
// );
