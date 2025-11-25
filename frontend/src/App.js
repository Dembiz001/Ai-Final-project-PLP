import React, { useState } from 'react';
import axios from 'axios';
import './App.css';
import ImageUpload from './components/ImageUpload';
import DiagnosisResult from './components/DiagnosisResult';
import PlantLibrary from './components/PlantLibrary';
import Header from './components/Header';
import Navigation from './components/Navigation';

function App() {
  const [currentPage, setCurrentPage] = useState('home');
  const [analysisResult, setAnalysisResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  const handleImageUpload = async (file) => {
    setLoading(true);
    setError(null);
    
    try {
      const formData = new FormData();
      formData.append('image', file);
      
      const response = await axios.post(
        `${API_BASE_URL}/api/analyze`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      );
      
      setAnalysisResult(response.data);
      setCurrentPage('results');
    } catch (err) {
      setError(err.response?.data?.error || 'Failed to analyze image. Please try again.');
      console.error('Upload error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Header />
      <Navigation currentPage={currentPage} onPageChange={setCurrentPage} />
      
      <div className="main-container">
        {currentPage === 'home' && (
          <section className="home-section">
            <div className="hero">
              <h2>Diagnose Your Plants with AI</h2>
              <p>Upload a photo of your plant to get instant diagnosis and care recommendations</p>
            </div>
            <ImageUpload 
              onUpload={handleImageUpload} 
              loading={loading}
            />
            {error && <div className="error-message">{error}</div>}
          </section>
        )}
        
        {currentPage === 'results' && analysisResult && (
          <DiagnosisResult 
            result={analysisResult}
            onNewAnalysis={() => {
              setCurrentPage('home');
              setAnalysisResult(null);
            }}
          />
        )}
        
        {currentPage === 'library' && (
          <PlantLibrary apiUrl={API_BASE_URL} />
        )}
      </div>
    </div>
  );
}

export default App;
