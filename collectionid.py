from instagrapi import Client
import requests
from urllib.parse import urlparse

ACCOUNT_USERNAME = "*********"
ACCOUNT_PASSWORD = "*********"

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

# Récupérez les médias de la collection "graphic design"
collection_name = "graphic design"
collection_medias = cl.collection_medias_by_name(collection_name)

#print(collection_medias)

import requests
from urllib.parse import urlparse

# ... [Your existing code to log in and get collection_medias] ...

if collection_medias:
    download_directory = 'images/'

    for media in collection_medias:
        if media.product_type == 'carousel_container' or (hasattr(media, 'resources') and media.resources):
            print(f"Processing carousel: {media.id}")
            for resource in media.resources:
                if resource.media_type == 1:  # Check if the resource is an image
                    url = resource.thumbnail_url
                    filename = urlparse(url).path.split('/')[-1]
                    response = requests.get(url)
                    if response.status_code == 200:
                        with open(download_directory + filename, 'wb') as file:
                            file.write(response.content)
                        print(f'Téléchargement réussi : {filename}')
                    else:
                        print(f'Échec du téléchargement : {filename}')
        else:
            # Handle single image post
            url = media.image_versions2['candidates'][0]['url']
            filename = urlparse(url).path.split('/')[-1]
            response = requests.get(url)
            if response.status_code == 200:
                with open(download_directory + filename, 'wb') as file:
                    file.write(response.content)
                print(f'Téléchargement réussi : {filename}')
            else:
                print(f'Échec du téléchargement : {filename}')

else:
    print(f'La collection "{collection_name}" n\'existe pas ou est vide.')
