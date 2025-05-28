# Gerador de Imagens

Um aplicativo web que permite gerar imagens a partir de descrições textuais usando a API do Google (Imagen 3.0).

## Funcionalidades

- Geração de imagens a partir de descrições textuais
- Suporte a diferentes proporções de imagem (1:1, 16:9, 9:16, 4:3)
- Download das imagens geradas
- Interface responsiva e moderna
- Feedback visual durante o carregamento

## Tecnologias Utilizadas

- HTML5
- Tailwind CSS
- JavaScript
- API do Google (Imagen 3.0)

## Como Usar

1. Clone o repositório
2. Copie o arquivo `config.example.js` para `config.js`
3. Obtenha uma chave API do Google Cloud Console
4. Configure sua chave API no arquivo `config.js`
5. Inicie o servidor local:
   ```bash
   python server.py
   ```
6. Acesse http://localhost:8000 no seu navegador
7. Insira uma descrição da imagem desejada
8. Selecione a proporção da imagem
9. Clique em "Gerar Imagem"
10. Após a geração, você pode baixar a imagem clicando no ícone de download

## Configuração

1. Acesse o [Google Cloud Console](https://console.cloud.google.com)
2. Crie um novo projeto ou selecione um existente
3. Ative a API do Imagen 3.0 para seu projeto
4. Crie uma chave API nas configurações de credenciais
5. Copie o arquivo `config.example.js` para `config.js`
6. Substitua `'SUA_CHAVE_API_AQUI'` pela sua chave API real

## Desenvolvimento

Para iniciar o servidor de desenvolvimento:

```bash
python server.py
```

O servidor estará disponível em http://localhost:8000

## Licença

Este projeto está sob a licença MIT. 