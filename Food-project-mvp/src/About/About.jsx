import "./About.css";
import chef from "./chef.jpg";

export default function About() {
  return (
    <section className="about" aria-labelledby="about-heading">
      <div className="about-main">
        <div className="about-copy">
          <p className="about-eyebrow">Talent meets taste</p>

          <h2 id="about-heading">
            About
            <span>Culinary Cart</span>
          </h2>

          <p>
            Culinary Cart is a student marketplace that brings together
            International Hotel School students, Eduvos students &amp; food
            lovers.
          </p>
          <p>
            Discover, support &amp; buy from talented chefs or showcase your
            work and grow your culinary journey.
          </p>
        </div>

        <div className="about-media">
          <img
            src={chef}
            alt="Chef slicing chicken on a blue cutting board in a professional kitchen"
          />

          <svg
            className="about-waves"
            viewBox="0 0 140 500"
            preserveAspectRatio="none"
            aria-hidden="true"
          >
            <path d="M20 0 C2 100, 10 170, 50 230 S90 360, 40 430 S30 480, 46 500" />
            <path d="M62 0 C44 100, 52 170, 92 230 S132 360, 82 430 S72 480, 88 500" />
          </svg>
        </div>
      </div>

      <div className="about-rule" aria-hidden="true" />
      <div className="about-tail" />
    </section>
  );
}