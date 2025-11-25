import React from 'react';
import './Navigation.css';

function Navigation({ currentPage, onPageChange }) {
  return (
    <nav className="navigation">
      <div className="nav-container">
        <button 
          className={`nav-link ${currentPage === 'home' ? 'active' : ''}`}
          onClick={() => onPageChange('home')}
        >
          <span className="nav-icon">📸</span>
          Diagnose
        </button>
        <button 
          className={`nav-link ${currentPage === 'library' ? 'active' : ''}`}
          onClick={() => onPageChange('library')}
        >
          <span className="nav-icon">📚</span>
          Plant Library
        </button>
      </div>
    </nav>
  );
}

export default Navigation;
