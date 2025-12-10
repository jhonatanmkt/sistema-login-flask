# 🛒 Projeto Americanas - Sistema de Autenticação Full Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-000000?style=for-the-badge&logo=mysql&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)

> **Projeto Acadêmico | Curso Técnico em Desenvolvimento de Sistemas (SENAI Roberto Simonsen)**

Este projeto consiste no desenvolvimento de uma aplicação web completa (**Full Stack**) que simula o sistema de login e cadastro da loja Americanas. O objetivo foi aplicar na prática conceitos de engenharia de software, desde a prototipagem da interface até a implementação do banco de dados e servidor.

---

## 🛠️ Tecnologias e Arquitetura

O projeto foi dividido entre **Front-end** (interface) e **Back-end** (lógica e dados):

### 🎨 Front-end & Design
* **Figma**: Prototipagem de alta fidelidade da interface antes da codificação.
    * 🔗 **[Acessar o Projeto no Figma](https://www.figma.com/design/amH9o7NR7fjfAzv8lfQV7S/Jhonatan---Marley?node-id=0-1&p=f)**
* **HTML5 Semântico**: Estruturação das páginas (`index`, `login`, `cadastro`, `painel`).
* **CSS3**: Estilização personalizada seguindo a identidade visual da marca (cores, tipografia e layout responsivo).

### ⚙️ Back-end & Banco de Dados
* **Python 3**: Linguagem principal utilizada no servidor.
* **Flask**: Micro-framework web utilizado para criar as rotas e gerenciar as requisições HTTP.
* **MySQL**: Sistema gerenciador de banco de dados relacional (SGBD) para armazenar os usuários.
* **XAMPP**: Ambiente de desenvolvimento local (servidor Apache + MySQL).
* **Segurança**: Implementação de Hash de senhas (criptografia) para proteção dos dados dos usuários.

---

## 🚀 Funcionalidades do Sistema

1.  **Cadastro de Usuários**: Formulário que recebe nome, e-mail e senha, criptografa a senha e salva no banco de dados MySQL.
2.  **Autenticação (Login)**: Verifica as credenciais e permite o acesso apenas se os dados baterem com o banco.
3.  **Controle de Sessão**: Gerenciamento de sessões do usuário (mantém o usuário logado enquanto navega).
4.  **Proteção de Rotas**: O "Painel do Usuário" é uma rota protegida; se tentar acessar sem logar, o sistema bloqueia e redireciona.
5.  **Feedback Visual**: Mensagens de erro (ex: "Senha incorreta") ou sucesso (ex: "Cadastro realizado") aparecem na tela (Flash Messages).

---

## 📂 Estrutura do Projeto

```text
projeto-americanas/
│
├── app.py              # Cérebro do sistema (Rotas e Lógica Flask)
├── conexao.py          # Script de teste de conexão com o banco
├── banco de dados.sql  # Script SQL para criação da tabela
│
├── static/             # Arquivos estáticos
│   └── style.css       # Folha de estilos
│
└── templates/          # Páginas HTML
    ├── index.html
    ├── login.html
    ├── cadastro.html
    └── paineldeusuario.html
