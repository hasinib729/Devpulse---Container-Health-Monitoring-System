from flask import Flask, jsonify, render_template
import monitor

app = Flask(__name__)

@app.route('/')
def index():
    """Render the dashboard UI."""
    return render_template('index.html')

@app.route('/containers', methods=['GET'])
def containers_api():
    """API endpoint to get real-time container stats."""
    stats = monitor.get_container_stats()
    
    # Return 200 OK for successful fetch (even if empty), 500 for server-side Docker errors
    if stats.get("status") == "error":
        return jsonify(stats), 500
        
    return jsonify(stats), 200

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
