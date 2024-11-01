// const { ipcRenderer } = require('electron');

// // Function to capture mouse event messages
// function handleMouseEvent(event) {
//   const output = document.getElementById('output');
//   output.innerHTML += `<p>${event}</p>`;
// }

// // Track mouse movements and clicks
// document.addEventListener('mousemove', (event) => {
//   handleMouseEvent(`Mouse moved to (${event.clientX}, ${event.clientY})`);
// });

// // Track mouse clicks
// document.addEventListener('mousedown', (event) => {
//   const button = event.button;
//   let buttonName;

//   // Determine which button was clicked
//   if (button === 0) {
//     buttonName = 'Left';
//   } else if (button === 1) {
//     buttonName = 'Middle'; // Optional, for middle click
//   } else if (button === 2) {
//     buttonName = 'Right';
//   }

//   handleMouseEvent(
//     `Mouse ${buttonName} clicked at (${event.clientX}, ${event.clientY})`
//   );
// });

// document.addEventListener('mouseup', (event) => {
//   const button = event.button;
//   let buttonName;

//   // Determine which button was released
//   if (button === 0) {
//     buttonName = 'Left';
//   } else if (button === 1) {
//     buttonName = 'Middle'; // Optional, for middle click
//   } else if (button === 2) {
//     buttonName = 'Right';
//   }

//   handleMouseEvent(
//     `Mouse ${buttonName} released at (${event.clientX}, ${event.clientY})`
//   );
// });
