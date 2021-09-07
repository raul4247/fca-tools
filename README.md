# TODO
* Documentação;
* iPred;
* Regras de implicação;
* Geradores;
* Adicionar densidade como propriedade dos contextos (ou função);


# Bônus:
* Geração de contextos sintéticos:
https://www.researchgate.net/publication/271477874_SCGaz_-_A_Synthetic_Formal_Context_Generator_with_Density_Control_for_Test_and_Evaluation_of_FCA_Algorithms


# Como usar com o Docker:

1. Instale o docker na sua máquina;
2. `docker build -t fca-tools-container .`

* Para executar o ambiente: `docker run -i -t fca-tools-container:latest /bin/bash`
* Para sair: `exit`

(Internamente, utilize o `python3`)