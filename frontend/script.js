const form = document.getElementById('email-form');
const resultado = document.getElementById('resultado');
const categoria = document.getElementById('categoria');
const resposta = document.getElementById('resposta');
const emailOriginal = document.getElementById('email-original');
const button = document.querySelector('button[type="submit"]');
const exportarBtn = document.getElementById('exportar-pdf');
const fecharBtn = document.getElementById('fechar-resultado'); // Novo elemento

form.addEventListener('submit', async (e) => {
    e.preventDefault(); 

    const text = document.getElementById('email-text').value.trim();
    if (!text) return;

    const formData = new FormData();
    formData.append('text', text);

    resultado.classList.remove('hidden');
    
    button.classList.add('loading');
    button.disabled = true;
    exportarBtn.classList.add('hidden');
    resultado.classList.remove('error'); 

    emailOriginal.textContent = text; 
    categoria.textContent = 'Processando...';
    resposta.textContent = 'Aguarde a resposta da IA.';

    try {
        const response = await fetch('http://localhost:8000/process', {
            method: 'POST',
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            const errorDetail = data.detail || 'Erro desconhecido do servidor.';
            throw new Error(errorDetail);
        }

        categoria.textContent = data.categoria;
        resposta.textContent = data.resposta;
        exportarBtn.classList.remove('hidden');

    } catch (error) {
        console.error('Falha na classificação:', error);

        let errorMessage = 'Não foi possível conectar ao servidor. Verifique se o FastAPI está rodando.';
        if (error.message && error.message !== 'Failed to fetch') {
            errorMessage = `Erro ao processar: ${error.message}`;
        }

        categoria.textContent = '❌ Erro de Sistema';
        resposta.textContent = errorMessage;
        exportarBtn.classList.add('hidden');
        resultado.classList.add('error'); 
    }

    button.classList.remove('loading');
    button.disabled = false;
});

// Lógica para Fechar a seção de resultados
fecharBtn.addEventListener('click', () => {
    resultado.classList.add('hidden');
    // Opcional: Limpar o campo de texto ao fechar
    document.getElementById('email-text').value = ''; 
});

exportarBtn.addEventListener('click', () => {
    
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();
    const margin = 20;
    let y = margin;
    const maxWidth = 170;
    const lineHeight = 10;
    
    doc.setFontSize(14);
    doc.text("Classificação de Email", margin, y);
    y += lineHeight * 2; 

    doc.setFontSize(12);
    doc.text("Email original:", margin, y);
    y += lineHeight / 2;
    // Opcional: Garante que a quebra de linha preserve a formatação original
    const emailTextContent = emailOriginal.textContent.replace(/\n/g, ' '); 
    const emailLines = doc.splitTextToSize(emailTextContent, maxWidth); 
    doc.text(emailLines, margin, y);
    y += emailLines.length * lineHeight + lineHeight; 

    doc.text(`Categoria: ${categoria.textContent}`, margin, y);
    y += lineHeight * 2; 

    doc.text("Resposta sugerida:", margin, y);
    y += lineHeight / 2;
    const respostaLines = doc.splitTextToSize(resposta.textContent, maxWidth);
    doc.text(respostaLines, margin, y);

    doc.save("classificacao-email.pdf");
});