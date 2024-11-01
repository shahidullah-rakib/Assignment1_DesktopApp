// Clear all logs function
function clearLogs() {
  // Clear the displayed log outputs
  document.getElementById('keyboard-output').textContent = '';
  document.getElementById('app-output').textContent = '';
  document.getElementById('url-output').textContent = '';
  document.getElementById('mouse-output').textContent = '';

  // Clear the charts
  const charts = ['keyboardChart', 'appChart', 'urlChart', 'mouseChart'];
  charts.forEach((chartId) => {
    const ctx = document.getElementById(chartId).getContext('2d');
    const chartInstance = Chart.getChart(chartId); // Get the chart instance
    if (chartInstance) {
      chartInstance.data.labels = [];
      chartInstance.data.datasets[0].data = [];
      chartInstance.update(); // Update the chart
    }
  });

  alert('Logs cleared!');
}

// Export logs function
function exportLogs() {
  // Create a JSON object with all the log data
  const logs = {
    keyboard: document.getElementById('keyboard-output').textContent,
    application: document.getElementById('app-output').textContent,
    url: document.getElementById('url-output').textContent,
    mouse: document.getElementById('mouse-output').textContent,
  };

  // Convert the logs object to a JSON string
  const logsJSON = JSON.stringify(logs, null, 2);

  // Create a blob from the JSON string
  const blob = new Blob([logsJSON], { type: 'application/json' });
  const url = URL.createObjectURL(blob);

  // Create a link element to trigger the download
  const a = document.createElement('a');
  a.href = url;
  a.download = 'tracking_logs.json';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url); // Clean up the URL

  alert('Logs exported as tracking_logs.json');
}

// Add event listeners for the buttons
document.getElementById('clear-logs').addEventListener('click', clearLogs);
document.getElementById('export-logs').addEventListener('click', exportLogs);

// Existing code for fetching and displaying data remains unchanged
async function fetchData(fileName) {
  const response = await fetch(fileName);
  if (!response.ok) {
    throw new Error(`HTTP error! status: ${response.status}`);
  }
  return response.json();
}

// Call existing display functions here...
async function displayKeyboardData() {
  try {
    const keyboardData = await fetchData('../backend/keyboard_data.json');
    document.getElementById('keyboard-output').textContent = JSON.stringify(
      keyboardData,
      null,
      2
    );

    // Create keyboard chart
    const labels = keyboardData.map((entry) => entry.timestamp);
    const data = keyboardData.map((entry) => entry.key); // Example: count occurrences of each key

    const ctx = document.getElementById('keyboardChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: [...new Set(data)], // Unique keys
        datasets: [
          {
            label: 'Key Press Frequency',
            data: data.reduce((acc, key) => {
              acc[key] = (acc[key] || 0) + 1;
              return acc;
            }, {}),
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  } catch (error) {
    console.error('Error fetching keyboard data:', error);
  }
}

async function displayAppData() {
  try {
    const appData = await fetchData('../backend/app_data.json');
    document.getElementById('app-output').textContent = JSON.stringify(
      appData,
      null,
      2
    );

    // Create application chart
    const labels = appData.map((entry) => entry.app_name);
    const data = appData.map((entry) => entry.duration); // Duration for each application

    const ctx = document.getElementById('appChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Application Usage Duration (seconds)',
            data: data,
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  } catch (error) {
    console.error('Error fetching application data:', error);
  }
}

async function displayUrlData() {
  try {
    const urlData = await fetchData('../backend/url_data.json');
    document.getElementById('url-output').textContent = JSON.stringify(
      urlData,
      null,
      2
    );

    // Create URL chart
    const labels = [...new Set(urlData.map((entry) => entry.url))]; // Unique URLs
    const dataCounts = labels.map(
      (label) => urlData.filter((entry) => entry.url === label).length
    );

    const ctx = document.getElementById('urlChart').getContext('2d');
    new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'URL Visit Count',
            data: dataCounts,
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  } catch (error) {
    console.error('Error fetching URL data:', error);
  }
}

async function displayMouseData() {
  try {
    const mouseData = await fetchData('../backend/mouse_data.json');
    document.getElementById('mouse-output').textContent = JSON.stringify(
      mouseData,
      null,
      2
    );

    // Create mouse activity chart
    const labels = mouseData.map((entry) => entry.timestamp);
    const data = mouseData.map((entry) => entry.activity); // Example: count mouse clicks

    const ctx = document.getElementById('mouseChart').getContext('2d');
    new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Mouse Activity',
            data: data,
            backgroundColor: 'rgba(255, 206, 86, 0.2)',
            borderColor: 'rgba(255, 206, 86, 1)',
            borderWidth: 1,
            fill: true,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  } catch (error) {
    console.error('Error fetching mouse data:', error);
  }
}

async function initialize() {
  await Promise.all([
    displayKeyboardData(),
    displayAppData(),
    displayUrlData(),
    displayMouseData(),
  ]);
}

initialize();
