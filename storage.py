import dropbox
import os


dbx = dropbox.Dropbox('sl.BMwUDC47VdoK_GQCUpq6mwVlD18s5W6Enz-ImofkH5UyVAN6JGR6F2l7D-leoMLXw_JAdv0AGw-zbhail8QuoknAdQDoQW1ZkKwIn88527jtZDJlXr5iDyIXzWl0LCSaud3mul-riYGG')

dropboxBaseDir = '/test_dropbox'
dropboxNewSubDir = '/new_empty_sub_dir/'
path = dropboxBaseDir+dropboxNewSubDir
directory = path+'data.json'

with path.open("rb") as f:
   # upload gives you metadata about the file
   # we want to overwite any previous version of the file
   dbx.files_upload(f.read(), directory, mode=dropbox.files.WriteMode("overwrite"))




# print(dbx.files_get_metadata(path))
# dbx.files_create_folder_v2(path)
#
# for entry in dbx.files_list_folder('').entries:
#     print(entry.name)
#
#
# def exists(path):
#     return os.path.basename(path) in [e.name for e in dbx.files_list_folder(path=os.path.dirname(path)).entries]
#
# def exists2(path):
#     try:
#         dbx.files_get_metadata(path)
#         return True
#     except:
#         return False
#
# # print(exists(path))
# print(exists2(path))