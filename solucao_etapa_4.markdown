### **Etapa 4:**

### **Com base no que definir nas etapas anteriores, responda às seguintes perguntas:**



- ##### Qual arquitetura você definiu?Qual o schema da(s) tabela(s) consolidada(s)?

  Utilizei um algoritimo para mapear e as tabelas auxiliares e trazer as colunas nescessárias. Subi as bases para buckets no AWS S3. Utilizei o crawler do AWS Glue para raspar a base e criar um banco de dados no AWS Athena, onde fiz as querys para apresentar os resultados.

  ![](./images/sem_lambda.png)

- ##### Com base na(s) tabela(s) consolidada(s), quais queries você utilizou para responder às perguntas acima?

  Para a estimativa de distribuição de cor/raça por estado, utilizei a tabela principal extraida da base. Fazendo joins com as tabelas auxiliares onde estão as nomenclatura das chaves.	

  ```
  
  SELECT mun.no_uf AS UF, cor.cor_raca_name AS cor_raca, COUNT(*) AS quantidade_de_pessoas
  FROM microdadoscensoescolar AS cen
  JOIN tabela_auxiliar_municipios_ufs AS mun
  	ON cen.co_uf = mun.co_uf
  JOIN tabela_auxiliar_cor_raca AS cor
  	ON cor.tp_cor_raca = cen.tp_cor_raca
  GROUP BY cor.cor_raca_name, mun.no_uf
  ORDER BY mun.no_uf, quantidade_de_pessoas, cor.cor_raca_name DESC;
  
  ```

  

  E para as 10 cidades com os alunos do nono ano também foi extraído da base utilizando de joins para nomear os campos.

  ```
  
  SELECT mun.NO_MUNICIPIO AS municipio, COUNT(cen.CO_MUNICIPIO) AS quantidade
  FROM microdadoscensoescolar AS cen
  JOIN tabela_auxiliar_municipios_ufs AS mun ON cen.CO_MUNICIPIO = mun.CO_MUNICIPIO
  WHERE cen.TP_ETAPA_ENSINO = 41
  GROUP BY mun.NO_MUNICIPIO
  ORDER BY quantidade DESC LIMIT 10;
  
  ```

  

- ##### Quais dados você incluiria na(s) tabela(s) consolidada(s) e que seriam interessantes para as pessoas analistas usarem? e qual a razão delas?

  Como eu conheço a preocupação da Trybe com todo o tipo de diversidade, eu incluiria a diversidade de gênero. Também havia campos de nacionalidade, pois, salvo engano, para alguns processos seletivos da Trybe é necessário ter nacionalidade brasileira. E também há dados de cursos profissionalizantes, o que pode melhorar a assertividade no interesse de possíveis candidatos.

- ##### Caso os dados fossem 10.000 vezes maior, você manteria a mesma arquitetura? porque?

  A princípio sim. Pois apesar de a arquitetura AWS ser paga, é extremamente escalável e dispensa a necessidade de uma infra estrutura. Porém se houver a necessidade de um volume maior de queries talvez seja mais interessante criar um serviço mais complexo no EC2.

