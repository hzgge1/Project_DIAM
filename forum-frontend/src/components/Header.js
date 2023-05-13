import React from 'react';
import '../static/style_react.css';
function Header() {
    return (

        <header>
      <nav>
        <a href="/"><img src="forum/static/images/clarify_logo.png" alt="Logo" /></a>

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