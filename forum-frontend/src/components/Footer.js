import React from "react";
import '../static/style_react.css';

function Footer(){
    return (
        <footer>
            <p>1980 Dahlia St Denver, CO 80220, EUA</p>
            <p>39.747371, -104.931689</p>
            <div className="social-icons">
                <a href="https://www.facebook.com/"><i className="fab fa-facebook"></i></a>
                <a href="https://www.youtube.com/"><i className="fab fa-youtube"></i></a>
                <a href="https://twitter.com/"><i className="fab fa-twitter"></i></a>
                <a href="https://www.linkedin.com/"><i className="fab fa-linkedin"></i></a>
            </div>
        </footer>
    );
}

export default Footer;