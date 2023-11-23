# Importando bibliotecas pertinentes
import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

# Definindo parâmetros fixos das requests
payload = {}
headers = {
  'Authorization': 'Basic a2F1ZS5zaWx2YUBtZXVrOC5jb20uYnI6MnNjcWxxMzdrcWR6NngyZzZxcmt3NHNybGdreGtzdTNsdG43NHF5Zmw2cGo0cmc1bWFjcQ==',
  'Cookie': 'VstsSession=%7B%22PersistentSessionId%22%3A%222391fd1e-1ff0-4e9c-9bce-932bbc11474a%22%2C%22PendingAuthenticationSessionId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22CurrentAuthenticationSessionId%22%3A%2200000000-0000-0000-0000-000000000000%22%2C%22SignInState%22%3A%7B%7D%7D'
}
organization = 'k8bank'

# Função para obter detalhes do work item
def get_work_item_details(work_item_id):
    url = f"https://dev.azure.com/{organization}/_apis/wit/workItems/{work_item_id}?$expand=all&api-version=6.0"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

# Função para verificar se um work item é pai e obter seus work items filhos
def get_parent_with_child_work_items(start_id, end_id):
    for work_item_id in range(start_id, end_id + 1):
        details = get_work_item_details(work_item_id)
        if details and 'relations' in details:
            relations = details['relations']
            child_ids = [int(rel['url'].split('/')[-1]) for rel in relations if rel['rel'] == 'System.LinkTypes.Hierarchy-Forward']
            if child_ids:
                print(f"Parent ID: {work_item_id}, Child IDs: {child_ids}")

# Início do seu script principal
if __name__ == "__main__":
    start_id = 1    # O ID inicial do intervalo de work items pais
    end_id = 5000   # O ID final do intervalo de work items pais
    get_parent_with_child_work_items(start_id, end_id)
