import json
import os

def create_assistant(client):
  assistant_file_path = 'assistant.json'

  if os.path.exists(assistant_file_path):
    with open(assistant_file_path, 'r') as file:
      assistant_data = json.load(file)
      assistant_id = assistant_data['assistant_id']
      print("Loaded existing assistant ID.")
  else:
    file = client.files.create(file=open("knowledge.docx", "rb"),
                               purpose='assistants')

    assistant = client.beta.assistants.create(instructions="""
          Appsure Assist will maintain a professional demeanor, ensuring all interactions are courteous and respectful. 
          It will convey an optimistic outlook, instilling confidence in users about Appsure's ability to meet their needs.
          The GPT will respond in a manner that is both informative and positive, 
          reflecting Appsure's forward-thinking and customer-centric approach. 
For contact details, tell the end user to contact our Sydney office. Sydney, Australia info@appsure.com.au
          """,
                                              model="gpt-4-1106-preview",
                                              tools=[{
                                                  "type": "retrieval"
                                              }],
                                              file_ids=[file.id])

    with open(assistant_file_path, 'w') as file:
      json.dump({'assistant_id': assistant.id}, file)
      print("Created a new assistant and saved the ID.")

    assistant_id = assistant.id

  return assistant_id
