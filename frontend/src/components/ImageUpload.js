import React, { useRef, useState } from 'react';
import './ImageUpload.css';

function ImageUpload({ onUpload, loading }) {
  const fileInputRef = useRef(null);
  const [preview, setPreview] = useState(null);

  const handleFileSelect = (event) => {
    const file = event.target.files?.[0];
    if (file) {
      handleFile(file);
    }
  };

  const handleFile = (file) => {
    // Validate file type
    if (!['image/png', 'image/jpeg', 'image/gif'].includes(file.type)) {
      alert('Please select a valid image file (PNG, JPG, JPEG, GIF)');
      return;
    }

    // Validate file size (5MB max)
    if (file.size > 5 * 1024 * 1024) {
      alert('File size must be less than 5MB');
      return;
    }

    // Show preview
    const reader = new FileReader();
    reader.onload = (e) => {
      setPreview(e.target.result);
    };
    reader.readAsDataURL(file);

    // Upload file
    onUpload(file);
  };

  const handleDragOver = (e) => {
    e.preventDefault();
    e.currentTarget.classList.add('drag-over');
  };

  const handleDragLeave = (e) => {
    e.currentTarget.classList.remove('drag-over');
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.currentTarget.classList.remove('drag-over');
    const file = e.dataTransfer.files?.[0];
    if (file) {
      handleFile(file);
    }
  };

  return (
    <div className="upload-container">
      <div
        className="upload-area"
        onClick={() => fileInputRef.current?.click()}
        onDragOver={handleDragOver}
        onDragLeave={handleDragLeave}
        onDrop={handleDrop}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept="image/*"
          onChange={handleFileSelect}
          style={{ display: 'none' }}
        />

        {preview && !loading ? (
          <div className="preview-container">
            <img src={preview} alt="Preview" className="preview-image" />
            <p className="preview-text">Click or drag to replace</p>
          </div>
        ) : loading ? (
          <div className="loading-container">
            <div className="spinner"></div>
            <p>Analyzing your plant...</p>
          </div>
        ) : (
          <div className="upload-prompt">
            <span className="upload-icon">📷</span>
            <h3>Upload Plant Photo</h3>
            <p>Click here or drag and drop an image</p>
            <p className="file-info">PNG, JPG, JPEG, or GIF • Max 5MB</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default ImageUpload;
