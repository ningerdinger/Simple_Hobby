import cbsodata
import logging
import json
import dropbox
import os

class CBSdata:
    def __init__(self):
        '''This connector first retrieves all the generic description including the identifier'''

        self.dbx = dropbox.Dropbox('sl.BMwUDC47VdoK_GQCUpq6mwVlD18s5W6Enz-ImofkH5UyVAN6JGR6F2l7D-leoMLXw_JAdv0AGw-zbhail8QuoknAdQDoQW1ZkKwIn88527jtZDJlXr5iDyIXzWl0LCSaud3mul-riYGG')
        self.tables = cbsodata.get_table_list()

        logging.info("Retrieving all the identifiers")
        self.list_of_identifier = [value['Identifier'] for value in self.tables]
        self.writing_to_storage(self.list_of_identifier)

    def check_path_exists(self, path: str):
        try:
            self.dbx.files_get_metadata(path)
            return True
        except:
            return False

    def writing_to_storage(self, list_identifier: list):
        for identifier in list_identifier:
            logging.info(f'retrieving data for table {identifier}')
            data = cbsodata.get_data(identifier)
            path = f'/DigitalPowerCBSData/{identifier}'
            if self.check_path_exists(path):
                print('Hurray')
            else:
                self.dbx.files_create_folder_v2(path)


new = CBSdata()

# tables = cbsodata.get_table_list()
# print(tables)

# for item in tables:
# print(item['Identifier'])
# data = cbsodata.get_data('80072NED')
# print(data)
# for id in data:
#     print(id)

# df = pd.DataFrame(data)
# print(df)
# print(df.columns)
