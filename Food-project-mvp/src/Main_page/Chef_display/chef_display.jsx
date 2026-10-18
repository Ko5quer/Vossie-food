import "./chef_display.css";
import chef from "./chef.jpg";

export default function chefDisplay() {
  return (
    <section className="hero">
      <div className="hero-inner">
        <div className="hero-copy">
          <p className="eyebrow">Talent meets taste</p>

          <h1>
            Culinary Skills.
            <span>Real Opportunities.</span>
          </h1>

          <p className="lead">
            Culinary Cart is a student marketplace that brings together
            International Hotel School students, Eduvos students and food
            lovers. Discover, support and buy from talented chefs or showcase
            your work and grow your culinary journey.
          </p>

          <div className="actions">
            <a className="btn btn-gold" href="/shop">
              Shop Now
              <svg viewBox="0 0 40 16" width="38" height="16" aria-hidden="true">
                <path
                  d="M1 8h36M30 1l7 7-7 7"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  strokeLinejoin="round"
                />
              </svg>
            </a>
            <a className="btn btn-outline" href="/students">
              For Students
            </a>
          </div>
        </div>

        <div className="hero-media">
            <img
                src={chef}
                alt="Smiling chef in a white uniform and apron, arms crossed in a professional kitchen"
            />

            <svg
                className="hero-waves"
                viewBox="0 0 140 500"
                preserveAspectRatio="none"
                aria-hidden="true"
            >
                <path d="M20 0 C2 100, 10 170, 50 230 S90 360, 40 430 S30 480, 46 500" />
                <path d="M62 0 C44 100, 52 170, 92 230 S132 360, 82 430 S72 480, 88 500" />
            </svg>
        </div>
      </div>
    </section>
  );
}