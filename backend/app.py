from flask import Flask
from utils.db import init_db
from routes.auth_routes import auth_bp
from routes.inventory_routes import inventory_bp
from routes.order_routes import order_bp
from routes.logs_routes import logs_bp
from utils.scheduler import schedule_tasks

app = Flask(__name__)

# Initialize the database
init_db(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(inventory_bp, url_prefix="/inventory")
app.register_blueprint(order_bp, url_prefix="/orders")
app.register_blueprint(logs_bp, url_prefix="/logs")

# Start the scheduler
schedule_tasks(app)

@app.route("/")
def home():
    return "Hardware Store Backend Running!"

if __name__ == "__main__":
    app.run(debug=True)
