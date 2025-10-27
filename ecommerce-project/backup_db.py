import os
import subprocess
from datetime import datetime

def backup_database():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_ecommerce_{timestamp}.sql"
    
    # Set your database credentials
    db_name = "ecommerce_db"
    db_user = "ecommerce_user"
    db_host = "localhost"
    
    # Create backup using pg_dump
    try:
        cmd = [
            'pg_dump',
            '-h', db_host,
            '-U', db_user,
            '-d', db_name,
            '-f', backup_file,
            '-w'  # Wait for password prompt
        ]
        
        # Set PGPASSWORD environment variable
        env = os.environ.copy()
        env['PGPASSWORD'] = 'bathulasaikiran2k2'
        
        subprocess.run(cmd, env=env, check=True)
        print(f"Backup created successfully: {backup_file}")
    except subprocess.CalledProcessError as e:
        print(f"Backup failed: {e}")

if __name__ == "__main__":
    backup_database()