from flask import Flask, request, jsonify, make_response
import requests
import json

app = Flask(__name__)

def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://masknetdesign.github.io'
    response.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Max-Age'] = '3600'
    return response

@app.after_request
def after_request(response):
    return add_cors_headers(response)

@app.route('/generate-image', methods=['POST', 'OPTIONS'])
def generate_image():
    if request.method == 'OPTIONS':
        response = make_response()
        return add_cors_headers(response)
        
    try:
        # Log request details
        print("Request Origin:", request.headers.get('Origin'))
        print("Request Method:", request.method)
        print("Request Headers:", dict(request.headers))
        
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
            return add_cors_headers(jsonify({'error': response.text})), response.status_code
        
        # Retornar a resposta da API
        result = response.json()
        print("Resposta da API:", json.dumps(result, indent=2))
        return add_cors_headers(jsonify(result)), response.status_code
        
    except Exception as e:
        print("Erro no proxy:", str(e))
        return add_cors_headers(jsonify({'error': str(e)})), 500

if __name__ == '__main__':
    print("Iniciando servidor proxy na porta 5000...")
    app.run(port=5000) 