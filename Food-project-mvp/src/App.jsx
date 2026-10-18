
import WavyBanner from "./Banner/WavyBanner.jsx";
import Header from "./Nav_bar/Header.jsx";
import ChefDisplay from "./Chef_display/chef_display.jsx";
import Features from "./Features/Features.jsx";
import Categories from "./Categories/Categories.jsx"
import About from "./About/About.jsx"
function App() {
    return (
        <>
            <WavyBanner />
            <Header />
            <ChefDisplay />
            <Features/>
            <Categories/>
            <About/>
        </>
    );
}

export default App;
