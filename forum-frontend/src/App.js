import React, { Component, Fragment } from "react"; //(7)
import Header from "./components/Header";
import Home from "./components/Home";
import Footer from "./components/Footer";



class App extends Component {
  render() {
    return (
        <Fragment>
            <Header />
            <Home />
            <Footer />
        </Fragment>

    );
  }
}
export default App; 