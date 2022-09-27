from yadisk import YaUploader



if __name__ == '__main__':
    path_to_file = 'Files/hello.txt'
    token = 'y0_AgAAAAAVp31iAADLWwAAAADP1yZmG2kiTifPQ4yhXqhFO2axi3yJe0k'
    uploader = YaUploader(token)
    result = uploader.get_upload_file(path_to_file)

