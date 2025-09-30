const form = document.getElementById('email-form');
const resultado = document.getElementById('resultado');
const categoria = document.getElementById('categoria');
const resposta = document.getElementById('resposta');
const fecharBtn = document.getElementById('fechar-resultado');
const button = document.querySelector('.btn-submit');
const fileDrop = document.getElementById('file-drop');
const fileInput = document.getElementById('pdf-file');

// Elemento para mostrar o nome do arquivo PDF
const fileNameDisplay = document.createElement('p');
fileNameDisplay.id = 'file-name-display';
fileNameDisplay.style.color = '#ccc';
fileNameDisplay.style.fontSize = '14px';
fileNameDisplay.style.marginTop = '8px';
fileDrop.appendChild(fileNameDisplay);

// Efeito de destaque ao arrastar PDF
fileDrop.addEventListener('dragover', (e) => {
  e.preventDefault();
  fileDrop.style.borderColor = '#1e90ff';
  fileDrop.style.background = '#333';
});
fileDrop.addEventListener('dragleave', () => {
  fileDrop.style.borderColor = '#555';
  fileDrop.style.background = '#2a2a2a';
});

// Atualiza o nome do arquivo quando selecionado
fileInput.addEventListener('change', () => {
  const file = fileInput.files[0];
  if (file) {
    fileNameDisplay.textContent = `Arquivo selecionado: ${file.name}`;
  } else {
    fileNameDisplay.textContent = '';
  }
});

form.addEventListener('submit', async (e) => {
  e.preventDefault();

  const text = document.getElementById('email-text').value.trim();
  const file = fileInput.files[0];

  if (!text && !file) {
    alert("Por favor, cole um texto ou envie um PDF.");
    return;
  }

  const formData = new FormData();
  if (text) formData.append('text', text);
  if (file) formData.append('file', file);

  resultado.classList.remove('hidden');
  button.classList.add('loading');
  button.disabled = true;

  categoria.textContent = 'Processando...';
  resposta.textContent = 'Aguarde a resposta da IA.';

  try {
    const response = await fetch('http://localhost:8000/process', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.detail || 'Erro desconhecido.');

    categoria.textContent = data.categoria;
    resposta.textContent = data.resposta;

  } catch (error) {
    categoria.textContent = '❌ Erro de Sistema';
    resposta.textContent = error.message;
  }

  button.classList.remove('loading');
  button.disabled = false;
});

fecharBtn.addEventListener('click', () => {
  resultado.classList.add('hidden');
  document.getElementById('email-text').value = '';
  fileInput.value = '';
  fileNameDisplay.textContent = '';
});
