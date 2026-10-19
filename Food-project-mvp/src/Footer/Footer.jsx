import "./Footer.css";
import logo from "./Logo.png"; // update to your logo path

const Icon = ({ children, fill }) => (
  <svg
    viewBox="0 0 24 24"
    fill={fill ? "currentColor" : "none"}
    stroke={fill ? "none" : "currentColor"}
    strokeWidth="1.8"
    strokeLinecap="round"
    strokeLinejoin="round"
    aria-hidden="true"
  >
    {children}
  </svg>
);

export default function Footer() {
  return (
    <footer className="footer">
      <span className="footer__arc footer__arc--tl" aria-hidden="true" />
      <span className="footer__arc footer__arc--br" aria-hidden="true" />

      <div className="footer__top">
        {/* Brand */}
        <div className="footer__col footer__brand">
          <img className="footer__logo" src={logo} alt="Culinary Cart Student Marketplace" />
          <p className="footer__tagline">
            Connecting student chefs with food lovers and new opportunities.
          </p>
          <ul className="footer__contact">
            <li>
              <Icon>
                <rect x="3" y="5" width="18" height="14" rx="2" />
                <path d="M3 7l9 6 9-6" />
              </Icon>
              <a href="mailto:hello@culinarycart.co.za">hello@culinarycart.co.za</a>
            </li>
            <li>
              <Icon>
                <path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z" />
              </Icon>
              <a href="tel:+27115550184">+27 11 555 0184</a>
            </li>
            <li>
              <Icon>
                <path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z" />
                <circle cx="12" cy="10" r="3" />
              </Icon>
              <span>Pretoria, South Africa</span>
            </li>
          </ul>
        </div>

        {/* Quick links */}
        <nav className="footer__col footer__divided" aria-label="Quick links">
          <h3 className="footer__heading">Quick Links</h3>
          <ul className="footer__links">
            <li><a href="/">Home</a></li>
            <li><a href="/shop">Shop</a></li>
            <li><a href="/students">Students</a></li>
            <li><a href="/events">Events &amp; Workshops</a></li>
            <li><a href="/about">About</a></li>
          </ul>
        </nav>

        {/* Support */}
        <nav className="footer__col footer__divided" aria-label="Support">
          <h3 className="footer__heading">Support</h3>
          <ul className="footer__links">
            <li><a href="/help">Help Centre</a></li>
            <li><a href="/faqs">FAQs</a></li>
            <li><a href="/shipping">Shipping &amp; Collection</a></li>
            <li><a href="/seller-guidelines">Seller Guidelines</a></li>
            <li><a href="/privacy">Privacy Policy</a></li>
          </ul>
        </nav>

        {/* Stay connected */}
        <div className="footer__col footer__divided">
          <h3 className="footer__heading">Stay Connected</h3>
          <p className="footer__follow">
            Follow our journey and discover student-made goodness.
          </p>

          <div className="footer__social">
            <a href="#" aria-label="Instagram">
              <Icon>
                <rect x="3" y="3" width="18" height="18" rx="5" />
                <circle cx="12" cy="12" r="4" />
                <circle cx="17.2" cy="6.8" r="0.6" fill="currentColor" />
              </Icon>
            </a>
            <a href="#" aria-label="Facebook">
              <Icon fill>
                <path d="M14 8h3V4h-3a4 4 0 0 0-4 4v2H7v4h3v8h4v-8h3l1-4h-4V8a1 1 0 0 1 1-1z" />
              </Icon>
            </a>
            <a href="#" aria-label="TikTok">
              <Icon fill>
                <path d="M16 3c.3 2.4 1.8 4 4 4.2v3.2c-1.5 0-2.900-.5-4-1.300V15a6 6 0 1 1-6-6c.3 0 .7 0 1 .1v3.300a2.800 2.800 0 1 0 1.800 2.600V3H16z" />
              </Icon>
            </a>
            <a href="#" aria-label="LinkedIn">
              <Icon fill>
                <rect x="4" y="9" width="3.5" height="11" />
                <circle cx="5.75" cy="5.5" r="2" />
                <path d="M10 9h3.400v1.600c.6-1 1.800-1.900 3.600-1.900 3.400 0 4 2.200 4 5.100V20h-3.500v-5.400c0-1.300 0-2.900-1.800-2.900s-2 1.400-2 2.800V20H10z" />
              </Icon>
            </a>
          </div>

          <form className="footer__form" onSubmit={(e) => e.preventDefault()}>
            <input type="email" placeholder="Your email address" aria-label="Email address" required />
            <button type="submit">Subscribe</button>
          </form>
        </div>
      </div>

      <div className="footer__bottom">
        <span>© 2026 Culinary Cart. All rights reserved.</span>
        <span>Made with care for the next generation of chefs.</span>
      </div>
    </footer>
  );
}
