# ============================================================
# PROJETO - PREPARAÇÃO DE DADOS
# Tratamento, organização e análise
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import os
import unicodedata


# ============================================================
# 1. CARREGAMENTO DO ARQUIVO
# ============================================================

df = pd.read_excel("vendas.xlsx")

# Remove espaços extras dos nomes das colunas
df.columns = df.columns.str.strip()

print("=" * 60)
print("BASE DE DADOS ORIGINAL")
print("=" * 60)

print("Dimensões da base:", df.shape)

print("\nColunas:")
print(df.columns.tolist())

print("\nPrimeiros registros:")
print(df.head())

print("\nInformações da base:")
print(df.info())

print("\nValores ausentes:")
print(df.isnull().sum())


# ============================================================
# 2. DIAGNÓSTICO - DATA DA VENDA
# ============================================================

print("\n" + "=" * 60)
print("2. DIAGNÓSTICO - DATA DA VENDA")
print("=" * 60)

print(
    df["Data da Venda"]
    .value_counts(dropna=False)
)


# ============================================================
# 3. TRATAMENTO DA DATA DA VENDA
# ============================================================

df_limpo = df.copy()

df_limpo["Data da Venda"] = pd.to_datetime(
    df_limpo["Data da Venda"],
    format="mixed",
    errors="coerce",
    dayfirst=True
)

print("\nDatas inválidas ou vazias após conversão:")
print(
    df_limpo["Data da Venda"].isna().sum()
)


# ============================================================
# 4. DIAGNÓSTICO - PRODUTO
# ============================================================

print("\n" + "=" * 60)
print("4. DIAGNÓSTICO - PRODUTO")
print("=" * 60)

print("Quantidade de produtos diferentes:")
print(
    df_limpo["Produto"].nunique(dropna=True)
)

print("\nProdutos encontrados:")
print(
    df_limpo["Produto"]
    .value_counts(dropna=False)
)


# ============================================================
# 5. FUNÇÃO PARA PADRONIZAR PRODUTOS
# ============================================================

def remover_acentos(texto):

    texto = unicodedata.normalize(
        "NFD",
        texto
    )

    texto = "".join(
        caractere
        for caractere in texto
        if unicodedata.category(caractere) != "Mn"
    )

    return texto


def padronizar_produto(produto):

    # Mantém vazio como vazio
    if pd.isna(produto):
        return pd.NA

    texto = str(produto).strip().lower()

    # Remove acentos para facilitar a identificação
    texto_sem_acento = remover_acentos(texto)

    # --------------------------------------------------------
    # FEIJÃO
    # --------------------------------------------------------

    if "feijao" in texto_sem_acento:
        return "Feijão"


    # --------------------------------------------------------
    # ARROZ
    # --------------------------------------------------------

    if (
        "arroz" in texto_sem_acento
        or "arros" in texto_sem_acento
    ):
        return "Arroz"


    # --------------------------------------------------------
    # LEITE
    # --------------------------------------------------------

    if "leite" in texto_sem_acento:
        return "Leite"


    # --------------------------------------------------------
    # AÇÚCAR
    # --------------------------------------------------------

    if "acucar" in texto_sem_acento:
        return "Açúcar"


    # --------------------------------------------------------
    # MANTEIGA
    # --------------------------------------------------------

    if (
        "manteiga" in texto_sem_acento
        or "mantega" in texto_sem_acento
    ):
        return "Manteiga"


    # --------------------------------------------------------
    # CERVEJA
    # --------------------------------------------------------

    if "cerveja" in texto_sem_acento:
        return "Cerveja"


    # --------------------------------------------------------
    # VODKA
    # --------------------------------------------------------

    if (
        "vodka" in texto_sem_acento
        or "vodca" in texto_sem_acento
    ):
        return "Vodka"


    # --------------------------------------------------------
    # REFRIGERANTE
    # --------------------------------------------------------

    if (
        "refrigerante" in texto_sem_acento
        or "refri" in texto_sem_acento
        or "coca" in texto_sem_acento
    ):
        return "Refrigerante"


    # --------------------------------------------------------
    # DETERGENTE
    # --------------------------------------------------------

    if "detergent" in texto_sem_acento:
        return "Detergente"


    # --------------------------------------------------------
    # SABÃO
    # --------------------------------------------------------

    if (
        "sabao" in texto_sem_acento
        or "sabao" in texto_sem_acento
    ):
        return "Sabão"


    # --------------------------------------------------------
    # PAPEL HIGIÊNICO
    # --------------------------------------------------------

    if (
        "papel higienico" in texto_sem_acento
        or "papel higenico" in texto_sem_acento
    ):
        return "Papel higiênico"


    # --------------------------------------------------------
    # CASO NÃO ENTRE EM NENHUM GRUPO
    # --------------------------------------------------------

    return produto


# Aplica a função
df_limpo["Produto"] = (
    df_limpo["Produto"]
    .apply(padronizar_produto)
)


print("\nProdutos após padronização:")
print(
    df_limpo["Produto"]
    .value_counts(dropna=False)
)

print("\nQuantidade de produtos após padronização:")
print(
    df_limpo["Produto"].nunique(dropna=True)
)


# ============================================================
# 6. DIAGNÓSTICO - CATEGORIA
# ============================================================

print("\n" + "=" * 60)
print("6. DIAGNÓSTICO - CATEGORIA")
print("=" * 60)

print(
    df_limpo["Categoria"]
    .value_counts(dropna=False)
)


# ============================================================
# 7. PADRONIZAÇÃO DAS CATEGORIAS
# ============================================================

def padronizar_categoria(categoria):

    # Mantém vazio
    if pd.isna(categoria):
        return pd.NA

    texto = str(categoria).strip().lower()

    texto_sem_acento = remover_acentos(texto)


    # ALIMENTAÇÃO
    if (
        "aliment" in texto_sem_acento
        or "alim" in texto_sem_acento
    ):
        return "Alimentação"


    # BEBIDAS
    if "bebid" in texto_sem_acento:
        return "Bebidas"


    # LIMPEZA
    if "limp" in texto_sem_acento:
        return "Limpeza"


    # HIGIENE
    if "hig" in texto_sem_acento:
        return "Higiene"


    return categoria


df_limpo["Categoria"] = (
    df_limpo["Categoria"]
    .apply(padronizar_categoria)
)


print("\nCategorias após padronização:")
print(
    df_limpo["Categoria"]
    .value_counts(dropna=False)
)

print("\nQuantidade de categorias:")
print(
    df_limpo["Categoria"].nunique(dropna=True)
)


# ============================================================
# 8. DIAGNÓSTICO - QUANTIDADE
# ============================================================

print("\n" + "=" * 60)
print("8. DIAGNÓSTICO - QUANTIDADE")
print("=" * 60)

print("Tipo de dado:")
print(
    df_limpo["Quantidade"].dtype
)

print("\nValores ausentes:")
print(
    df_limpo["Quantidade"].isna().sum()
)

print("\nValores negativos:")
print(
    (
        pd.to_numeric(
            df_limpo["Quantidade"],
            errors="coerce"
        ) < 0
    ).sum()
)

print("\nValores encontrados:")
print(
    df_limpo["Quantidade"]
    .value_counts(dropna=False)
)


# ============================================================
# 9. TRATAMENTO DA QUANTIDADE
# ============================================================

df_limpo["Quantidade"] = pd.to_numeric(
    df_limpo["Quantidade"],
    errors="coerce"
)

# Quantidades negativas são consideradas inválidas
df_limpo.loc[
    df_limpo["Quantidade"] < 0,
    "Quantidade"
] = pd.NA

print("\nQuantidade após tratamento:")
print(
    df_limpo["Quantidade"]
    .value_counts(dropna=False)
)


# ============================================================
# 10. DIAGNÓSTICO - VALOR TOTAL
# ============================================================

print("\n" + "=" * 60)
print("10. DIAGNÓSTICO - VALOR TOTAL")
print("=" * 60)

print("Tipo de dado:")
print(
    df_limpo["Valor Total"].dtype
)

print("\nValores ausentes:")
print(
    df_limpo["Valor Total"].isna().sum()
)

print("\nValores negativos:")
print(
    (
        pd.to_numeric(
            df_limpo["Valor Total"],
            errors="coerce"
        ) < 0
    ).sum()
)

print("\nMenor valor:")
print(
    df_limpo["Valor Total"].min()
)

print("\nMaior valor:")
print(
    df_limpo["Valor Total"].max()
)


# ============================================================
# 11. TRATAMENTO DO VALOR TOTAL
# ============================================================

df_limpo["Valor Total"] = pd.to_numeric(
    df_limpo["Valor Total"],
    errors="coerce"
)

# Valores negativos são considerados inválidos
df_limpo.loc[
    df_limpo["Valor Total"] < 0,
    "Valor Total"
] = pd.NA

print("\nValor Total após tratamento:")
print(
    df_limpo["Valor Total"].describe()
)


# ============================================================
# 12. DIAGNÓSTICO - FORMA DE PAGAMENTO
# ============================================================

print("\n" + "=" * 60)
print("12. DIAGNÓSTICO - FORMA DE PAGAMENTO")
print("=" * 60)

print("Valores ausentes:")
print(
    df_limpo["Forma de Pagamento"].isna().sum()
)

print("\nFormas de pagamento encontradas:")
print(
    df_limpo["Forma de Pagamento"]
    .value_counts(dropna=False)
)


# ============================================================
# 13. PADRONIZAÇÃO DA FORMA DE PAGAMENTO
# ============================================================

def padronizar_pagamento(pagamento):

    # Mantém vazio
    if pd.isna(pagamento):
        return pd.NA

    texto = str(pagamento).strip().lower()

    texto_sem_acento = remover_acentos(texto)


    # --------------------------------------------------------
    # PIX
    # --------------------------------------------------------

    if "pix" in texto_sem_acento:
        return "Pix"


    # --------------------------------------------------------
    # DINHEIRO
    # --------------------------------------------------------

    if (
        "dinheiro" in texto_sem_acento
        or "dinhero" in texto_sem_acento
        or "dinh" in texto_sem_acento
    ):
        return "Dinheiro"


    # --------------------------------------------------------
    # CARTÃO DE CRÉDITO
    # --------------------------------------------------------

    if (
        "credito" in texto_sem_acento
        or "credit" in texto_sem_acento
    ):
        return "Cartão de crédito"


    # --------------------------------------------------------
    # CARTÃO DE DÉBITO
    # --------------------------------------------------------

    if (
        "debito" in texto_sem_acento
        or "debit" in texto_sem_acento
    ):
        return "Cartão de débito"


    # --------------------------------------------------------
    # BOLETO
    # --------------------------------------------------------

    if "boleto" in texto_sem_acento:
        return "Boleto"


    # Caso não seja reconhecido
    return pagamento


df_limpo["Forma de Pagamento"] = (
    df_limpo["Forma de Pagamento"]
    .apply(padronizar_pagamento)
)


print("\nFormas de pagamento após padronização:")
print(
    df_limpo["Forma de Pagamento"]
    .value_counts(dropna=False)
)


# ============================================================
# 14. VALIDAÇÃO FINAL
# ============================================================

print("\n" + "=" * 60)
print("14. VALIDAÇÃO FINAL")
print("=" * 60)

print("\nDimensões:")
print(
    df_limpo.shape
)

print("\nTipos de dados:")
print(
    df_limpo.dtypes
)

print("\nValores ausentes:")
print(
    df_limpo.isnull().sum()
)

print("\nRegistros duplicados:")
print(
    df_limpo.duplicated().sum()
)

print("\nQuantidades negativas:")
print(
    (
        df_limpo["Quantidade"] < 0
    ).sum()
)

print("\nValores negativos:")
print(
    (
        df_limpo["Valor Total"] < 0
    ).sum()
)

print("\nProdutos diferentes:")
print(
    df_limpo["Produto"].nunique(dropna=True)
)

print("\nCategorias:")
print(
    df_limpo["Categoria"].nunique(dropna=True)
)

print("\nFormas de pagamento:")
print(
    df_limpo["Forma de Pagamento"].nunique(dropna=True)
)


# ============================================================
# 15. EXPORTAÇÃO DO ARQUIVO LIMPO
# ============================================================

df_limpo.to_excel(
    "vendas_limpa.xlsx",
    index=False
)

print("\n" + "=" * 60)
print("BASE LIMPA GERADA")
print("=" * 60)

print(
    os.path.abspath("vendas_limpa.xlsx")
)


# ============================================================
# 16. ANÁLISE - FATURAMENTO POR PRODUTO
# ============================================================

vendas_produto = (
    df_limpo
    .groupby("Produto")["Valor Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== VENDAS POR PRODUTO =====")
print(vendas_produto)


# ============================================================
# 17. ANÁLISE - FATURAMENTO POR CATEGORIA
# ============================================================

vendas_categoria = (
    df_limpo
    .groupby("Categoria")["Valor Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== VENDAS POR CATEGORIA =====")
print(vendas_categoria)


# ============================================================
# 18. ANÁLISE - QUANTIDADE POR PRODUTO
# ============================================================

quantidade_produto = (
    df_limpo
    .groupby("Produto")["Quantidade"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== QUANTIDADE VENDIDA POR PRODUTO =====")
print(quantidade_produto)


# ============================================================
# 19. ANÁLISE - FATURAMENTO POR FORMA DE PAGAMENTO
# ============================================================

vendas_pagamento = (
    df_limpo
    .groupby("Forma de Pagamento")["Valor Total"]
    .sum()
    .sort_values(ascending=False)
)

print("\n===== VENDAS POR FORMA DE PAGAMENTO =====")
print(vendas_pagamento)


# ============================================================
# 20. RESUMO GERAL
# ============================================================

print("\n" + "=" * 60)
print("RESUMO GERAL")
print("=" * 60)

print(
    "Total de registros:",
    len(df_limpo)
)

print(
    "Faturamento registrado: R$",
    round(
        df_limpo["Valor Total"].sum(),
        2
    )
)

print(
    "Quantidade total registrada:",
    df_limpo["Quantidade"].sum()
)

print(
    "Produtos diferentes:",
    df_limpo["Produto"].nunique(dropna=True)
)

print(
    "Categorias:",
    df_limpo["Categoria"].nunique(dropna=True)
)

print(
    "Formas de pagamento:",
    df_limpo["Forma de Pagamento"].nunique(dropna=True)
)


# ============================================================
# 21. EXPORTAÇÃO DAS ANÁLISES PARA EXCEL
# ============================================================

vendas_produto.to_excel(
    "vendas_por_produto.xlsx"
)

vendas_categoria.to_excel(
    "vendas_por_categoria.xlsx"
)

quantidade_produto.to_excel(
    "quantidade_por_produto.xlsx"
)

vendas_pagamento.to_excel(
    "vendas_por_pagamento.xlsx"
)


# ============================================================
# 22. CONFIRMAÇÃO DOS ARQUIVOS
# ============================================================

print("\n" + "=" * 60)
print("PLANILHAS GERADAS")
print("=" * 60)

print("\nBase limpa:")
print(
    os.path.abspath("vendas_limpa.xlsx")
)

print("\nVendas por produto:")
print(
    os.path.abspath("vendas_por_produto.xlsx")
)

print("\nVendas por categoria:")
print(
    os.path.abspath("vendas_por_categoria.xlsx")
)

print("\nQuantidade por produto:")
print(
    os.path.abspath("quantidade_por_produto.xlsx")
)

print("\nVendas por forma de pagamento:")
print(
    os.path.abspath("vendas_por_pagamento.xlsx")
)


# ============================================================
# 23. GRÁFICO - FATURAMENTO POR CATEGORIA
# ============================================================

ax = vendas_categoria.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title(
    "Faturamento por Categoria",
    fontsize=14
)

plt.xlabel("Categoria")
plt.ylabel("Faturamento (R$)")

plt.xticks(
    rotation=0,
    ha="center"
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="R$ %.2f",
        padding=3
    )

plt.tight_layout()
plt.show()


# ============================================================
# 24. GRÁFICO - TOP 10 PRODUTOS POR FATURAMENTO
# ============================================================

top_10_produtos = (
    vendas_produto
    .head(10)
    .sort_values(ascending=True)
)

ax = top_10_produtos.plot(
    kind="barh",
    figsize=(11, 7)
)

plt.title(
    "Top 10 Produtos por Faturamento",
    fontsize=14
)

plt.xlabel("Faturamento (R$)")
plt.ylabel("Produto")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="R$ %.2f",
        padding=3
    )

plt.tight_layout()
plt.show()


# ============================================================
# 25. GRÁFICO - TOP 10 PRODUTOS POR QUANTIDADE
# ============================================================

top_10_quantidade = (
    quantidade_produto
    .head(10)
    .sort_values(ascending=True)
)

ax = top_10_quantidade.plot(
    kind="barh",
    figsize=(11, 7)
)

plt.title(
    "Top 10 Produtos por Quantidade Vendida",
    fontsize=14
)

plt.xlabel("Quantidade Vendida")
plt.ylabel("Produto")

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="%.0f",
        padding=3
    )

plt.tight_layout()
plt.show()


# ============================================================
# 26. GRÁFICO - FATURAMENTO POR FORMA DE PAGAMENTO
# ============================================================

ax = vendas_pagamento.plot(
    kind="bar",
    figsize=(10, 6)
)

plt.title(
    "Faturamento por Forma de Pagamento",
    fontsize=14
)

plt.xlabel("Forma de Pagamento")
plt.ylabel("Faturamento (R$)")

plt.xticks(
    rotation=0,
    ha="center"
)

for container in ax.containers:
    ax.bar_label(
        container,
        fmt="R$ %.2f",
        padding=3
    )

plt.tight_layout()
plt.show()


# ============================================================
# FIM
# ============================================================

print("\n" + "=" * 60)
print("PROCESSAMENTO CONCLUÍDO COM SUCESSO!")
print("=" * 60)
