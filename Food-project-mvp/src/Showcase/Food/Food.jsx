import "./Food.css";
import "./Food.css";

import pexels_1 from "./pexels_1.jpg";
import pexels_2 from "./pexels_2.jpg";
import pexels_3 from "./pexels_3.jpg";
import pexels_4 from "./pexels_4.jpg";


const defaultImages = [
  { src: pexels_1, alt: "Mini tarts and citrus desserts on white plates" },
  { src: pexels_2, alt: "Pâté on apple crisps with pomegranate seeds" },
  { src: pexels_3, alt: "Plated starter in a speckled grey bowl" },
  { src: pexels_4, alt: "Salmon with greens on a green speckled plate" },
];

export default function FoodCollage({ images = defaultImages }) {
  return (
    <section className="food-collage" aria-label="Food gallery">
      {images.slice(0, 4).map((img, i) => (
        <figure className="food-collage__cell" key={i}>
          <img
            className="food-collage__img"
            src={img.src}
            alt={img.alt || ""}
            loading="lazy"
          />
        </figure>
      ))}
    </section>
  );
}
