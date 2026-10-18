import "./Features.css";
import showcase from "./showcase.png";
import shop from "./shop.png";
import network from "./network.png";
import events from "./events.png";

const features = [
  {
    title: "Showcase Your Work",
    text: "International Hotel School students can display their skills & build their portfolio.",
    icon: showcase,
  },
  {
    title: "Buy Fresh & Local",
    text: "Support student chefs by purchasing homemade, high quality food & culinary products.",
    icon: shop,
  },
  {
    title: "Build Your Network",
    text: "Connect with fellow students, industry professionals & potential employers.",
    icon: network,
  },
  {
    title: "Events & Workshops",
    text: "Join exclusive tasting events, workshops and networking opportunities.",
    icon: events,
  },
];

export default function Features() {
  return (
    <section className="features" aria-label="Why Culinary Cart">
      <ul className="features-grid">
        {features.map((f) => (
          <li className="feature" key={f.title}>
            <img className="feature-icon" src={f.icon} alt="" />
            <h3>{f.title}</h3>
            <p>{f.text}</p>
          </li>
        ))}
      </ul>
    </section>
  );
}