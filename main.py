from yadisk import YaUploader
from superhero import S_Hero



if __name__ == '__main__':
    print('Task 1')
    Heroes = ['Hulk', 'Captain America', 'Thanos']
    hero = S_Hero()
    print(hero.intelligence(Heroes))

    print("__________________________")

    print('Task 2')
    path_to_file = 'Files/hello.txt'
    token = 'TOKEN'
    uploader = YaUploader(token)
    result = uploader.get_upload_file(path_to_file)