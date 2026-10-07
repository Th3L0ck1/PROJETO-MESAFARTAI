# Escopo do Projeto - MESAFARTAI

## Problema de negócio

Muitos alimentos que ainda podem ser consumidos são jogados fora por mercados, restaurantes e feirantes, por estarem perto da validade ou por sobra de estoque. Ao mesmo tempo, ONGs e abrigos têm dificuldade para conseguir doações.

O problema principal é a falta de uma forma rápida e fácil de ligar quem quer doar com quem precisa receber.

## Público-alvo

- **Doadores:** mercados, restaurantes, padarias, feirantes e produtores que têm alimento sobrando.
- **ONGs:** ONGs, abrigos e cozinhas comunitárias que precisam receber alimentos.

## Intenções tratadas pelo chatbot

| Intenção | Exemplo |
|---|---|
| cadastrar_doacao | "Tenho 20kg de arroz para doar" |
| solicitar_alimentos | "Nossa ONG está precisando de feijão" |
| consultar_status | "Minha doação já foi retirada?" |
| fora_de_escopo | "Qual o placar do jogo?" |

Se o modelo tiver confiança menor que 0.60, o bot responde com uma mensagem pedindo para o usuário reformular a frase.

## Dados coletados no chat

- Tipo de alimento
- Quantidade (kg, caixas, unidades)
- Validade / prazo (hoje, amanhã, 18h)
- Nome, tipo de usuário (doador ou ONG), CEP, telefone e localização

## Prompt usado para gerar o logo

Ferramenta: gerador de imagens por IA (Google Gemini)

```
Logotipo minimalista e moderno para "MESAFARTAI", uma plataforma de inteligência artificial assistiva que conecta doadores de alimentos a ONGs no combate à fome. O símbolo central une duas mãos acolhedoras em formato de concha segurando um prato com uma folha verde e um grão de trigo, onde o contorno do prato se transforma em circuitos digitais e nós de rede neural que se conectam como pontos de um mapa. Paleta de cores: verde-esperança (#2E7D32), laranja quente (#F57C00) e azul tecnologia (#1565C0) sobre fundo branco. Estilo flat design vetorial, linhas limpas, ícone centralizado com o texto "MESAFARTAI" em fonte sans-serif arredondada e em negrito logo abaixo. Transmite acolhimento, solidariedade e tecnologia.
```
