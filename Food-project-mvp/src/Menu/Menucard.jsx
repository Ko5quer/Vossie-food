import React from "react";

export default function MenuCard({ image, title, description, price, onAdd }) {
  return (
    <article className="menu-card">
      <div className="menu-card__image-wrap">
        <img className="menu-card__image" src={image} alt={title} />
      </div>

      <div className="menu-card__body">
        <h3 className="menu-card__title">{title}</h3>
        <p className="menu-card__desc">{description}</p>
        <p className="menu-card__price">R{price}</p>
        <button className="menu-card__btn" type="button" onClick={onAdd}>
          Add to cart
        </button>
      </div>
    </article>
  );
}
