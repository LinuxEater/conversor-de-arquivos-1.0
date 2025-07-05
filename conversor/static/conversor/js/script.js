document.addEventListener('DOMContentLoaded', () => {
    console.alert("Conversor pronto!");
});

const selectConversao = document.getElementById('tipoConversao');
const fileInput = document.getElementById('arquivo');
const labelArquivo = document.getElementById('label-arquivo');

function updateAcceptAndLabel() {
  const selected = selectConversao.value;
  switch(selected) {
    case 'txt-pdf':
      fileInput.accept = '.txt';
      labelArquivo.textContent = 'Escolha um arquivo .txt';
      break;
    case 'pdf-txt':
      fileInput.accept = '.pdf';
      labelArquivo.textContent = 'Escolha um arquivo .pdf';
      break;
    case 'docx-pdf':
      fileInput.accept = '.docx';
      labelArquivo.textContent = 'Escolha um arquivo .docx';
      break;
    case 'pdf-docx':
      fileInput.accept = '.pdf';
      labelArquivo.textContent = 'Escolha um arquivo .pdf';
      break;
    default:
      fileInput.accept = '';
      labelArquivo.textContent = 'Escolha um arquivo compatível';
  }
  fileInput.value = ''; // limpa seleção anterior
}

selectConversao.addEventListener('change', updateAcceptAndLabel);
updateAcceptAndLabel();
