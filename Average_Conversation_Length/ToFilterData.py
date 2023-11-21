import json

# Specify the path to your JSON file
#json_file_path = 'snapshot_20230831/20230831_061926_discussion_sharings.json'
#path = 'snapshot_20230831/discussions.json'
#json_file_path = 'snapshot_20230831/20230831_060603_pr_sharings.json'
#path = 'snapshot_20230831/prsharing.json'
#json_file_path = 'snapshot_20230831/20230831_061759_issue_sharings.json'S
#path = 'snapshot_20230831/issuesharing.json'
#json_file_path = 'snapshot_20230831/20230831_063412_commit_sharings.json'
#path = 'snapshot_20230831/commitsharing.json'
#json_file_path = 'snapshot_20230831/20230831_072722_file_sharings.json'
#path = 'snapshot_20230831/filesharing.json'
json_file_path = 'snapshot_20230831/20230831_073827_hn_sharings.json'
path = 'snapshot_20230831/hnsharing.json'

# Open the file and load the JSON data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)

# Now 'data' contains the contents of your JSON file as a Python dictionary
# print(data)
sources = data["Sources"]
print(len(sources))
i=0
for objects in sources:
    something = objects['ChatgptSharing']
    
    for some in something:
        if 'Conversations' in some:
            prom = some['Conversations']
            # with open(path, 'a', encoding='utf-8') as output_file:
            #     json.dump(prom, output_file, ensure_ascii=False)
            #     output_file.write('\n')
                # print(prom, file=output_file)
            # print(prom)
            # for prompts in prom:
                # questions = prompts['Prompt'].encode('utf-8')
            with open(path, 'a', encoding='utf-8') as output_json_file:
                output_json_file.seek(0, 2)  # Move the cursor to the end of the file
                if output_json_file.tell() > 0:
                    output_json_file.write(',')
                json.dump(prom, output_json_file, ensure_ascii=False)
                output_json_file.write('\n')
        else:
            continue