import requests
import time
import os

# Define the URL and credentials
qb_url = 'http://localhost:8085/api/v2'
username = 'admin'
password = 'shifeng570'

# Start a session
session = requests.Session()

# Login
login_url = f'{qb_url}/auth/login'
login_response = session.post(login_url, data={'username': username, 'password': password})

if login_response.status_code == 200:
    print("Logged in successfully!")

    def get_torrent_hashes():
        """Retrieve the list of torrent hashes."""
        response = session.get(f'{qb_url}/torrents/info')
        if response.status_code == 200:
            torrents_info = response.json()
            return {torrent['hash'] for torrent in torrents_info}
        else:
            print("Failed to fetch torrents info.")
            return set()

    def get_files(torrent_hash):
        """Retrieve file information for a specific torrent."""
        response = session.get(f'{qb_url}/torrents/files?hash={torrent_hash}')
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch files info.")
            return []

    def set_file_selection(torrent_hash, largest_file_index):
        """Set which files in the torrent to download."""
        # Convert largest_file_index list to a comma-separated string
        # indexes = ','.join(map(str, largest_file_index))

        largest_file_name = largest_file['name']
        largest_file_name_base, _ = os.path.splitext(os.path.basename(largest_file_name))
        # Step: Check for any existing picture files with the same name in the torrent
        picture_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
        # picture_file_found = False


        file_index_to_download = largest_file_index #indexes
        files_info = get_files(torrent_hash)
        # Prepare the data for setting file priority
        for file in files_info:
            file_index = file['index']
            priority = 0  # Default to 0 (do not download)

            if file_index == file_index_to_download:
                priority = 6  # Set to 6 (high priority download)

            for ext in picture_extensions:
                if file['name'].lower().endswith(ext):
                    pic_file_name, _ = os.path.splitext(os.path.basename(file['name']))
                    # print(pic_file_name)
                    # print(largest_file_name_base)
                    if pic_file_name == largest_file_name_base:
                        priority = 1 # Set to 1 (download)
                        picture_file_found = True

            if 'is_seed' in file:
                priority = 0   # Do not download the seed file

            # Set the file priority using the filePrio endpoint
            file_prio_payload = {
                'hash': torrent_hash,
                'id': file_index,
                'priority': priority
            }
            response = session.post(f'{qb_url}/torrents/filePrio', data=file_prio_payload)
            # print(response.status_code)
            if response.status_code == 200:
                if priority:
                    print(f"File selection updated for torrent {torrent_hash}. - file index: ", file_index, f", priority: {priority}, name: {file['name']}")
            else:
                print(f"Failed to update file selection for torrent {torrent_hash}.")
                print(response.text)

    # Fetch initial list of torrents
    initial_torrent_hashes = get_torrent_hashes()


    # List all torrent files in the specified folder
    torrent_folder = 'scrapy/spider_tutorial/torrent_files'
    for filename in os.listdir(torrent_folder):
        if filename.endswith('.torrent'):
            torrent_file_path = os.path.join(torrent_folder, filename)

            # Add the torrent file
            add_torrent_url = f'{qb_url}/torrents/add'
            with open(torrent_file_path, 'rb') as torrent_file:
                response = session.post(add_torrent_url, files={'torrents': torrent_file})

            if response.status_code == 200:
                print('Torrent added successfully!!! \n')
                
                # Wait for a short time to ensure the torrent has been added
                time.sleep(5)

                # Fetch the updated list of torrents
                current_torrent_hashes = get_torrent_hashes()
                # print("current_torrent_hashes: ", current_torrent_hashes)
                # print("initial_torrent_hashes: ", initial_torrent_hashes)
                new_torrent_hashes = current_torrent_hashes - initial_torrent_hashes

                if new_torrent_hashes:
                    # Process the new torrents
                    for torrent_hash in new_torrent_hashes:
                        print(f"Processing new torrent: {torrent_hash}")
                        files_info = get_files(torrent_hash)
                        
                        if files_info:
                            largest_file = max(files_info, key=lambda file: file['size'])
                            largest_file_id = largest_file['index']
                            print("largest_file_id:", largest_file_id)
                            print(f"Largest file: {largest_file['name']} (Size: {largest_file['size']/1024/1024/1024} G)")
                            
                            # Set only the largest file to download
                            set_file_selection(torrent_hash, largest_file_id)
                        else:
                            print("No file information available.")
                else:
                    print("No new torrents detected.")
            else:
                print('Failed to add torrent:', response.text)

    # Log out
    logout_response = session.post(f'{qb_url}/auth/logout')
    if logout_response.status_code == 200:
        print("Logged out successfully!")
    else:
        print("Failed to log out.")
        print(logout_response.text)
else:
    print("Failed to log in.")
    print(login_response.text)