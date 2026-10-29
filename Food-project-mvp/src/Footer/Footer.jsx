import { useState } from "react";
import "./Footer.css";
import logo from "./Logo.png"
/* ============================================================
   EDIT THIS SECTION TO CHANGE CONTENT
   Everything the footer shows lives in this config object.
   ============================================================ */
const FOOTER = {
  brand: {
    name: "Culinary Cart",
    tagline: "Student Marketplace",
    logoSrc: logo,
    // true = your image already contains the icon AND the wordmark text,
    // so show the image on its own. false = image is just the icon and
    // the name + tagline are drawn as live text beside it.
    logoOnly: false,
    description:
      "Connecting student chefs with food lovers and new opportunities.",
  },

  // icon options: "mail" | "phone" | "pin"
  contact: [
    { icon: "mail", text: "hello@culinarycart.co.za", href: "mailto:hello@culinarycart.co.za" },
    { icon: "phone", text: "+27 11 555 0184", href: "tel:+27115550184" },
    { icon: "pin", text: "Pretoria, South Africa" }, // no href = plain text
  ],

  // Add, remove or reorder columns freely. Each one renders automatically.
  columns: [
    {
      title: "Quick Links",
      links: [
        { label: "Home", href: "/" },
        { label: "Shop", href: "/shop" },
        { label: "Students", href: "/students" },
        { label: "Events & Workshops", href: "/events" },
        { label: "About", href: "/about" },
      ],
    },
    {
      title: "Support",
      links: [
        { label: "Help Centre", href: "/help" },
        { label: "FAQs", href: "/faqs" },
        { label: "Shipping & Collection", href: "/shipping" },
        { label: "Seller Guidelines", href: "/seller-guidelines" },
        { label: "Privacy Policy", href: "/privacy" },
      ],
    },
  ],

  // To add a social: add a line here. `icon` must be a key in ICONS below.
  // Built in: instagram, facebook, tiktok, linkedin, x, youtube, whatsapp
  socials: [
    { label: "Instagram", icon: "instagram", href: "https://instagram.com/culinarycart" },
    { label: "Facebook", icon: "facebook", href: "https://facebook.com/culinarycart" },
    { label: "TikTok", icon: "tiktok", href: "https://tiktok.com/@culinarycart" },
    { label: "LinkedIn", icon: "linkedin", href: "https://linkedin.com/company/culinarycart" },
    // { label: "YouTube", icon: "youtube", href: "https://youtube.com/@culinarycart" },
    // { label: "X", icon: "x", href: "https://x.com/culinarycart" },
    // { label: "WhatsApp", icon: "whatsapp", href: "https://wa.me/27115550184" },
  ],

  newsletter: {
    title: "Stay Connected",
    text: "Follow our journey and discover student-made goodness.",
    placeholder: "Your email address",
    button: "Subscribe",
  },

  legal: {
    copyright: "Culinary Cart. All rights reserved.",
    note: "Made with care for the next generation of chefs.",
  },
};

/* ============================================================
   ICONS (inline SVG, no dependencies). Add new ones here.
   ============================================================ */
const stroke = {
  fill: "none",
  stroke: "currentColor",
  strokeWidth: 1.6,
  strokeLinecap: "round",
  strokeLinejoin: "round",
};

const ICONS = {
  // Contact icons (outlined)
  mail: (
    <g {...stroke}>
      <rect x="3" y="5" width="18" height="14" rx="2.5" />
      <path d="m3.5 7 8.5 6 8.5-6" />
    </g>
  ),
  phone: (
    <g {...stroke}>
      <path d="M5 4h3l1.6 4-2 1.3a11 11 0 0 0 5.1 5.1l1.3-2 4 1.6v3a2 2 0 0 1-2.2 2A15 15 0 0 1 3 6.2 2 2 0 0 1 5 4Z" />
      <path d="M14 3.5a6.5 6.5 0 0 1 6.5 6.5M14 7a3 3 0 0 1 3 3" />
    </g>
  ),
  pin: (
    <g {...stroke}>
      <path d="M12 21s-6.5-5.6-6.5-10.5a6.5 6.5 0 0 1 13 0C18.5 15.4 12 21 12 21Z" />
      <circle cx="12" cy="10.5" r="2.4" />
    </g>
  ),

  // Social icons
  instagram: (
    <g {...stroke}>
      <rect x="3.5" y="3.5" width="17" height="17" rx="5" />
      <circle cx="12" cy="12" r="4" />
      <circle cx="17.2" cy="6.8" r="0.6" fill="currentColor" />
    </g>
  ),
  facebook: (
    <path
      fill="currentColor"
      d="M13.5 21v-7.6h2.6l.4-3h-3V8.5c0-.9.3-1.5 1.5-1.5h1.6V4.3c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H8v3h2.4V21h3.1Z"
    />
  ),
  tiktok: (
    <path
      fill="currentColor"
      d="M16.6 3h-2.8v12.2a2.6 2.6 0 1 1-2.6-2.6c.3 0 .5 0 .8.1V9.8a5.4 5.4 0 1 0 4.6 5.4V9.1a6.7 6.7 0 0 0 3.9 1.3V7.6A3.9 3.9 0 0 1 16.6 3Z"
    />
  ),
  linkedin: (
    <path
      fill="currentColor"
      d="M5.2 8.6a1.8 1.8 0 1 0 0-3.6 1.8 1.8 0 0 0 0 3.6ZM3.7 10h3v10h-3V10Zm5 0h2.9v1.4c.4-.8 1.4-1.6 3-1.6 3 0 3.6 2 3.6 4.6V20h-3v-5c0-1.2 0-2.7-1.7-2.7s-1.9 1.3-1.9 2.6v5.1h-3V10Z"
    />
  ),
  x: (
    <path
      fill="currentColor"
      d="M17.8 4h2.9l-6.3 7.2L21.8 20h-5.8l-4.5-5.9L6.3 20H3.4l6.7-7.7L2.9 4h5.9l4.1 5.4L17.8 4Zm-1 14.3h1.6L7.9 5.6H6.2l10.6 12.7Z"
    />
  ),
  youtube: (
    <g>
      <rect x="2.5" y="5.5" width="19" height="13" rx="4" {...stroke} />
      <path d="m10 9.2 5 2.8-5 2.8V9.2Z" fill="currentColor" />
    </g>
  ),
  whatsapp: (
    <g {...stroke}>
      <path d="M4 20l1.2-4.1A8 8 0 1 1 8.2 19L4 20Z" />
      <path d="M9.3 8.8c.2 2.4 2.5 4.7 5 5l1-1.2-1.7-.9-.7.6a3.800 3.800 0 0 1-1.900-1.900l.6-.7-.9-1.700-1.400.8Z" />
    </g>
  ),
};

function Icon({ name, size = 18 }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      {ICONS[name] ?? null}
    </svg>
  );
}

/* Built-in placeholder logo (chef hat over a pot). Swap via brand.logoSrc. */
function DefaultLogo() {
  return (
    <svg width="52" height="44" viewBox="0 0 52 44" aria-hidden="true" fill="none" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M14 22c-5.500 0-9-3.400-9-7.500S8.600 7 13 7c1.500-3.500 5-5 9-5 3 0 5.600 1 7.500 3 1.200-.8 2.600-1.200 4-1.200 4.500 0 8 3.200 8 7.200 0 2-.8 3.800-2.200 5.200" />
      <path d="M10 25h32M13 25v6c0 5 4 9 9 9h8c5 0 9-4 9-9v-6" />
      <path d="M6 28h4M42 28h4" />
    </svg>
  );
}

/* ============================================================
   COMPONENT
   ============================================================ */
export default function Footer({ onSubscribe, config = FOOTER }) {
  const { brand, contact, columns, socials, newsletter, legal } = config;
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState("idle"); // idle | done

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!email.trim()) return;
    // Plug your newsletter provider in via the onSubscribe prop.
    if (onSubscribe) await onSubscribe(email.trim());
    setStatus("done");
    setEmail("");
  };

  const isExternal = (href = "") => /^https?:\/\//.test(href);

  return (
    <footer className="cc-footer">
      <span className="cc-arc cc-arc--tl" aria-hidden="true" />
      <span className="cc-arc cc-arc--br" aria-hidden="true" />

      <div className="cc-inner">
        <div className="cc-grid">
          {/* Brand */}
          <div className="cc-brand">
            <div className="cc-logo">
              {brand.logoSrc ? (
                <img
                  className={brand.logoOnly ? "cc-logo-img" : "cc-logo-icon"}
                  src={brand.logoSrc}
                  alt={brand.logoOnly ? brand.name : ""}
                />
              ) : (
                <DefaultLogo />
              )}
              {!brand.logoOnly && (
                <div>
                  <div className="cc-logo-name">
                    {brand.name.split(" ")[0]}{" "}
                    <span>{brand.name.split(" ").slice(1).join(" ")}</span>
                  </div>
                  <div className="cc-logo-tag">{brand.tagline}</div>
                </div>
              )}
            </div>
            <p className="cc-desc">{brand.description}</p>
            <ul className="cc-contact">
              {contact.map((c) => (
                <li key={c.text}>
                  <span className="cc-gold"><Icon name={c.icon} /></span>
                  {c.href ? <a href={c.href}>{c.text}</a> : <span>{c.text}</span>}
                </li>
              ))}
            </ul>
          </div>

          {/* Link columns */}
          {columns.map((col) => (
            <nav key={col.title} className="cc-col" aria-label={col.title}>
              <h3 className="cc-heading">{col.title}</h3>
              <ul className="cc-links">
                {col.links.map((l) => (
                  <li key={l.label}>
                    <a
                      href={l.href}
                      {...(isExternal(l.href) ? { target: "_blank", rel: "noopener noreferrer" } : {})}
                    >
                      {l.label}
                    </a>
                  </li>
                ))}
              </ul>
            </nav>
          ))}

          {/* Socials + newsletter */}
          <div className="cc-col cc-connect">
            <h3 className="cc-heading">{newsletter.title}</h3>
            <p className="cc-desc">{newsletter.text}</p>

            <ul className="cc-socials">
              {socials.map((s) => (
                <li key={s.label}>
                  <a href={s.href} target="_blank" rel="noopener noreferrer" aria-label={s.label}>
                    <Icon name={s.icon} size={20} />
                  </a>
                </li>
              ))}
            </ul>

            <form className="cc-form" onSubmit={handleSubmit}>
              <input
                type="email"
                required
                value={email}
                onChange={(e) => { setEmail(e.target.value); setStatus("idle"); }}
                placeholder={newsletter.placeholder}
                aria-label={newsletter.placeholder}
              />
              <button type="submit">{newsletter.button}</button>
            </form>
            <p className="cc-status" role="status" aria-live="polite">
              {status === "done" ? "Thanks, you're on the list." : ""}
            </p>
          </div>
        </div>

        <div className="cc-bottom">
          <span>© {new Date().getFullYear()} {legal.copyright}</span>
          <span>{legal.note}</span>
        </div>
      </div>
    </footer>
  );
}
