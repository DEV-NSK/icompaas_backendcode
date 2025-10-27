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

# Install dependencies from requirements.txt
echo "Installing dependencies..."
pip install -r requirements.txt

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear

echo "=== Build Completed Successfully ==="