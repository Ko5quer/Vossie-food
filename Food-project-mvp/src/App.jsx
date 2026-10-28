import { useState } from "react";
import Main_page from "./Main_page/Main_page.jsx";
import WavyBanner from "./Banner/WavyBanner.jsx";
import Header from "./Nav_bar/Header.jsx";
import About from "./About/About.jsx";
import Showcase from "./Showcase/Showcase.jsx";
import Footer from "./Footer/Footer.jsx";
import Carts from "./Carts/Carts.jsx";
import Menu from "./Menu/Menu.jsx";
import { BrowserRouter, Routes, Route } from "react-router";

function App() {
  const [items, setItems] = useState([]);

  const addItem = (product) =>
    setItems((prev) => {
      const existing = prev.find((i) => i.id === product.id);
      return existing
        ? prev.map((i) =>
            i.id === product.id ? { ...i, quantity: i.quantity + 1 } : i
          )
        : [...prev, { ...product, quantity: 1 }];
    });

  const changeQuantity = (id, quantity) =>
    setItems((prev) =>
      prev.map((i) => (i.id === id ? { ...i, quantity } : i))
    );

  const removeItem = (id) =>
    setItems((prev) => prev.filter((i) => i.id !== id));

  const handleCheckout = () => {
    console.log("Checkout", items);
  };

  return (
    <BrowserRouter>
      <WavyBanner />
      <Header />
      <Routes>
        <Route path="/" element={<Main_page />} />
        <Route path="/showcase" element={<Showcase />} />
        <Route path="/shop" element={<Menu onAdd={addItem} />} />
        <Route path="/about" element={<About />} />
        <Route
          path="/cart"
          element={
            <Carts
              items={items}
              onQuantityChange={changeQuantity}
              onRemove={removeItem}
              onCheckout={handleCheckout}
            />
          }
        />
      </Routes>
      {/*<Footer/>*/}
    </BrowserRouter>
  );
}

export default App;
