import requests
import time
import json

def search(sequence):
    url = "https://bioinformatics.lt/comer/search/api/submit"
    
    # Data
    data = {
    'sequence': sequence,
    'database': 'PDB70',
    "hhsuite_in_use": "true",  # Enable HHblits
    "hmmer_in_use": "false",  # Disable HMMER
    'EVAL': '0.001'
    # measures statistical significance of sequence alignement.
    # lower evalue means sequence is more significant/similar
    }
    
    # Request
    try:
        response = requests.post(url, data=data)
        result = response.json()

        if result.get('success'):
            job_id = result.get('job_id')
            print(f'Job Submitted. Job_id = {job_id}')
            return job_id
        else:
            print('Error Submitting Job:', result.get('form_errors'))
            return None
    except requests.exceptions.RequestException as error_message:
        print(f'Search Request failed: {error_message}')
        return None

def status(job_id):
    url = f"https://bioinformatics.lt/comer/search/api/job_status/{job_id}"
    response = requests.get(url)
    if response.status_code == 200:
        status_data = response.json()
        return status_data.get("status"), status_data.get('log')
    else:
        return None

def results(job_id):
    url = f"https://bioinformatics.lt/comer/search/api/results_json/{job_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def run(sequence):
    job_id = search(sequence)
    if job_id:
        while True:
            status_check, log_message = status(job_id)
            if status_check == 'finished':
                print('Complete. Fetching results')
                
                result_data = results(job_id)
                
                with open('homo_search_results.txt', 'w') as file:
                    json.dump(result_data, file, indent=4) 
                return(result_data)
            
            
            elif status_check == 'failed':
                print('Job failed.')
                return None
            else:
                if log_message:
                    print(log_message)
                else:
                    print('Waiting... ')
                time.sleep(5)
    else:
        return None
    
sequence = '''>sp|P68871|HBB_HUMAN Hemoglobin subunit beta OS=Homo sapiens OX=9606 GN=HBB PE=1 SV=2
MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPK
VKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFG
KEFTPPVQAAYQKVVAGVANALAHKYH'''
run(sequence)
