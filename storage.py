import dropbox

dbx = dropbox.Dropbox('sl.BMzeDs1lImzutaO611_dWZRewAGnsm2nuh2hYrdr7OCc9qI01YfhdzyDq1sWukXppuyzkqOEbXXGH_97Gef792FZ2ydlb6VckTGHbh3Dm9Jmy6NJyf4p0t6FC3Fhaka9GXaQ6iJ9USvL')

dropboxBaseDir = '/test_dropbox'
dropboxNewSubDir = '/new_empty_sub_dir'

dbx.files_create_folder_v2(dropboxBaseDir + dropboxNewSubDir)

for entry in dbx.files_list_folder('').entries:
    print(entry.name)