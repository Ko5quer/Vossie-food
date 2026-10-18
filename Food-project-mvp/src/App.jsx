
import Main_page from "./Main_page/Main_page.jsx";
import WavyBanner from "./Banner/WavyBanner.jsx";
import Header from "./Nav_bar/Header.jsx";
import About from "./About/About.jsx";
import Showcase from "./Showcase/Showcase.jsx";
function App() {
    return (
        <>
            <WavyBanner/>
            <Header/>
            <Main_page/>
            <Showcase/>
            <About/>
        </>
    );
}

export default App;
