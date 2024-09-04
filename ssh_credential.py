import paramiko
import os
import getpass

# Configuration
unix_server = {
    'hostname': 'your_unix_server_address',
    'port': 22,
    'username': 'your_username',
}

nas_path = '/path/to/nas/directory/'
local_download_path = '/local/path/to/downloaded/file'
remote_file_path = '/remote/path/to/remote/file'

def download_file_from_unix_server(password):
    try:
        # Create an SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(
            hostname=unix_server['hostname'],
            port=unix_server['port'],
            username=unix_server['username'],
            password=password
        )
        
        # Create an SFTP client
        sftp_client = ssh_client.open_sftp()
        
        # Download the file
        sftp_client.get(remote_file_path, local_download_path)
        print(f"File downloaded from {remote_file_path} to {local_download_path}")

        # Close SFTP session
        sftp_client.close()
        ssh_client.close()

    except Exception as e:
        print(f"An error occurred: {e}")

def upload_file_to_nas():
    try:
        # Make sure the NAS directory exists
        if not os.path.exists(nas_path):
            os.makedirs(nas_path)
        
        # Move the file to the NAS path
        os.rename(local_download_path, os.path.join(nas_path, os.path.basename(local_download_path)))
        print(f"File uploaded to {os.path.join(nas_path, os.path.basename(local_download_path))}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Prompt for the password
    password = getpass.getpass(prompt="Enter the SSH password: ")
    download_file_from_unix_server(password)
    upload_file_to_nas()
