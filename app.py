from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)

# Configure CORS to be more permissive
CORS(app, 
     resources={r"/*": {
         "origins": "*",  # Allow all origins
         "methods": ["GET", "POST", "OPTIONS"],
         "allow_headers": ["Content-Type", "Authorization", "Accept"],
         "expose_headers": ["Content-Type", "Authorization"],
         "supports_credentials": True,
         "max_age": 3600
     }},
     supports_credentials=True)

@app.route('/generate-image', methods=['POST', 'OPTIONS'])
def generate_image():
    # Add CORS headers manually
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type, Authorization, Accept',
        'Access-Control-Max-Age': '3600'
    }
    
    if request.method == 'OPTIONS':
        # Handle preflight request
        return ('', 204, headers)
        
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
            return jsonify({'error': response.text}), response.status_code, headers
        
        # Retornar a resposta da API
        result = response.json()
        print("Resposta da API:", json.dumps(result, indent=2))
        return jsonify(result), response.status_code, headers
        
    except Exception as e:
        print("Erro no proxy:", str(e))
        return jsonify({'error': str(e)}), 500, headers

if __name__ == '__main__':
    print("Iniciando servidor proxy na porta 5000...")
    app.run(port=5000) 