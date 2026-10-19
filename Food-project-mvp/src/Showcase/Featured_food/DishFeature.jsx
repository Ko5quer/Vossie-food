import "./DishFeature.css";

// Each swirl is drawn in a 100x100 box that stretches to fill the section,
// so the same path works at any section height. Add more presets here.
export const swirls = {
  left: "M19 1 C9 7 8 22 16 30 C24 39 20 49 11 53 C3 58 6 72 0 83",
  right: "M55 1 C57 6 80 8 83 23 C86 38 85 50 93 55 C97 58 99 62 100 68",
};

export default function DishFeature({
  image,
  alt = "",
  title,
  description,
  swirl = "left", // a preset name from `swirls`, or your own SVG path string
  tick = false,   // small gold stroke at the bottom edge
}) {
  const path = swirls[swirl] ?? swirl;

  return (
    <section className="dish">
      {path && (
        <svg
          className="dish__swirl"
          viewBox="0 0 100 100"
          preserveAspectRatio="none"
          fill="none"
          aria-hidden="true"
        >
          <path d={path} vectorEffect="non-scaling-stroke" />
        </svg>
      )}

      <img className="dish__img" src={image} alt={alt} />
      <h2 className="dish__title">{title}</h2>
      <p className="dish__text">{description}</p>

      {tick && <span className="dish__tick" aria-hidden="true" />}
    </section>
  );
}
