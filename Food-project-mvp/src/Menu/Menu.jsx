import React from "react";
import MenuSection from "./Menusection.jsx";
import MenuCard from "./Menucard.jsx";

// Replace with your own image imports / URLs
import chicken from "./chicken.jpg";
import boerewors from "./boerewors.jpg";
import grilled_chicken from "./grilled.jpg";
import burger from "./burger.jpg";
const items = [
  {
    id: 1,
    image: chicken,
    title: "Grilled Chicken & Cashew Rice",
    description:
      "Spiced yellow rice topped with grilled chicken breasts & whole cashews",
    price: 55,
  },
  {
    id: 2,
    image: boerewors,
    title: "Boerewors with rice & gravy",
    description:
      "Three grilled Boerewors with yellow rice, crispy onions & gravy",
    price: 70,
  },
  {
    id: 3,
    image: burger,
    title: "Smoked Double burger",
    description:
      "Two beef patties with BBQ sauce,bacon, greenery & chips",
    price: 70,
  },
  {
    id: 4,
    image: chicken,
    title: "Caesar Chicken Wraps",
    description:
      "Four tortilla wraps with crispy chicken & greenery",
    price: 35,
  },
  // add more objects here and new cards appear automatically
];

export default function Menu() {
  const handleAdd = (item) => console.log("Added to cart:", item);

  return (
    <MenuSection>
      {items.map((item) => (
        <MenuCard key={item.id} {...item} onAdd={() => handleAdd(item)} />
      ))}
    </MenuSection>
  );
}
