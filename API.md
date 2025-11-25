# API Documentation - AI Garden Assistant

## Base URL
Development: `http://localhost:5000`
Production: `https://api.aigarden.com` (when deployed)

## Authentication
Currently no authentication required. Future versions will support JWT tokens.

---

## Endpoints

### 1. Health Check
Check if the backend is running.

**Endpoint:** `GET /api/health`

**Response:**
```json
{
  "status": "healthy",
  "service": "AI Gardening Assistant Backend",
  "model_loaded": true
}
```

---

### 2. Plant Analysis (Main Feature)
Upload an image and get plant diagnosis.

**Endpoint:** `POST /api/analyze`

**Request:**
- Content-Type: `multipart/form-data`
- Parameters:
  - `image` (file, required): Image file (PNG, JPG, JPEG, GIF)
  - Max size: 5MB

**cURL Example:**
```bash
curl -X POST http://localhost:5000/api/analyze \
  -F "image=@plant.jpg"
```

**Response (Success):**
```json
{
  "success": true,
  "condition": "fungal_disease",
  "confidence": 0.87,
  "diagnosis": "Fungal Disease Detected",
  "description": "Your plant shows signs of fungal infection.",
  "actions": [
    "Remove affected leaves",
    "Improve air circulation around the plant",
    "Apply fungicide (neem oil or sulfur spray)",
    "Reduce watering frequency",
    "Ensure soil is not waterlogged"
  ]
}
```

**Response (Error):**
```json
{
  "error": "No image provided"
}
```

**Error Codes:**
- 400: Bad request (no file, invalid type, etc.)
- 413: File too large (>5MB)
- 500: Server error

---

### 3. Plant Library - Get All Plants
Retrieve information for all plants in the library.

**Endpoint:** `GET /api/plant-library`

**Response:**
```json
{
  "tomato": {
    "name": "Tomato",
    "watering": "1 inch per week, more during fruiting",
    "light": "6-8 hours of direct sunlight",
    "temp": "65-75°F (18-24°C)",
    "soil": "Rich, well-draining loam",
    "common_issues": ["fungal_disease", "pest_damage", "water_stress"]
  },
  "lettuce": {
    "name": "Lettuce",
    "watering": "Keep soil consistently moist",
    "light": "4-6 hours of sunlight (less in summer)",
    "temp": "60-70°F (15-21°C)",
    "soil": "Light, well-draining loam",
    "common_issues": ["bacterial_disease", "pest_damage"]
  }
  // ... more plants
}
```

---

### 4. Plant Library - Get Specific Plant
Get care information for a specific plant.

**Endpoint:** `GET /api/plant-library/<plant_name>`

**Parameters:**
- `plant_name` (string, required): Name of plant (e.g., "tomato", "rose")

**Response:**
```json
{
  "name": "Tomato",
  "watering": "1 inch per week, more during fruiting",
  "light": "6-8 hours of direct sunlight",
  "temp": "65-75°F (18-24°C)",
  "soil": "Rich, well-draining loam",
  "common_issues": ["fungal_disease", "pest_damage", "water_stress"]
}
```

**Error Response (Plant not found):**
```json
{
  "error": "Plant not found"
}
```

---

### 5. Get All Recommendations
Retrieve recommendation templates for all conditions.

**Endpoint:** `GET /api/recommendations`

**Response:**
```json
{
  "healthy": {
    "title": "Your plant looks healthy!",
    "description": "Your plant appears to be in great condition.",
    "actions": [
      "Continue regular watering schedule",
      "Maintain current light conditions",
      "Monitor for any changes in leaf color"
    ]
  },
  "fungal_disease": {
    "title": "Fungal Disease Detected",
    "description": "Your plant shows signs of fungal infection.",
    "actions": [
      "Remove affected leaves",
      // ... more actions
    ]
  }
  // ... more conditions
}
```

---

## Plant Conditions

The AI can detect the following plant conditions:

1. **healthy** - Plant is in good condition
2. **fungal_disease** - Fungal infections (powdery mildew, rust, etc.)
3. **bacterial_disease** - Bacterial infections
4. **viral_disease** - Viral infections
5. **pest_damage** - Pest or insect damage (aphids, spider mites, etc.)
6. **nutrient_deficiency** - Lacks essential nutrients (N, P, K, etc.)
7. **water_stress** - Over or under-watering issues

---

## Available Plants in Library

- tomato
- lettuce
- rose
- basil
- pepper

---

## Error Handling

All errors return appropriate HTTP status codes with JSON response:

```json
{
  "error": "Error description"
}
```

### Common Error Codes:
- `400` - Bad Request (missing fields, invalid format)
- `404` - Not Found (plant not found)
- `413` - Payload Too Large (file exceeds 5MB)
- `500` - Internal Server Error

---

## Rate Limiting

Currently unlimited. Production deployment will implement rate limiting.

---

## CORS

CORS is enabled to allow requests from:
- Development: `*` (all origins)
- Production: Specific frontend domain

---

## Image Format Requirements

- **Formats:** PNG, JPG, JPEG, GIF
- **Max Size:** 5MB
- **Recommended Size:** 224x224 pixels (but any size works)
- **Quality:** High quality for better accuracy

---

## JavaScript/Fetch Example

```javascript
const formData = new FormData();
formData.append('image', imageFile);

const response = await fetch('http://localhost:5000/api/analyze', {
  method: 'POST',
  body: formData
});

const result = await response.json();
console.log(result);
```

---

## Python/Requests Example

```python
import requests

files = {'image': open('plant.jpg', 'rb')}
response = requests.post('http://localhost:5000/api/analyze', files=files)
result = response.json()
print(result)
```

---

## Future Endpoints (Planned)

- `POST /api/user/register` - User registration
- `POST /api/user/login` - User login
- `GET /api/user/history` - Get diagnosis history
- `POST /api/feedback` - Submit feedback
- `POST /api/plant-sighting` - Report plant sighting
- `GET /api/articles` - Get gardening articles

---

## Support

For API issues or questions:
1. Check response error messages
2. Review this documentation
3. Open an issue on GitHub
4. Contact support team

---

Last Updated: November 2025
