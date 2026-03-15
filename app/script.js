// Crop Prediction Data
const cropData = {
  'rice': { price: 2100, rainfall: 180 },
  'maize': { price: 1800, rainfall: 120 },
  'peas': { price: 1500, rainfall: 100 },
  'wheat': { price: 2000, rainfall: 150 }
};

/**
 * Validate input fields
 */
function validateInputs(n, p, r) {
  if (n === '' || p === '' || r === '') {
    showError('Please fill all fields');
    return false;
  }

  const nitrogen = parseFloat(n);
  const phosphorus = parseFloat(p);
  const rainfall = parseFloat(r);

  if (nitrogen < 0 || nitrogen > 200 || phosphorus < 0 || phosphorus > 200 || rainfall < 0 || rainfall > 500) {
    showError('Please enter valid values within specified ranges');
    return false;
  }

  return true;
}

/**
 * Show error message
 */
function showError(message) {
  const resultDiv = document.getElementById("cropResult");
  resultDiv.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${message}`;
  resultDiv.style.borderLeftColor = '#e74c3c';
  resultDiv.style.backgroundColor = '#fdeef0';
  resultDiv.style.color = '#e74c3c';
  resultDiv.classList.add('show');
}

/**
 * Show success message
 */
function showSuccess(message) {
  const resultDiv = document.getElementById("cropResult");
  resultDiv.innerHTML = `<i class="fas fa-check-circle"></i> ${message}`;
  resultDiv.style.borderLeftColor = '#27ae60';
  resultDiv.style.backgroundColor = '#eafaf1';
  resultDiv.style.color = '#27ae60';
  resultDiv.classList.add('show');
}

/**
 * Predict crop based on soil parameters
 */
function predictCrop() {
  const n = document.getElementById("n").value;
  const p = document.getElementById("p").value;
  const r = document.getElementById("r").value;

  if (!validateInputs(n, p, r)) {
    return;
  }

  const nitrogen = parseFloat(n);
  const phosphorus = parseFloat(p);
  const rainfall = parseFloat(r);

  // Simple logic to determine crop (can be replaced with actual ML model call)
  let predictedCrop = 'rice';
  let price = '₹2100';

  if (rainfall < 120) {
    predictedCrop = 'wheat';
    price = '₹2000';
  } else if (rainfall < 150) {
    predictedCrop = 'maize';
    price = '₹1800';
  } else if (nitrogen < 40) {
    predictedCrop = 'peas';
    price = '₹1500';
  }

  // Update cards
  document.getElementById("cropCard").innerHTML = predictedCrop.charAt(0).toUpperCase() + predictedCrop.slice(1);
  document.getElementById("priceCard").innerHTML = price + ' / quintal';

  // Show success message
  showSuccess(`Recommended Crop: <strong>${predictedCrop.toUpperCase()}</strong> | Expected Price: ${price}`);

  // Clear inputs
  setTimeout(() => {
    document.getElementById("n").value = '';
    document.getElementById("p").value = '';
    document.getElementById("r").value = '';
  }, 1500);
}

/**
 * Open camera box for disease detection
 */
function openCamera() {
  const cameraBox = document.getElementById("cameraBox");
  cameraBox.classList.toggle('show');
}

/**
 * Close camera box
 */
function closeCameraBox() {
  const cameraBox = document.getElementById("cameraBox");
  cameraBox.classList.remove('show');
}

/**
 * Detect disease from uploaded image (Mock implementation)
 */
function detectDisease(event) {
  if (!event.target.files || !event.target.files[0]) {
    return;
  }

  const file = event.target.files[0];

  // Validate file
  if (!file.type.startsWith('image/')) {
    alert('Please upload a valid image file');
    return;
  }

  // Mock disease detection (in production, this would call an API)
  const diseases = ['Tomato Early Blight', 'Powdery Mildew', 'Leaf Spot', 'Rust'];
  const pesticides = ['Mancozeb Spray', 'Sulfur Powder', 'Copper Fungicide', 'Neem Oil'];

  const randomDisease = diseases[Math.floor(Math.random() * diseases.length)];
  const randomPesticide = pesticides[Math.floor(Math.random() * pesticides.length)];

  // Update disease detection results
  document.getElementById("diseaseResult").innerHTML =
    `<strong>Disease Detected:</strong> ${randomDisease} <br><i class="fas fa-info-circle"></i> Confidence: 87%`;

  document.getElementById("pesticideResult").innerHTML =
    `<strong>Recommended Pesticide:</strong> ${randomPesticide} <br><i class="fas fa-leaf"></i> Application: 2-3 sprays at 7-day intervals`;

  document.getElementById("diseaseCard").innerHTML = randomDisease.split(' ')[0];

  // Close camera box
  setTimeout(() => {
    closeCameraBox();
  }, 500);
}

/**
 * Initialize price trend chart
 */
function initializeChart() {
  const ctx = document.getElementById("priceChart");

  if (ctx) {
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June'],
        datasets: [
          {
            label: 'Rice Price (₹/quintal)',
            data: [1800, 1900, 2000, 2100, 2050, 2150],
            borderColor: '#2e8b57',
            backgroundColor: 'rgba(46, 139, 87, 0.1)',
            fill: true,
            tension: 0.4,
            pointRadius: 5,
            pointBackgroundColor: '#2e8b57',
            pointHoverRadius: 7
          },
          {
            label: 'Maize Price (₹/quintal)',
            data: [1600, 1650, 1700, 1800, 1750, 1900],
            borderColor: '#f39c12',
            backgroundColor: 'rgba(243, 156, 18, 0.1)',
            fill: true,
            tension: 0.4,
            pointRadius: 5,
            pointBackgroundColor: '#f39c12',
            pointHoverRadius: 7
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            position: 'top'
          }
        },
        scales: {
          y: {
            beginAtZero: false,
            title: {
              display: true,
              text: 'Price (₹)'
            }
          }
        }
      }
    });
  }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  initializeChart();
});