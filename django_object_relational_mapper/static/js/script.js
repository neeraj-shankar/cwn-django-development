// Get the elements
const openPopupButton = document.getElementById('cwn--open-model-form-btn');
const closePopupButton = document.getElementById('cwn--model-close');
const popup = document.getElementById('model--form-container');
const cancelButton = document.getElementById('cwn--model-cancel-btn');
const saveButton = document.getElementById('cwn--model-submit-btn');

// Open the pop-up when the button is clicked
openPopupButton.addEventListener('click', () => {
  popup.style.display = 'block';
});

// Close the pop-up when the close button is clicked
closePopupButton.addEventListener('click', () => {
  popup.style.display = 'none';
});

// Close the pop-up when the Cancel button is clicked
cancelButton.addEventListener('click', () => {
  popup.style.display = 'none';
});

// Handle form submission (you can add your logic here)
saveButton.addEventListener('click', () => {
  // Add your form submission logic here
  // For example, you can use AJAX to submit the form data to a server
  // Then close the pop-up
  popup.style.display = 'none';
});
