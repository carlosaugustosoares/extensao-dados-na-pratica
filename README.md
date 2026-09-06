# extensão-dados-na-pratica
Preparação e análise de dados de vendas utilizando Python e Pandas.


# Dados na Prática: Organização e Preparação de Informações para Pequenos Negócios

## Sobre o projeto

Este projeto foi desenvolvido com o objetivo de aplicar, na prática, conceitos de preparação e organização de dados em uma situação relacionada ao dia a dia de um comércio, juntamente com o objetivo de consolidar os conhecimentos adquiridos na disciplina de Preparação de Dados.

Por meio de uma rotina desenvolvida em Python, os dados foram analisados, tratados, padronizados e organizados, tornando a base mais adequada para análises posteriores.

O projeto também demonstra como uma base de vendas fornecida por um comerciante, inicialmente desorganizada pode ser transformada em informações mais estruturadas e úteis para compreender as vendas de um negócio.

---

## Objetivos

O projeto teve como principais objetivos:

- Identificar inconsistências presentes na base de dados;
- Verificar dados ausentes e inválidos;
- Padronizar nomes de produtos e categorias;
- Padronizar as formas de pagamento;
- Corrigir formatos de datas;
- Tratar valores e quantidades;
- Validar a base após o processo de preparação;
- Exportar os dados tratados para novos arquivos;
- Realizar análises simples sobre as vendas;
- Criar gráficos para facilitar a visualização dos resultados.

---

## Tecnologias utilizadas

- **Python**
- **Pandas**
- **Matplotlib**

---

## Estrutura dos dados

A base utilizada contém informações relacionadas às vendas de um pequeno comércio.

As principais colunas são:

| Coluna | Descrição |
|---|---|
| Data da Venda | Data em que a venda foi realizada |
| Produto | Produto comercializado |
| Categoria | Categoria à qual o produto pertence |
| Quantidade | Quantidade registrada na venda |
| Valor Total | Valor total registrado na venda |
| Forma de Pagamento | Forma utilizada para realizar o pagamento |

---

## Etapas do projeto

### 1. Carregamento dos dados

A base de vendas foi carregada utilizando a biblioteca Pandas.

Após o carregamento, foram verificadas informações como:

- quantidade de registros;
- quantidade de colunas;
- tipos de dados;
- valores ausentes;
- estrutura das informações.

### 2. Diagnóstico da base

Foi realizada uma análise inicial para identificar possíveis problemas nos dados.

Entre os problemas encontrados estavam:

- valores ausentes;
- datas em formatos diferentes;
- datas inválidas;
- nomes de produtos escritos de formas diferentes;
- categorias com variações de escrita;
- formas de pagamento com diferentes padrões;
- valores monetários em formatos diferentes;
- quantidades inválidas.

### 3. Tratamento das datas

As datas foram convertidas para um formato adequado para análise.

Também foram identificadas datas inválidas ou ausentes durante o processo de conversão.

### 4. Padronização dos produtos

Foram identificadas diferentes formas de escrita para produtos que representavam o mesmo item.

Por exemplo:

- Arroz
- Feijão
- Leite
- Açúcar
- Manteiga
- Cerveja
- Vodka
- Refrigerante
- Detergente
- Sabão
- Papel higiênico

As diferentes formas de escrita foram agrupadas e padronizadas para facilitar as análises.

### 5. Padronização das categorias

As categorias também apresentavam variações de escrita.

Após o tratamento, os registros foram organizados em categorias padronizadas, permitindo uma análise mais consistente das vendas.

### 6. Tratamento das quantidades

Foram identificados registros com valores ausentes, valores inválidos e diferentes formas de representação.

Os dados foram convertidos para formato numérico e os valores considerados inválidos foram tratados adequadamente.

### 7. Tratamento dos valores

Os valores das vendas apresentavam diferentes formatos.

Foi realizado o tratamento necessário para converter essas informações para um formato numérico, permitindo realizar cálculos e análises de faturamento.

### 8. Padronização das formas de pagamento

As formas de pagamento também apresentavam diferentes maneiras de preenchimento.

Os registros foram analisados e padronizados para facilitar a identificação das principais formas utilizadas nas vendas.

Entre elas estão:

- Pix
- Dinheiro
- Cartão de crédito
- Cartão de débito
- Boleto

### 9. Validação dos dados

Após as etapas de tratamento, a base foi novamente analisada para verificar se os dados estavam estruturados de maneira adequada.

Foram verificadas informações como:

- quantidade de registros;
- tipos de dados;
- valores ausentes;
- registros duplicados;
- valores inválidos;
- produtos padronizados;
- categorias padronizadas;
- formas de pagamento padronizadas.

### 10. Análise dos dados

Depois da preparação da base, foram realizadas análises simples utilizando os dados tratados.

Foram analisados:

- faturamento por produto;
- faturamento por categoria;
- quantidade vendida por produto;
- faturamento por forma de pagamento.

### 11. Visualização dos resultados

Foram utilizados gráficos para facilitar a interpretação das informações.

Entre as visualizações desenvolvidas estão:

- faturamento por categoria;
- produtos com maior faturamento;
- quantidade de produtos vendidos;
- faturamento por forma de pagamento.

---

## Resultados

Após o processo de preparação, foi obtida uma base de dados mais organizada e estruturada para realização de análises.

O tratamento permitiu reduzir as variações de preenchimento e transformar informações que estavam em formatos diferentes em dados mais padronizados.

Com a base preparada, tornou-se possível realizar análises de faturamento, produtos, categorias e formas de pagamento de maneira mais organizada.

Os gráficos também facilitaram a visualização dos resultados e demonstraram como a preparação dos dados é uma etapa importante antes da realização de análises.

---

## Arquivos gerados

Durante a execução do projeto, são gerados arquivos contendo os dados tratados e os resultados das análises.

Entre eles:

- `vendas_limpa.xlsx`
- `vendas_por_produto.xlsx`
- `vendas_por_categoria.xlsx`
- `quantidade_por_produto.xlsx`
- `vendas_por_pagamento.xlsx`

---

## Como executar o projeto

### 1. Instale o Python

É necessário ter o Python instalado no computador.

### 2. Instale as bibliotecas

No terminal, execute:

bash
pip install pandas matplotlib
