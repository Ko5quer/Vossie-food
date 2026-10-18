import "./Categories.css";
import dish from "./plated-dish.jpg";
import boxes from "./sandwich-boxes.jpg";
import capIcon from "./graduation-cap.png";
import cartIcon from "./cart.png";

const categories = [
  {
    title: "Student Showcase",
    text: "See what our International Hotel School students have created.",
    cta: "Explore Work",
    href: "/showcase",
    image: dish,
    imageAlt: "Plated beef fillet with sauce and garnish on handmade stoneware plates",
    icon: capIcon,
  },
  {
    title: "Shop Student-made",
    text: "Browse homemade meals and culinary products from talented student chefs.",
    cta: "Shop Now",
    href: "/shop",
    image: boxes,
    imageAlt: "Boxed sandwiches, fruit cups and orange juice bottles",
    icon: cartIcon,
  },
];

export default function Categories() {
  return (
    <section className="categories" aria-labelledby="categories-heading">
      <div className="categories-inner">
        <p className="cat-eyebrow">Explore our categories</p>
        <h2 id="categories-heading">
          Two Worlds, <span>One Platform</span>
        </h2>

        {categories.map((c, i) => (
          <div key={c.title}>
            {i > 0 && <div className="cat-divider" aria-hidden="true" />}

            <article className="cat-card">
              <img className="cat-image" src={c.image} alt={c.imageAlt} />

              <div className="cat-body">
                <img className="cat-icon" src={c.icon} alt="" />
                <h3>{c.title}</h3>
                <p>{c.text}</p>
                <a className="cat-btn" href={c.href}>
                  {c.cta}
                  <svg viewBox="0 0 40 16" width="34" height="14" aria-hidden="true">
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
              </div>
            </article>
          </div>
        ))}
      </div>
    </section>
  );
}