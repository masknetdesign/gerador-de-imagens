from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

# Configure CORS
CORS(app, 
     resources={
         r"/*": {
             "origins": ["https://masknetdesign.github.io"],
             "methods": ["GET", "POST", "OPTIONS"],
             "allow_headers": ["Content-Type"],
             "expose_headers": ["Content-Type"],
             "supports_credentials": False,
             "max_age": 3600
         }
     })

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'online',
        'message': 'Proxy server is running'
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'healthy',
        'message': 'Server is healthy'
    })

@app.route('/generate-image', methods=['POST', 'OPTIONS'])
def generate_image():
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
            return jsonify({'error': response.text}), response.status_code
        
        # Retornar a resposta da API
        result = response.json()
        print("Resposta da API:", json.dumps(result, indent=2))
        return jsonify(result)
        
    except Exception as e:
        print("Erro no proxy:", str(e))
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not Found',
        'message': 'The requested URL was not found on the server'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'An unexpected error occurred'
    }), 500

if __name__ == '__main__':
    print("Iniciando servidor proxy na porta 5000...")
    app.run(port=5000) 