const uploadBtn = document.getElementById('uploadBtn');
const pdfInput = document.getElementById('pdfInput');
const summaryContainer = document.getElementById('summaryContainer');
const summaryText = document.getElementById('summaryText');
const loading = document.getElementById('loading');

uploadBtn.addEventListener('click', async () => {
  const file = pdfInput.files[0];
  if (!file) {
    alert('Please select a PDF file first!');
    return;
  }

  loading.classList.remove('hidden');
  summaryContainer.classList.add('hidden');

  const formData = new FormData();
  formData.append('file', file);

  try {
    const response = await fetch('http://127.0.0.1:8000/upload_file', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();

    if (data.ok) {
      summaryText.textContent = data.summary;
      summaryContainer.classList.remove('hidden');
    } else {
      alert(data.message || 'No summary available');
    }
  } catch (err) {
    alert('Error: ' + err.message);
  } finally {
    loading.classList.add('hidden');
  }
});
