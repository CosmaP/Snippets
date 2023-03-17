

    def get_file_properties_from_folder_for_import(self, folder_name):
        files_list = self._get_files_list(folder_name)
        properties_list = []
        for file in files_list:
            file_dict = {
                'file_name': file.name,
                'author' : None,
                'time_created': file.time_created,
                'major_version': file.major_version,
                'minor_version': file.minor_version,
                'file_size': file.length,
                'modifiedby' :None,                
                'time_last_modified': file.time_last_modified
            }

            # Retrieve the author's display name
            if file.author:
                author_url = f'https://graph.microsoft.com/v1.0/users/{file.author.users.id}'
                response = requests.get(author_url, headers={'Authorization': 'Bearer ' + access_token})
                author = json.loads(response.content)
                file_dict['author'] = author['displayName']

            # Retrieve the modified by user's display name
            if file.last_modified_by:
                modifiedby_url = f'https://graph.microsoft.com/v1.0/users/{file.last_modified_by.user.id}'
                response = requests.get(modifiedby_url, headers={'Authorization': 'Bearer ' + access_token})
                modifiedby = json.loads(response.content)
                file_dict['modifiedby'] = modifiedby['displayName']


            properties_list.append(file_dict)
            file_dict = {}
        return properties_list

