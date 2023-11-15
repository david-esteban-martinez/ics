import os

def get_max_downloads_and_visits(folder_path):
    max_user_downloads = ('', 0)
    max_url_visits = ('', 0)

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        if filename == '_SUCCESS':
            continue
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                for line in file:
                    data_type, data = line.strip().split('\t')

                    if 'url' in data_type:
                        url, visits = data.split(',')
                        url = url.replace('url:', '')  # Fix: use url.replace instead of url.replace
                        visits = int(visits)
                        if visits > max_url_visits[1]:
                            max_url_visits = (url, visits)

                    elif 'user' in data_type:
                        user_id, downloads = data.split(',')
                        user_id = user_id.replace('user:', '')  # Fix: use user_id.replace instead of user_id.replace
                        downloads = int(downloads)
                        if downloads > max_user_downloads[1]:
                            max_user_downloads = (user_id, downloads)

    return max_user_downloads, max_url_visits

# Example usage for a folder
folder_path = '/path/to/your/folder'  # Replace with the actual path to your folder
max_user_downloads, max_url_visits = get_max_downloads_and_visits(folder_path)

print("User with most .ps downloads is " + max_user_downloads[0] + " with " + str(max_user_downloads[1]) + " downloads")
print("URL with most visits is " + max_url_visits[0] + " with " + str(max_url_visits[1]) + " visits")
