import React from 'react';
// import logo from './logo.svg';
import './App.css';
import NameInput from './components/NameInput'

function App() {
  return (
    <div className="App">
      <header id="sd-topbar" class="sd-container style-module--top-bar--8EncK  style-module--revealed--23Rha">
        <div class="sd-container-inner">
          <div class="style-module--inner--1qRHH">
            <a aria-label="Go to homepage" class="style-module--logo--10oUe" href="/"><h1>Namify</h1></a>
            <nav aria-label="site navigation" class="style-module--desktop-nav--22t5t">
              <ul class="unstyled-list style-module--navigation--Xeg87">
                <li><a class="t-ui-2 style-module--item--2doqO " href="/about"><span>About</span></a></li>
                <li><a class="t-ui-2 style-module--item--2doqO " href="/hire-me"><span>Hire me!</span></a></li>
              </ul>
            </nav>
          </div>
        </div>
      </header>

      <body>
        <NameInput />
      </body>
    </div>
  );
}

export default App;
