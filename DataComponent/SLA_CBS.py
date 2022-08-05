import sys
import logging
# import os
import json
from xml.dom import ValidationErr
import cbsodata
from utilities import writing_to_DB as wDB


class CBSdata:
    '''This connector retrieves all the generic description including the identifier.
        After that it will retrieve the data corresponding to the identifier.
        Finallly, it will write everything, as raw data, to a dropbox storage'''
    def __init__(self, key: str):
        self.key = key
        # self.tables = cbsodata.get_table_list()
        logging.info("Retrieving all the identifiers")
        print("Retrieving all the identifiers")
        #self.list_of_identifier = [value['Identifier'] for value in self.tables]
        self.list_of_identifier = ['84669NED', '83583NED', '83582NED']
        self.writing_to_json(self.list_of_identifier)

    def save_dict_to_json(self, data_dict: dict, identifier: str):
        '''Converts a dictionary to JSON file and also saves it on your local drive'''
        with open(f'storage/{identifier}.json', 'w', encoding="utf8") as f:
            json.dump(data_dict, f, indent=1)

    def writing_to_json(self, list_identifier: list):
        '''This method first retrievers the data based on the identifier.
        It will then convert the dictionary into a JSON format on your local drive
        It will then proceed to upload from your local drive toward Dropbox.
        NOTE: reason why it doesn't save directly to Dropbox Cloud is because
        Dropbox doesn't support this functionality'''
        for identifier in list_identifier:
            logging.info(f'retrieving data for table {identifier}')
            data = cbsodata.get_data(identifier)
            logging.info(f'converting data to {identifier}.json')
            self.save_dict_to_json(data, identifier)
            path = f'/DigitalPowerCBSData/Bronze/{identifier}'
            wDB.WritingToDB(name=identifier, path=path, key=self.key)


token = "sl.BMz5d0gTykmAfhUmZtYNTCTLhsxJ7ONhuwKBXX4aO2kwXOKZDSoh87m6Im7Q3VO0WnBwv4RakjpOnknhpHuQ3rwFDgPl4oe08EzujJlttbWJoTmNH9NaEsOEnSjkJln9NBfXybD5iP6X"
new = CBSdata(token)
