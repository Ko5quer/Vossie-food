
import Main_page from "./Main_page/Main_page.jsx";
import WavyBanner from "./Banner/WavyBanner.jsx";
import Header from "./Nav_bar/Header.jsx";
import About from "./About/About.jsx";
import Showcase from "./Showcase/Showcase.jsx";
import Footer from "./Footer/Footer.jsx";
import Menu from "./Menu/Menu.jsx";
import {BrowserRouter, Routes, Route} from "react-router";
function App() {
    return (
        <BrowserRouter>
            <WavyBanner/>
            <Header/>
            <Routes>
                 <Route path="/" element={<Main_page />}/>
                 <Route path="/showcase" element={<Showcase/>}/>
                 <Route path = "/shop" element = {<Menu/>}/>
                 <Route path = "/about" element = {<About/>}/>
            </Routes>
            {/*<About/>*/}
            {/*<Menu/>*/}
            {/*<Footer/>*/}
        </BrowserRouter>
    );
}

export default App;
