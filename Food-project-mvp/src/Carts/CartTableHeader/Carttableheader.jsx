import "./CartTableHeader.css";

const COLUMNS = ["Product", "Price", "Quantity", "Total"];

export default function CartTableHeader({ columns = COLUMNS }) {
  return (
    <div className="cart-header" role="row">
      {columns.map((label) => (
        <span key={label} className="cart-header__cell" role="columnheader">
          {label}
        </span>
      ))}
    </div>
  );
}