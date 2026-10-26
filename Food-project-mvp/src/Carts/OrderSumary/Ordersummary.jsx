import "./OrderSummary.css";

const formatRand = (amount) => `R${amount.toFixed(2).replace(/\.00$/, "")}`;

/**
 * subtotal: number  - sum of item totals
 * shipping: number  - shipping fee
 * onCheckout: () => void
 */
export default function OrderSummary({ subtotal = 0, shipping = 0, onCheckout }) {
  const total = subtotal + shipping;

  return (
    <section className="order-summary" aria-labelledby="order-summary-title">
      <h2 id="order-summary-title" className="order-summary__title">
        Order Summary
      </h2>

      <dl className="order-summary__rows">
        <div className="order-summary__row">
          <dt>Subtotal</dt>
          <dd>{formatRand(subtotal)}</dd>
        </div>
        <div className="order-summary__row">
          <dt>Shipping</dt>
          <dd>{formatRand(shipping)}</dd>
        </div>
      </dl>

      <dl className="order-summary__rows order-summary__rows--total">
        <div className="order-summary__row">
          <dt>Estimated total</dt>
          <dd>{formatRand(total)}</dd>
        </div>
      </dl>

      <button
        type="button"
        className="order-summary__checkout"
        onClick={onCheckout}
      >
        Proceed to checkout
      </button>
    </section>
  );
}