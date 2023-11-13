def get_max_downloads_and_visits(file_path):
    max_user_downloads = ('', 0)
    max_url_visits = ('', 0)

    with open(file_path, 'r') as file:
        for line in file:
            data_type, data = line.strip().split('\t')

            if 'url' in data_type:
                url, visits = data.split(',')
                url.replace('url:', '')
                visits = int(visits)
                if visits > max_url_visits[1]:
                    max_url_visits = (url, visits)

            elif 'user' in data_type:
                user_id, downloads = data.split(',')
                user_id.replace('user:', '')
                downloads = int(downloads)
                if downloads > max_user_downloads[1]:
                    max_user_downloads = (user_id, downloads)

    return max_user_downloads, max_url_visits


# Example usage
file_path = 'your_file.txt'  # Replace with the actual path to your file
max_user_downloads, max_url_visits = get_max_downloads_and_visits(file_path)

print(f"User with the most downloads: {max_user_downloads}")
print(f"URL with the most visits: {max_url_visits}")
