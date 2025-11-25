import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="app-header">
      <div className="header-container">
        <div className="logo">
          <span className="logo-icon">🌱</span>
          <h1>AI Garden Assistant</h1>
        </div>
        <p className="tagline">Intelligent Plant Care at Your Fingertips</p>
      </div>
    </header>
  );
}

export default Header;
