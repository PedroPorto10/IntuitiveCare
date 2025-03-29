import tabula
import pandas as pd
import zipfile
import shutil
import os

pdf_path = r"C:\Users\taped\IdeaProjects\IntuitiveCareScraping\Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_local = "dados_tabela.csv"
csv_acessivel = r"C:\temp\dados_tabela.csv"
zip_path = "Teste_pedro_henrique_porto_ferreira.zip"

os.makedirs(os.path.dirname(csv_acessivel), exist_ok=True)

dados_tabela = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)

dados_tabela_completa = pd.concat(dados_tabela, ignore_index=True)

dados_tabela_completa.columns = dados_tabela_completa.columns.str.replace(r"\n|\r", " ", regex=True)

dados_tabela_completa.columns = [col.strip() for col in dados_tabela_completa.columns]

dados_tabela_completa['OD'] = dados_tabela_completa['OD'].replace({'OD': 'Seg. Odontológica'})
dados_tabela_completa['AMB'] = dados_tabela_completa['AMB'].replace({'AMB': 'Seg. Ambulatorial'})

dados_tabela_completa.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorial'}, inplace=True)

colunas_tabela = ['PROCEDIMENTO', 'RN (alteração)', 'VIGÊNCIA', 'Seg. Odontológica', 'Seg. Ambulatorial', 'HCO', 'HSO', 'REF', 'PAC', 'DUT', 'SUBGRUPO', 'GRUPO', 'CAPÍTULO']

dados_tabela_completa = dados_tabela_completa[colunas_tabela]

dados_tabela_completa.dropna(how='all', inplace=True)

dados_tabela_completa.reset_index(drop=True, inplace=True)

dados_tabela_completa.to_csv(csv_local, index=False, header=True, encoding='utf-8-sig', sep=';')

shutil.copy(csv_local, csv_acessivel)

with zipfile.ZipFile(zip_path, "w") as zipf:
    zipf.write(csv_local)

print(f"Processamento concluído com sucesso!\nArquivo CSV salvo em: {csv_acessivel}")
