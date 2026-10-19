
import { useState } from "react";
import { Link } from "react-router";
import "./Header.css";
import logo from "./Logo.png";

const links = [
  { label: "Home", href: "/" },
  { label: "About", href: "/about" },
  { label: "Our Stories", href: "/showcase" },
  { label: "Sale", href: "/shop" },
  { label: "My Cart", href: "/cart" },
  { label: "Sign Up", href: "/signup" },
];

export default function Header() {
  const [open, setOpen] = useState(false);

  const handleSearch = (e) => {
    e.preventDefault();
    const q = new FormData(e.currentTarget).get("q");
    console.log("search:", q);
  };

  return (
    <header className="site-header">
      <div className="header-inner">
        <Link className="brand" to="/" onClick={() => setOpen(false)}>
          <img className="brand-logo" src={logo} alt="" />
          <span className="brand-text">
            <span className="brand-name">
              Culinary <span>Cart</span>
            </span>
            <span className="brand-tagline">
              Your Campus. Your Marketplace
            </span>
          </span>
        </Link>

        <button
          className="menu-toggle"
          aria-expanded={open}
          aria-controls="primary-nav"
          onClick={() => setOpen((o) => !o)}
        >
          <span className="sr-only">Menu</span>
          <span className="bars" aria-hidden="true" />
        </button>

        <nav
          id="primary-nav"
          className={`nav ${open ? "is-open" : ""}`}
          aria-label="Primary"
        >
          <ul>
            {links.map((l) => (
              <li key={l.label}>
                <Link to={l.href} onClick={() => setOpen(false)}>
                  {l.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        <form className="search" role="search" onSubmit={handleSearch}>
          <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true">
            <circle
              cx="10"
              cy="10"
              r="6.5"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
            />
            <path
              d="M15 15l6 6"
              stroke="currentColor"
              strokeWidth="2.5"
              strokeLinecap="round"
            />
          </svg>
          <input
            type="search"
            name="q"
            placeholder="Search products"
            aria-label="Search products"
          />
        </form>
      </div>
    </header>
  );
}

