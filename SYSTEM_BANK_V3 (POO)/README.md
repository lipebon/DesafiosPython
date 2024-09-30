# 💻 Sistema Bancário em Python

## 🚀 Bem-vindo ao Sistema Bancário
Este projeto é um sistema bancário completo, desenvolvido em Python, que permite a criação e gerenciamento de contas, realização de depósitos, saques, exibição de extratos e muito mais. Ele utiliza uma abordagem orientada a objetos (OOP) com classes como `Cliente`, `Conta`, `PessoaFisica`, entre outras.

---

## ⚙️ Funcionalidades

- **Cadastro de Clientes**: Crie novos clientes com nome, CPF, data de nascimento e endereço.
- **Criação de Contas Bancárias**: Abra contas para clientes já cadastrados, com uma senha numérica de acesso.
- **Depósitos e Saques**: Realize operações de depósito e saque, com validação de saldo e limites diários.
- **Extrato Bancário**: Exiba o histórico de transações e o saldo atual da conta.
- **Solicitação de Aumento de Limite de Saques**: Solicite aumentos no limite de saques diários.



---

## 📖 Exemplos de Uso

### 1. Cadastro de Cliente

```bash
Informe o CPF (somente número): 12345678900
Digite seu nome completo: João do Exemplo
Digite a data de nascimento (dd-mm-aaaa): 01-01-1990
Digite seu endereço: Rua Exemplo, 123 - Centro - São Paulo/SP
--- Cliente cadastrado com sucesso ---
```

### 2. Abertura de Conta
```bash
Copiar código
Informe o CPF do cliente: 12345678900
Agora você irá cadastrar uma senha numérica para acessar sua conta.
Digite sua senha: ****
Confirme sua senha: ****
--- Sua conta foi criada com sucesso! ---
```

### 3. Realizar Depósito
```bash
Copiar código
Informe o CPF do cliente: 12345678900
Digite sua senha: ****
Informe o valor do depósito: 100.00
--- Depósito no valor de R$100.00 realizado ---
```


### 4. Exibir Extrato
```bash
Copiar código
Informe o CPF do cliente: 12345678900
Digite sua senha: ****
================ EXTRATO ================
Depósito:
    R$ 100.00
Saque:
    R$ 50.00
Saldo:
    R$ 50.00
=========================================
```

## 🖼️ Demonstração

```
Veja abaixo para ver o sistema funcionando:
```

<img src=https://raw.githubusercontent.com/lipebon/DesafiosPython/refs/heads/main/SYSTEM_BANK_V3%20(POO)/gif/demo_funcionamento_py.gif>



## 🧠 Tecnologias Utilizadas

```
Python: Linguagem principal do projeto.
Orientação a Objetos (OOP): Estrutura de classes como Cliente, Conta, Transacao, etc.
Biblioteca time: Para adicionar delays e melhorar a experiência do usuário.
```

<img src=https://github.com/lipebon/DesafiosPython/blob/main/SYSTEM_BANK_V3%20(POO)/gif/demo_cod_py.gif>


---

## 🤝 Como Contribuir
Contribuições são sempre bem-vindas! Aqui está um guia para quem quiser colaborar:

### 1. Realize um Fork do Repositório
```bash
Se você deseja fazer alterações ou melhorias, primeiro faça um fork do repositório.
Você pode fazer isso diretamente pelo GitHub clicando no botão "Fork" no canto superior direito da página do repositório.
```
### 2. Clone o Repositório Forkado

```bash
git clone https://github.com/seu-usuario/seu-fork.git
```

### 3. Crie uma Branch para sua Funcionalidade ou Correção

```bash
git checkout -b minha-feature
```

### 4. Faça suas Alterações

Após realizar as modificações desejadas, faça o commit das suas alterações.

```bash
git add .
git commit -m "Adiciona minha nova feature"
```

### 5. Envie suas Alterações para o Repositório Forkado
```bash
git push origin minha-feature
```

### 6. Abra um Pull Request

Vá até a página do repositório original e abra um Pull Request, explicando detalhadamente as mudanças que você fez.

##### Abrir uma Issue

 - Caso você tenha encontrado algum problema ou tenha uma sugestão, abra uma issue no GitHub.
 - Descreva o problema ou a melhoria sugerida, e ficaremos felizes em discutir a melhor solução!

-----------

## 📧 Contato
Felipe Teixeira Bon - felipetbon@gmail.com
