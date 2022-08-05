import logging
# import os
from xml.dom import ValidationErr
import dropbox


class WritingToDB:
    def __init__(self, name: str, path: str, key: str):
        '''This class writes files in JSON format toward Dropbox
        name: The name that the JSON file should have
        path: the directory in which it needs to be saved on Dropbox
        key: The access token that can be generated via the app'''
        self.dbx = dropbox.Dropbox(key)
        try:
            file_json = open(f'storage/{name}.json', 'rb')
            if self.check_path_exists(path):
                self.dbx.files_upload(
                    file_json.read(),
                    f'{path}/{name}.json',
                    mode=dropbox.files.WriteMode("overwrite")
                    )
                logging.info('Saving to the Cloud success')
                print('Saving to the Cloud success')
            else:
                print(f'Partition directory {name} does not exist. We make this directory')
                self.dbx.files_create_folder_v2(path)
                self.dbx.files_upload(
                    file_json.read(),
                    f'{path}/{name}.json',
                    mode=dropbox.files.WriteMode("overwrite")
                    )
                logging.info('Saving to the Cloud success')
                print('Saving to the Cloud success')

        except ValidationErr:
            logging.info('Saving to the Cloud failed')
            print('Saving to the Cloud failed')

    def check_path_exists(self, path: str):
        '''This method checks if the directory already exists. 
        It will return a boolean value if it exists and a false'''
        try:
            self.dbx.files_get_metadata(path)
            return True
        except BaseException:
            return False
