# Gerador de Fichas de Treino - Template Comercial

Este é o template base para o gerador de fichas de treino, projetado para ser facilmente personalizado para cada cliente.

## 🚀 Como Usar

1.  **Execute o script `personalizar.py`**:
    ```bash
    python3 personalizar.py
    ```
    O script irá solicitar os dados do consultor (nome, empresa, CREF, telefone, nome curto para o app) e os dados do aluno (nome do aluno, data de troca da ficha).
    Ele criará uma nova pasta com o projeto personalizado para o cliente.

2.  **Substitua os Ícones e o Logo (Opcional)**:
    Na pasta recém-criada (`ficha-treino-[nome-do-consultor]`), você encontrará os arquivos `icon-*.png` e `logo.jpeg`. Substitua-os pelos ícones e logo específicos do cliente para uma personalização completa.

3.  **Crie um Repositório GitHub**:
    Crie um novo repositório no GitHub e faça o upload de todo o conteúdo da pasta personalizada (`ficha-treino-[nome-do-consultor]`).

4.  **Conecte ao Vercel**:
    Conecte o novo repositório GitHub ao Vercel. O Vercel fará o deploy automaticamente, e você terá uma URL exclusiva para o cliente.

5.  **Entregue a URL ao Cliente**:
    Compartilhe a URL gerada pelo Vercel com o cliente. Ele poderá acessar o gerador de fichas personalizado e instalá-lo como um PWA em seu dispositivo móvel.

## 🎨 Personalização

O script `personalizar.py` substitui automaticamente os seguintes placeholders:

-   `{{CONSULTOR_NOME}}`: Nome completo do consultor
-   `{{CONSULTOR_NOME_UPPER}}`: Nome completo do consultor em maiúsculas
-   `{{CONSULTOR_EMPRESA}}`: Nome da empresa/consultoria
-   `{{CONSULTOR_CREF}}`: Número do CREF
-   `{{CONSULTOR_TELEFONE}}`: Telefone de contato
-   `{{CONSULTOR_SHORT_NAME}}`: Nome curto para o PWA (aparece na tela inicial)

Além disso, os campos para **Nome do Aluno** e **Data de Troca da Ficha** são adicionados dinamicamente no HTML e incluídos no PDF gerado.

## 📱 PWA (Progressive Web App)

Este template é configurado como um PWA, permitindo que os usuários o instalem na tela inicial de seus dispositivos móveis e o utilizem como um aplicativo nativo, com ícone personalizado e funcionamento offline.

## 📄 Geração de PDF

A geração de PDF é feita utilizando PDFMake, garantindo compatibilidade total com dispositivos móveis e texto selecionável. O nome do arquivo PDF gerado incluirá o nome do aluno para facilitar a organização.

## 📞 Suporte

Para dúvidas ou suporte, entre em contato com o desenvolvedor.

