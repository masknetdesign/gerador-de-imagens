from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route('/generate-image', methods=['POST'])
def generate_image():
    try:
        # Obter os dados da requisição
        data = request.json
        print("Payload recebido:", json.dumps(data, indent=2))
        
        # Configuração da API
        api_key = 'AIzaSyBIUAoStzUUuJL2ZJ1D1xB1JvtCkDXlukY'
        api_url = 'https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:predict'
        
        # Fazer a requisição para a API do Google
        print("Enviando requisição para:", api_url)
        response = requests.post(
            f'{api_url}?key={api_key}',
            json=data,
            headers={'Content-Type': 'application/json'}
        )
        
        # Se houver erro, mostrar detalhes
        if response.status_code != 200:
            print("Erro da API:", response.text)
            return jsonify({'error': response.text}), response.status_code
        
        # Retornar a resposta da API
        result = response.json()
        print("Resposta da API:", json.dumps(result, indent=2))
        return jsonify(result), response.status_code
        
    except Exception as e:
        print("Erro no proxy:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Iniciando servidor proxy na porta 5000...")
    app.run(port=5000) 