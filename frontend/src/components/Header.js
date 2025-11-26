import React from 'react';
import './Header.css';

function Header() {
  return (
    <header className="app-header">
      <div className="header-container">
        <div className="logo">
          <span className="logo-icon">🌱</span>
          <h1>Gardener.ai</h1>
        </div>
        <p className="tagline">AI-Powered Plant Care for Every Gardener</p>
      </div>
    </header>
  );
}

export default Header;
