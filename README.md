# Documentação:

(Explicar o que é a lib)
(Referências para o lattice miner, ipred, data-peeler, e artigos relacionados)
(Explicar divisão de módulos)

## Input/Output

(Explicar formatos)
(Mostrar métodos para diádico)
(Mostrar métodos para triádico)


## Conversão de contextos

(Explicar como funciona)
(Mostrar método)


## Conceitos

(Explicar o que são)
(Explicar como usar o data-peeler)

**Os arquivos que serão entrada para o data-peeler, devem estar com a quebra de linha configurada em *LF (Line Feed)*, para o funcionamento correto do data-peeler.


(Mostrar métodos para diádico)
(Mostrar métodos para triádico)


## Conceitos

(Explicar o que são)
(Explicar como usar o data-peeler)

(Mostrar métodos para diádico)
(Mostrar métodos para triádico)

***

# Exemplos de código

(falar dos arquivos de exemplo)
(explicar o que é possível fazer com a lib)

***

# Trabalhos futuros:

* Possibilitar a geração de contextos sintéticos (detalhar melhor):
https://www.researchgate.net/publication/271477874_SCGaz_-_A_Synthetic_Formal_Context_Generator_with_Density_Control_for_Test_and_Evaluation_of_FCA_Algorithms

* Ambiente de uso com interface gráfica (aplicação desktop ou web);
* Adicionar métodos para medir tempo de execução de etapas;
* Gerar relatório com:
  * Resultados de tempo;
  * Quantidade de itens obtidos por etapa;
  * Arquivos contendo os itens (conceitos, geradores, regras...)

***

# Como usar com o pip:

(Subir lib no pip)
(Mostrar tutorial de instalação)

***

# Como usar com o Docker:

1. Instale o docker na sua máquina;
2. `docker build -t fca-tools-container .`

* Para executar o ambiente: `docker run -i -t fca-tools-container:latest /bin/bash`
* Para sair: `<ctrl + z> ou <ctrl + c>`

* Para parar o serviço: `docker stop <container-id>`
* Para reiniciar o serviço: `docker restart <container-id>`
* Para entrar no shell: `docker exec -it <container-id> /bin/bash`

(Internamente, utilize o `python3`)


# TODO

* Criar exemplo pro triádico;
* Safe type em todas as classes e funções;
* Documentação;
* Completar texto do TCC
