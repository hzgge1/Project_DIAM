import React from 'react';
import '../static/style/style_react.css';
function Header() {
    return (

        <header>
      <nav>
        <img src="https://keystoneacademic-res.cloudinary.com/image/upload/q_auto,f_auto,w_743,c_limit/element/1
1/111948_2.jpg" alt="Logo" />

        <form className="search-form" action="/forum/pesquisa_questoes" method="post">
          <input type="text" name="tags" placeholder="Search Tags .." />
          <input type="submit" value="🔍" />
        </form>

        <div className="button_nav_list">
          <a href="/forum/about"><button>About</button></a>

          <a href="/forum/logout"><button>Logout</button></a>

          <a href="/forum/login"><button>Login</button></a>
          <a href="/forum/signup"><button>Sign Up</button></a>
        </div>
      </nav>
    </header>


    );
}
export default Header;