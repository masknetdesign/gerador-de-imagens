const cors = require('cors')({origin: true});
const fetch = require('node-fetch');

exports.proxy = async (req, res) => {
    return cors(req, res, async () => {
        try {
            const { apiKey, apiUrl, ...payload } = req.body;
            
            console.log('Payload recebido:', JSON.stringify(payload, null, 2));
            
            const response = await fetch(`${apiUrl}?key=${apiKey}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            });
            
            const data = await response.json();
            
            if (!response.ok) {
                console.error('Erro da API:', data);
                return res.status(response.status).json(data);
            }
            
            return res.status(200).json(data);
        } catch (error) {
            console.error('Erro no proxy:', error);
            return res.status(500).json({ error: error.message });
        }
    });
}; 