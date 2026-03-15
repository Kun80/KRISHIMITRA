# 🚀 KrishiMitra - Hackathon Deployment Guide

## Quick Deployment Checklist

### Before Presentation
- [ ] Test all features in the browser
- [ ] Verify crop prediction works with sample data
- [ ] Test disease detection with sample images
- [ ] Check responsive design on mobile
- [ ] Verify all links and navigation work
- [ ] Check console for JavaScript errors

### System Requirements
- Python 3.8+
- Node.js (optional, for advanced features)
- Modern web browser (Chrome, Firefox, Safari)
- ~500MB disk space

## Step-by-Step Deployment

### 1. Environment Setup
```bash
# Clone repository
git clone <your-repo-url>
cd krishimitra

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Quick Test
```bash
# Test ML model
cd models
python crop_prediction_demo.py

# Go back to root
cd ..
```

### 3. Launch Dashboard
```bash
# Method 1: Direct file opening
# Open app/index.html in your browser

# Method 2: Local server (recommended)
cd app
python -m http.server 8000
# Visit: http://localhost:8000

# Method 3: Using Python 3.7+
python -m http.server --directory . 8000
```

## Feature Testing Checklist

### Crop Prediction
- **Test Input**: N=90, P=42, R=200
- **Expected Output**: Recommended Crop + Price
- **Valid Ranges**: N(0-200), P(0-200), R(0-500)

### Disease Detection
- **Test**: Upload any leaf image
- **Expected**: Disease name + Pesticide recommendation
- **Supported Formats**: JPG, PNG, WebP

### Chart Display
- **Should show**: Rice and Maize price trends
- **Interactive**: Hover over data points

### Vendor Locator
- **Should display**: Google Maps embed
- **Should show**: 2 vendor cards with discounts

### Responsive Design
- **Desktop**: Full grid layout
- **Tablet**: 2-column grid
- **Mobile**: Single column, stacked

## Performance Optimization

### Frontend
- Chart.js: Already minified via CDN
- Images: Keep under 2MB
- CSS: Single file (fully loaded)
- JS: Modular and commented

### Backend
- Model: Lightweight Decision Tree
- Prediction time: <100ms
- Memory usage: ~5MB

## Browser Compatibility
- Chrome 90+: ✅ Fully supported
- Firefox 88+: ✅ Fully supported
- Safari 14+: ✅ Fully supported
- Edge 90+: ✅ Fully supported
- Mobile browsers: ✅ Responsive design

## Common Issues & Fixes

### Issue: Chart not displaying
**Solution**: Check Chart.js CDN is loaded
```javascript
console.log(typeof Chart); // Should be 'function'
```

### Issue: Prediction not working
**Solution**: Verify input validation
```javascript
// Check browser console for errors
// Ensure all fields are filled
// Check value ranges
```

### Issue: CORS errors on local server
**Solution**: Use `python -m http.server 8000` instead of opening file directly

### Issue: Disease detection not showing results
**Solution**: 
- Use JPG or PNG images
- Check file size (should be <5MB)
- Verify JavaScript is enabled

## Hackathon Demo Script

### 1. Introduction (1 min)
- Show dashboard UI
- Highlight responsive design
- Explain problem being solved

### 2. Live Demo (3-4 mins)

#### Crop Prediction
```
- Enter: Nitrogen=85, Phosphorus=40, Rainfall=180
- Click: "Predict Crop"
- Show: "Rice Recommended" + Market price
- Explain: Based on ML decision tree model
```

#### Disease Detection
```
- Click camera button
- Upload leaf image
- Show: Disease detected + pesticide recommendation
- Explain: Powered by image classification
```

#### Price Trends
```
- Point to Chart.js visualization
- Show: Historical prices for 2 crops
- Explain: Helps farmers plan harvest timing
```

#### Vendor Locator
```
- Show: Google Maps integration
- Display: Nearby vendors with discounts
- Explain: Direct farmer-vendor connection

### 3. Technical Highlights (1-2 mins)
- Full-stack application (Frontend + Backend)
- Real ML model integration
- Responsive UI
- Real-time data processing

### 4. Future Roadmap (1 min)
- Deep learning disease detection
- Market price prediction
- Mobile app
- Voice interface

## Deployment to Cloud (Optional)

### Heroku Deployment
```bash
# Install Heroku CLI
# Create Procfile
echo "web: python -m http.server 8000" > Procfile

# Deploy
heroku create krishimitra
git push heroku main
```

### GitHub Pages (Frontend only)
```bash
# Copy app folder contents
# Push to gh-pages branch
# Access at: username.github.io/krishimitra
```

### AWS / Google Cloud
See docs/CLOUD_DEPLOYMENT.md for detailed instructions

## Support During Hackathon

### Pre-Presentation
- Test on judging device/screen
- Bring backup laptop
- Have offline copy ready
- Ensure WiFi/connectivity works

### During Presentation
- Keep slides minimal
- Let the app do the talking
- Have sample data ready
- Be ready to answer technical questions

### Post-Presentation
- Share GitHub link
- Provide installation instructions
- Offer to answer follow-up questions
- Get feedback for improvements

## Success Metrics

✅ App loads without errors  
✅ All features work as expected  
✅ Responsive on all devices  
✅ Fast performance (<2s load)  
✅ Clear UI/UX  
✅ Solves real farmer problem  
✅ Scalable architecture  

## Resources

- [Decision Tree Classifier Docs](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Chart.js Documentation](https://www.chartjs.org/)
- [Font Awesome Icons](https://fontawesome.com/)
- [Google Fonts API](https://fonts.google.com/)

---
**Good luck at the hackathon! 🎯**
