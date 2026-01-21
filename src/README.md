# ETL – Santander Dev Week 

Este projeto implementa um fluxo **ETL (Extração, Transformação e Carregamento)** utilizando Python, inspirado no desafio da Santander Dev Week.  
O objetivo é demonstrar a construção de um pipeline simples e funcional, ideal para portfólios de Ciência de Dados.

---

## 🚀 Objetivo

Criar um processo ETL que:

1. **Extraia** dados de usuários (lista em Python)  
2. **Transforme** esses dados gerando mensagens personalizadas  
3. **Carregue** o resultado em um arquivo CSV  

---

## 🧩 Tecnologias Utilizadas

- Python 3  
- Biblioteca padrão `csv`  

---

## 📁 Estrutura do Projeto
src/ └── etl.py mensagens.csv README.md requirements.txt

---

## 🔄 Fluxo ETL

### **1. Extração**
Os dados são carregados a partir de uma lista Python contendo nome, conta e cartão dos usuários.

### **2. Transformação**
Cada usuário recebe uma mensagem personalizada simulando uma oferta bancária.

### **3. Carregamento**
As mensagens são gravadas no arquivo `mensagens.csv`.

---

## ▶️ Como Executar

1. Clone o repositório  
2. Entre na pasta do projeto  
3. Execute:
python src/etl.py

4. O arquivo `mensagens.csv` será criado automaticamente.

---

## 📄 Exemplo de Saída (mensagens.csv)
nome,mensagem Ana Souza,"Olá, Ana Souza! Identificamos que sua conta 12345-6 e cartão 5555 4444 3333 2222 estão elegíveis para uma oferta exclusiva. Entre em contato!" Pedro Lima,"Olá, Pedro Lima! Identificamos que sua conta 98765-4 e cartão 1111 2222 3333 4444 estão elegíveis para uma oferta exclusiva. Entre em contato!"

---

## 🏁 Conclusão

Este projeto demonstra de forma simples e clara como funciona um pipeline ETL.  
É ideal para estudos, portfólio e como base para projetos mais avançados.
