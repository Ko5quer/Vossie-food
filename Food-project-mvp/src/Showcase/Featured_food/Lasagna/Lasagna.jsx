import "./LasagnaFeature.css";
import lasagna from "./Lasagna.jpg"; // update to your image path

export default function LasagnaFeature() {
  return (
    <section className="lasagna">
      <svg
        className="lasagna__swirl"
        viewBox="0 0 160 470"
        fill="none"
        aria-hidden="true"
      >
        <path
          d="M135 5 C60 35 55 120 110 165 C170 215 140 270 75 295 C15 320 45 400 0 460"
          stroke="#d4a02c"
          strokeWidth="4"
          strokeLinecap="round"
        />
      </svg>

      <img className="lasagna__img" src={lasagna} alt="Plated lasagna with garlic ciabatta toasts" />

      <h2 className="lasagna__title">Classic comforts Lasanga</h2>

      <p className="lasagna__text">
        Indulgent layered pasta baked to perfection with a rich meat sauce and
        beautifully carmelized grantee cheese crown. Plated with vibrant
        marinara and accomplished by garlic ciabatta toasts for the perfect
        dip. Hearty, classic comfort and redefined.
      </p>

      <span className="lasagna__tick" aria-hidden="true" />
    </section>
  );
}
