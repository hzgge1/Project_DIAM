import React from 'react';
import '../static/style/style_react.css';
import myImage from '../static/images/clarify_logo.png';
// import about from 'forum/templates/about.html';
// import login from 'forum/templates/login_form.html';
// import signup from 'forum/templates/sign_up.html';

function Header() {
    return (

        <header>
      <nav>
        <a href="http://127.0.0.1:8000/forum/">
            <img src={myImage} alt="Logo" />
        </a>

        {/*<form className="search-form" action="/forum/pesquisa_questoes" method="post">*/}
        {/*  <input type="text" name="tags" placeholder="Search Tags .." />*/}
        {/*  <input type="submit" value="🔍" />*/}
        {/*</form>*/}

        <div className="button_nav_list">
          <a href="http://127.0.0.1:8000/forum/about"><button>About</button></a>
          <a href="http://127.0.0.1:8000/forum/login"><button>Login</button></a>
          <a href="http://127.0.0.1:8000/forum/sign_up"><button>Sign Up</button></a>
        </div>
      </nav>
    </header>


    );
}
export default Header;