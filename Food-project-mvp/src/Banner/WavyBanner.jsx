import "./WavyBanner.css";

export default function WavyBanner() {
  return (
    <header className="banner">
      <svg
        className="waves"
        viewBox="300 0 130 141"
        preserveAspectRatio="xMidYMin meet"
        role="presentation"
        aria-hidden="true"
      >
        <path
          className="wave wave-1"
          pathLength="1"
          d="M315 0 C312 25, 322 38, 345 48 S375 70, 345 90 S328 125, 337 141"
        />
        <path
          className="wave wave-2"
          pathLength="1"
          d="M358 0 C355 22, 368 38, 392 52 S415 70, 385 95 S372 125, 380 141"
        />
      </svg>
    </header>
  );
}