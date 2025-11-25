import React, { useState, useEffect } from 'react';
import './PlantLibrary.css';

function PlantLibrary({ apiUrl }) {
  const [plants, setPlants] = useState({});
  const [selectedPlant, setSelectedPlant] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchPlantLibrary();
  }, []);

  const fetchPlantLibrary = async () => {
    try {
      const response = await fetch(`${apiUrl}/api/plant-library`);
      const data = await response.json();
      setPlants(data);
      setLoading(false);
    } catch (err) {
      setError('Failed to load plant library');
      setLoading(false);
      console.error('Error fetching plants:', err);
    }
  };

  if (loading) {
    return <div className="library-loading">Loading plant library...</div>;
  }

  if (error) {
    return <div className="library-error">{error}</div>;
  }

  return (
    <div className="library-container">
      <div className="library-header">
        <h2>🌿 Plant Care Guide</h2>
        <p>Learn how to care for popular garden plants</p>
      </div>

      <div className="library-content">
        <div className="plants-grid">
          {Object.entries(plants).map(([key, plant]) => (
            <div
              key={key}
              className={`plant-card ${selectedPlant?.name === plant.name ? 'selected' : ''}`}
              onClick={() => setSelectedPlant(plant)}
            >
              <div className="plant-card-header">
                <h3>{plant.name}</h3>
              </div>
              <p className="plant-preview">Click to view care guide</p>
            </div>
          ))}
        </div>

        {selectedPlant && (
          <div className="plant-detail">
            <button 
              className="close-detail"
              onClick={() => setSelectedPlant(null)}
            >
              ✕
            </button>
            <h2>{selectedPlant.name} 🌱</h2>
            
            <div className="care-info">
              <div className="info-section">
                <h4>💧 Watering</h4>
                <p>{selectedPlant.watering}</p>
              </div>

              <div className="info-section">
                <h4>☀️ Light</h4>
                <p>{selectedPlant.light}</p>
              </div>

              <div className="info-section">
                <h4>🌡️ Temperature</h4>
                <p>{selectedPlant.temp}</p>
              </div>

              <div className="info-section">
                <h4>🌍 Soil</h4>
                <p>{selectedPlant.soil}</p>
              </div>

              {selectedPlant.common_issues && (
                <div className="info-section">
                  <h4>⚠️ Common Issues</h4>
                  <ul className="issues-list">
                    {selectedPlant.common_issues.map((issue, index) => (
                      <li key={index}>{issue.replace(/_/g, ' ')}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default PlantLibrary;
