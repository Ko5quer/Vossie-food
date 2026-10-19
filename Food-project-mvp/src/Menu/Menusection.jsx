import React from "react";
import "./MenuSection.css";

// Container: grows downward automatically as you add children.
export default function MenuSection({
  title = "On THE MENU",
  subtitle = "Thinking of something delicious ?",
  tagline = "Check out our student made foods !",
  children,
}) {
  return (
    <section className="menu-section">
      <header className="menu-section__header">
        <h2 className="menu-section__title">{title}</h2>
        <p className="menu-section__subtitle">{subtitle}</p>
        <p className="menu-section__tagline">{tagline}</p>
      </header>

      <div className="menu-section__grid">{children}</div>
    </section>
  );
}
