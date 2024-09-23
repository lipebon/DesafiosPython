```
#🌟 Bem-vindo ao Sistema Bancário Simples 🌟

Este é um projeto de um **Sistema Bancário** em Python que permite que você faça depósitos, saques, visualize extratos, crie contas, usuários, e muito mais. Tudo isso através de um simples menu interativo no terminal! 🏦

##📜 Funcionalidades Principais:

1. **Depósitos** - Deposite dinheiro na conta 💵
2. **Saques** - Realize saques com limite diário por segurança 💸
3. **Visualizar Extrato** - Acompanhe as movimentações da conta 📄
4. **Solicitar Aumento de Limite de Saques** - Caso precise de mais saques no dia 📈
5. **Criar Novos Usuários** - Adicione novos usuários ao sistema 👤
6. **Criar Novas Contas** - Vincule novas contas aos usuários existentes 🏦
7. **Listar Contas** - Veja todas as contas registradas no sistema 📋
8. **Sair** - Finalize a sessão 🔒

```

----

##📚 Como Usar

Aqui estão alguns exemplos de como você pode interagir com o sistema:

- **Criar um Novo Usuário**: Escolha a opção `[nu]` e siga as instruções para registrar um novo usuário. O sistema pedirá o CPF, nome, data de nascimento e endereço.
- **Criar uma Nova Conta**: Depois de ter pelo menos um usuário cadastrado, use a opção `[nc]` para criar uma nova conta para o usuário.
- **Depositar**: Com a opção `[d]`, insira o valor que deseja depositar na conta.
- **Sacar**: Use a opção `[s]` para realizar um saque, desde que não exceda o limite diário e tenha saldo suficiente.
- **Visualizar Extrato**: Acompanhe as movimentações de sua conta com a opção `[e]`.

### 🛠 Funções Importantes:
- **`depositar`**: Função responsável por adicionar valor ao saldo.
- **`sacar`**: Função que realiza o saque, verificando saldo e limites.
- **`exibir_extrato`**: Mostra as movimentações da conta.
- **`criar_usuario`**: Registra novos usuários.
- **`criar_conta`**: Cria uma nova conta vinculada a um usuário existente.
- **`listar_contas`**: Exibe todas as contas criadas no sistema.

---

## 🔄 Como Fazer um Fork do Projeto

Se você quiser contribuir com este projeto ou apenas personalizá-lo para o seu uso, é muito fácil! Basta seguir os passos abaixo:

1. **Faça o Fork** 🍴:
   - Vá até o topo direito desta página no GitHub e clique no botão `Fork`.

2. **Clone o Repositório Forkado**:
   - No seu terminal, rode o comando:
     ```bash
     git clone https://github.com/seu-usuario/nome_do_repositorio.git
     ```

3. **Crie uma Branch para suas Alterações**:
   - Crie uma nova branch para as suas modificações:
     ```bash
     git checkout -b minha-branch
     ```

4. **Realize suas Alterações e Commit**:
   - Após fazer as mudanças desejadas, adicione e faça o commit:
     ```bash
     git add .
     git commit -m "Minhas alterações no sistema bancário"
     ```

5. **Suba as Alterações**:
   - Envie suas alterações para o GitHub:
     ```bash
     git push origin minha-branch
     ```

6. **Abra um Pull Request**:
   - Por fim, vá até o repositório original e abra um Pull Request para que suas alterações possam ser revisadas e possivelmente incorporadas ao projeto principal!

---

## 💡 Exemplo de Execução

Veja abaixo um exemplo de como o sistema responde quando você realiza um depósito e depois visualiza o extrato:

```plaintext
Valor do depósito: 100.00

Depósito de R$ 100.00 realizado com sucesso!

================ EXTRATO ================
Depósito:      R$ 100.00

Saldo:         R$ 100.00
==========================================
```

---

## 🏅 Contribuindo

Contribuições são sempre bem-vindas! Se você encontrar algum bug, tiver sugestões de melhoria ou quiser adicionar novas funcionalidades, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*. Vamos juntos tornar este projeto cada vez melhor! 😄


---

**Muito obrigado por conferir este projeto!** ✨
