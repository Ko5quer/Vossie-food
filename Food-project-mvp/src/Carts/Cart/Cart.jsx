import "./Cart.css";

const formatRand = (amount) => `R${amount.toFixed(2).replace(/\.00$/, "")}`;

function QuantityStepper({ name, quantity, onChange }) {
  return (
    <div className="qty" role="group" aria-label={`Quantity for ${name}`}>
      <button
        type="button"
        className="qty__btn"
        onClick={() => onChange(quantity - 1)}
        aria-label={`Decrease quantity of ${name}`}
      >
        -
      </button>
      <span className="qty__value" aria-live="polite">
        {quantity}
      </span>
      <button
        type="button"
        className="qty__btn"
        onClick={() => onChange(quantity + 1)}
        aria-label={`Increase quantity of ${name}`}
      >
        +
      </button>
    </div>
  );
}

function CartRow({ item, onQuantityChange, onRemove }) {
  const { id, name, image, price, quantity } = item;

  // Dropping below 1 removes the item from the cart
  const handleChange = (next) =>
    next < 1 ? onRemove(id) : onQuantityChange(id, next);

  return (
    <li className="cart-row">
      <div className="cart-row__product">
        <img className="cart-row__image" src={image} alt={name} />
        <p className="cart-row__name">{name}</p>
      </div>

      <span className="cart-row__price">{formatRand(price)}</span>

      <QuantityStepper name={name} quantity={quantity} onChange={handleChange} />

      <span className="cart-row__total">{formatRand(price * quantity)}</span>
    </li>
  );
}

/**
 * items: [{ id, name, image, price, quantity }]
 * onQuantityChange(id, newQuantity)
 * onRemove(id)
 */
export default function Cart({ items = [], onQuantityChange, onRemove }) {
  return (
    <section className="cart" aria-label="Your cart">
      {items.length === 0 ? (
        <p className="cart__empty">Your cart is empty. Add something tasty.</p>
      ) : (
        <ul className="cart__list">
          {items.map((item) => (
            <CartRow
              key={item.id}
              item={item}
              onQuantityChange={onQuantityChange}
              onRemove={onRemove}
            />
          ))}
        </ul>
      )}
    </section>
  );
}