# Solução





Minha primeira ideia foi fazer um dump das tabelas para um banco de dados. Mas estava apresentando muitos erros. Então decidi mapear os dados para deixá-los melhor estruturados.

![Processamento local](./images/processamento_local.png)

Na tentativa de fazer um algoritmo para mapear os dados utilizando o processamento local, em python. O primeiro desafio foi a dimensão dos arquivos pois não havia memória suficiente para fazer de um jeito instantâneo. Uma solução simples foi varrer o arquivo linha por linha persistindo no banco. Deixei rodando o algoritmo em quando buscava outra solução.



![](./images/Peek 10-08-2021 16-55.gif)



Enquanto rodava estava estudando AWS e aprendi sobre os serviços de processamento em nuvem do EC2.  Então pensei em fazer tudo na nuvem. Mas tinha o receio do custo disso, pois é cobrado por memória utilizada, processamento e armazenamento deixando o algoritmo inviável. E ainda havia o problema do tamanho do arquivo.

Estudando mais aprendi sobre os serviços do S3, AWS Glue e Athena.  O que tornou o algoritmo desnecessário. Então só restou um problema para resolver, o do tamanho do arquivo.

Cheguei a conclusão que era mais fácil e rápido enviar o arquivo compactado. E levantou o desafio de como descompactar um arquivo dentro de um Bucket. Não é possível, pois um bucket não tem sistema de pastas.

Minha primeira ideia foi utilizar o EC2 para descompactar e espalhar os arquivos em um novo bucket.



![](./images/utilizando_EC2.png)


Ao pesquisar mais soluções da AWS encontrei a Lambda. Que executa um algoritmo em resposta a algum evento, como alguma alteração em um bucket. 

Assim tive a ideia de utilizar para descompactar o arquivo, ao fazer o upload. 

![](./images/enviando_compactado.png)

E ao fim preocupado com o tamanho do arquivo a ser descompactado pela lambda, se traria algum custo e para não atrasar a entrega, subi os arquivos descompactados para um bucket. E tudo funcionou como o esperado.

![](./images/sem_lambda.png)

