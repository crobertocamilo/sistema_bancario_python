## Desafio 2 do ***Potência Tech iFood* Ciência de Dados com Python**

Evento promovido pela [Digital Innovation One - DIO](https://www.dio.me/en), com patrocínio do [iFood](https://www.ifood.com.br/).

<div align="right">
  <img src="https://github.com/crobertocamilo/sistema_bancario_python/raw/main/assets/logo.webp" alt="logo bootcamp" width=20%/>
</div>

--- 
## Desafio : Criando um Sistema Bancário

### Objetivo

Desenvolver uma aplicação simples que implemente as principais operações bancárias (depósito, saque, extrato de operações). O sistema deve ser desenolvido em **Python**.

---
### Implementando a solução:

O [código](https://github.com/crobertocamilo/sistema_bancario_python/blob/main/src/codigo.py) desenvolvido está na pasta **src**. Para executá-lo baixe o arquivo e no terminal (ou *prompt* de comando) digite:

`python codigo.py` ou `python3 codigo.py`




Considerando que a imagem (AMI) Linux padrão na AWS utiliza o gerenciador de pacotes **yum**, ao invés do **apt**, são apresentados dois *scripts* para implementar a solução:

* [script_ubuntu.sh](https://github.com/crobertocamilo/linux_servidor_apache/blob/main/script_ubuntu.sh) para Ubuntu e outras distribuições baseadas no Debian;
* [scrip_aws.sh](https://github.com/crobertocamilo/linux_servidor_apache/blob/main/script_aws.sh) para distribuições que utilizam o yum como gerenciador de pacote, e especificamente, a distro utilizada na AMI Amazon Linux, da AWS.

Para executar o *script.sh* adequado:
* Copie o arquivo script.sh para máquina;
* Dê permissão de execução ao *script*:
  
  `sudo chmod +x script.sh`
* Execute o *script*:
  
  `./script.sh`

---
### Lançando uma instância EC2 com o servidor apache já instalado

Ao lançar uma máquina no EC2 é possível incluir um *script* de personalização da instância. 

Para criar uma **instância EC2 que já realize a instalação e configuração do httpd (Apache)** e disponibilize a página HTML ao iniciar, copie o [script_aws.sh](https://github.com/crobertocamilo/linux_servidor_apache/blob/main/script_aws.sh) para janela a **Advanced details**, na seção **USER DATA** da interface de configuração da instância (no console da AWS, é a última seção da página de configuração da instância a ser criada). 

Neste caso, seu servidor *web* já estará *online* após a inicialização da máquina. Basta acessar a página diretamente pelo IPv4 público da instância!

<div align="center">
  <img src="https://github.com/crobertocamilo/linux_servidor_apache/blob/main/assets/pagina_online_aws.png?raw=true" alt="Pagina html online numa instancia EC2" width=100%/>
</div>

<div align="center">
Página HTML personalizada sendo exibida a partir do servidor web criado numa instância do EC2.
</div>


