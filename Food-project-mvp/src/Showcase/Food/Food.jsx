import "./FoodCollage.css";

// Replace these with your own image imports or paths, e.g.
// import tarts from "../assets/tarts.jpg";
const defaultImages = [
  { src: "/images/tarts.jpg", alt: "Mini tarts and citrus desserts on white plates" },
  { src: "/images/pate-apple.jpg", alt: "Pâté on apple crisps with pomegranate seeds" },
  { src: "/images/speckled-bowl.jpg", alt: "Plated starter in a speckled grey bowl" },
  { src: "/images/green-plate.jpg", alt: "Salmon with greens on a green speckled plate" },
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