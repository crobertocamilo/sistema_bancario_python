## Desafio 2 do ***Potência Tech iFood* Ciência de Dados com Python**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio do [iFood](https://www.ifood.com.br/).

<div align="right">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/raw/main/assets/logo.webp" alt="logo bootcamp" width=30%/>
</div>

--- 
## Desafio - Criando um Sistema Bancário

### Objetivo

Desenvolver uma aplicação simples que implemente as principais operações bancárias (depósito, saque, extrato de operações). O sistema deve ser desenvolvido em **Python**.

**Observações:**

- O sistema deve exibir um menu com as operações. O usuário deve poder fazer diversas operações, respeitando as instruções abaixo;
- Considerar que o usário já fez o *login* no sistema (não é necessário se preocupar com as informações do cliente: nome, conta, agência já foram validados);
- Deve ser possível depositar valores positivos (sem limite de valor ou número de operações);
- O sistema deve permitir até 3 saques por dia, sendo o valor máximo para cada saque R$ 500. Se o usário não tiver saldo suficiente na conta, não permitir o saque;
- A opção extrato deve listar todas as operações de depósito e saque realizadas durante a seção, além do saldo da conta. O extrato pode ser solicitado a qualquer momento e deve considerar as operações realizadas até então - caso nenhuma operação tenha sido realizada ainda, exibir a mensagem *Não foram realizadas movimentações*.

---
### Implementando a solução:

O [código](https://github.com/crobertocamilo/sistema_bancario_python/blob/main/src/codigo.py) desenvolvido está na pasta **src**. Para executá-lo baixe o arquivo ou este repositório. Tendo o Python instalado em sua máquina, digite no terminal (ou *prompt* de comando):

`python codigo.py` ou `python3 codigo.py`

<br>

Será exibido o menu de operações e o usuário deve escolher uma das opções:
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/blob/main/assets/menu.png?raw=true" alt="Menu de operações" width=35%/>
</div>

<br>

Foi aplicada validação à todas as entradas de dados (*inputs*) utilizando **try... except**.

<br>

As operações de depósito e saque implementam as regras definidas nas *instruções* e solicitam a confirmação do usário para concluir a transação:

<br>
<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/blob/main/assets/validacao.png?raw=true" alt="Exemplo confirmação saque" width=52%/>
</div>

<br>

A opção de extrato pode ser selecionada a qualquer momento (e várias vezes durante a seção) e exibe toda a movimentação financeira da conta:

<br>

<div align="center">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/blob/main/assets/extrato.png?raw=true" alt="Exemplo extrato" width=30%/>
</div>

