import cbsodata
import logging
import dropbox

class CBSdata:
    def __init__(self):
        '''This connector retrieves all the generic description including the identifier. After that it will retrieve the data corresponding to the identifier.
        Finallly, it will write everything, as raw data, to a dropbox storage'''
        self.dbx = dropbox.Dropbox('sl.BMzXW-sbtWVAYTtZOUvPGVpdIKFCtWOvSa5CJborii9mlDarnQ6cvUGKVqz0LomSFsj5x0viXOwfWJ3hxO6SOMhO9Ps2OV8HMOMDj9dcFyJyG7RnzlKkQx7jZrpJLfT7IDlHa-Qv24Df')
        # self.tables = cbsodata.get_table_list()
        #logging.info("Retrieving all the identifiers")
        print("Retrieving all the identifiers")
        #self.list_of_identifier = [value['Identifier'] for value in self.tables]
        self.list_of_identifier = ['84669NED']
        self.writing_to_storage(self.list_of_identifier)

    def check_path_exists(self, path: str):
        try:
            self.dbx.files_get_metadata(path)
            return True
        except:
            return False

    def writing_to_storage(self, list_identifier: list):
        for identifier in list_identifier:
            #logging.info(f'retrieving data for table {identifier}')
            print(f'Retrieving data from {identifier}')
            data = cbsodata.get_data(identifier)
            path = f'/DigitalPowerCBSData/{identifier}'
            if self.check_path_exists(path):

            else:
                print(f'Partition directory {identifier} does not exist. We make this directory')
                self.dbx.files_create_folder_v2(path)


new = CBSdata()


