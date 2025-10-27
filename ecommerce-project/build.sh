# #!/usr/bin/env bash
# # build.sh

# echo "=== Starting Build Process ==="

# # Install dependencies from requirements.txt
# echo "Installing dependencies..."
# pip install -r requirements.txt

# # Apply database migrations
# echo "Applying database migrations..."
# python manage.py migrate

# # Collect static files
# echo "Collecting static files..."
# python manage.py collectstatic --noinput --clear

# echo "=== Build Completed Successfully ==="
#!/usr/bin/env bash
# build.sh

echo "=== Starting Build Process ==="

# Exit on error and show commands
set -o errexit
set -o xtrace

# Upgrade pip first
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Check if database is available
echo "Checking database connection..."
python -c "
import django
from django.conf import settings
django.setup()
from django.db import connection
try:
    connection.ensure_connection()
    print('✅ Database connection successful')
except Exception as e:
    print('❌ Database connection failed:', e)
    exit(1)
"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "=== Build Completed Successfully ==="