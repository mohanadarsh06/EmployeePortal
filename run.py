from app import create_app
from app.utils.db_init import seed_database

app = create_app()

# In Flask 2.x, before_first_request is deprecated
# We'll use a different approach to initialize the database
with app.app_context():
    seed_database()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)