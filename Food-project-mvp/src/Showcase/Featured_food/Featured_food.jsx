
import DishFeature from "./DishFeature";

import Berry from "./berry.jpg";
import Chocolate from "./chocolate.jpg";
import Harvest from "./Harvest.jpg";
import Lasagna from "./Lasagna.jpg";

const dishes = [
  {
    image: Lasagna,
    alt: "Plated lasagna with garlic ciabatta toasts",
    title: "Classic comforts Lasagna",
    description:
      "Indulgent layered pasta baked to perfection with a rich meat sauce and beautifully caramelized cheese. Plated with vibrant marinara and accompanied by garlic ciabatta toasts for the perfect dip.",
    swirl: "left",
    tick: true,
  },
  {
    image: Harvest,
    alt: "Stacked grilled vegetables with beet lace on a white plate",
    title: "Harvest Symphony",
    description:
      "An intricate stack of layered, grilled vegetables crowned with a golden gratin topping, elevated by mushroom cream sauce, balsamic glaze, and vibrant carrot and pea puree.",
    swirl: "right",
  },
  {
    image: Chocolate,
    alt: "Chocolate tart topped with raspberries",
    title: "Chocolate Raspberry",
    description:
      "An elegant tart featuring a rich dark chocolate pastry shell filled with smooth chocolate ganache, topped with fresh raspberries and caramelized sugar.",
    swirl: "right",
  },
  {
    image: Berry,
    alt: "Berry cheesecake topped with strawberry compote",
    title: "Summer Harvest Cheesecake",
    description:
      "A velvety-smooth cheesecake slice topped with glossy strawberry compote and macerated fruit, finished with freeze-dried strawberry pieces.",
    swirl: "right",
  },
];

export default function Featured_food() {
  return (
    <main>
      {dishes.map((dish) => (
        <DishFeature key={dish.title} {...dish} />
      ))}
    </main>
  );
}

