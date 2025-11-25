import React from 'react';
import './DiagnosisResult.css';

function DiagnosisResult({ result, onNewAnalysis }) {
  const getConfidenceColor = (confidence) => {
    if (confidence >= 0.8) return '#4caf50';
    if (confidence >= 0.6) return '#ff9800';
    return '#f44336';
  };

  const getConditionEmoji = (condition) => {
    const emojis = {
      'healthy': '✅',
      'fungal_disease': '🍄',
      'bacterial_disease': '🦠',
      'viral_disease': '🦠',
      'pest_damage': '🐛',
      'nutrient_deficiency': '⚗️',
      'water_stress': '💧'
    };
    return emojis[condition] || '🌿';
  };

  return (
    <div className="diagnosis-container">
      <div className="diagnosis-card">
        <div className="diagnosis-header">
          <span className="condition-emoji">
            {getConditionEmoji(result.condition)}
          </span>
          <h2>{result.diagnosis}</h2>
        </div>

        <div className="diagnosis-content">
          <p className="description">{result.description}</p>

          <div className="confidence-section">
            <label>Analysis Confidence:</label>
            <div className="confidence-bar">
              <div
                className="confidence-fill"
                style={{
                  width: `${result.confidence * 100}%`,
                  backgroundColor: getConfidenceColor(result.confidence)
                }}
              ></div>
            </div>
            <span className="confidence-text">
              {(result.confidence * 100).toFixed(1)}%
            </span>
          </div>

          <div className="recommendations-section">
            <h3>🌟 Recommended Actions</h3>
            <ul className="actions-list">
              {result.actions.map((action, index) => (
                <li key={index}>
                  <span className="action-number">{index + 1}</span>
                  <span className="action-text">{action}</span>
                </li>
              ))}
            </ul>
          </div>

          <div className="info-box">
            <h4>💡 Tip</h4>
            <p>
              Monitor your plant regularly and check for improvements within 1-2 weeks. 
              If the condition worsens, consider consulting a local gardening expert.
            </p>
          </div>
        </div>

        <div className="action-buttons">
          <button className="btn btn-primary" onClick={onNewAnalysis}>
            📸 Analyze Another Plant
          </button>
        </div>
      </div>
    </div>
  );
}

export default DiagnosisResult;
