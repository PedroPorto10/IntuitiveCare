from flask import Flask, jsonify
import csv
from collections import Counter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def carregar_dados_csv():
    try:
        with open(r'C:\Relatorio_cadop.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            dados = list(reader)
            if not dados:
                return []
            return dados
    except Exception as e:
        print(f"Erro ao carregar o CSV: {e}")
        return []

dados_operadoras = carregar_dados_csv()

@app.route('/buscar-campos-mais-repetidos', methods=['GET'])
def buscar_campos_mais_repetidos():
    if not dados_operadoras:
        return jsonify({"erro": "Nenhum dado disponível"}), 500

    campos_mais_repetidos = {}
    for coluna in dados_operadoras[0].keys():
        valores_coluna = [operadora[coluna] for operadora in dados_operadoras if operadora[coluna] and operadora[coluna].strip() != '']

        if valores_coluna:
            contador = Counter(valores_coluna)
            campo_mais_comum, quantidade = contador.most_common(1)[0]
            campos_mais_repetidos[coluna] = {
                'campo': campo_mais_comum,
                'quantidade': quantidade
            }
        else:
            campos_mais_repetidos[coluna] = None

    return jsonify(campos_mais_repetidos)

if __name__ == '__main__':
    app.run(debug=True)
