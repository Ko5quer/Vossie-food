import CartTableHeader from "./CartTableHeader/Carttableheader.jsx";
import Cart from "./Cart/Cart.jsx";
import Ordersummary from "./OrderSumary/Ordersummary.jsx";

const SHIPPING = 10;

export default function Carts({ items = [], onQuantityChange, onRemove, onCheckout }) {
  const subtotal = items.reduce((sum, i) => sum + i.price * i.quantity, 0);

  return (
    <>
      <CartTableHeader />
      <Cart
        items={items}
        onQuantityChange={onQuantityChange}
        onRemove={onRemove}
      />
      <Ordersummary
        subtotal={subtotal}
        shipping={items.length ? SHIPPING : 0}
        onCheckout={onCheckout}
      />
    </>
  );
}