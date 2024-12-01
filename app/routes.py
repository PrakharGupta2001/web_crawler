from flask import Flask, request, jsonify
from crawler import crawl_domain

app = Flask(__name__)

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    sitemap = crawl_domain(url)
    return jsonify(sitemap)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
