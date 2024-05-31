import os
import requests

api_token = ''
zone_id = ''

def create_dns_record(record):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, json=record)
    return response.json()

def read_txt_file(file_path):
    dns_records = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split()
            if len(parts) >= 5:
                name, ttl, _, record_type, content = parts[:5]
                record = {
                    "type": record_type,
                    "name": name.rstrip('.'),
                    "content": content,
                    "ttl": int(ttl),
                    "proxied": False 
                }
                dns_records.append(record)
    return dns_records

def add_dns_records(file_path):
    dns_records = read_txt_file(file_path)
    results = []
    for record in dns_records:
        result = create_dns_record(record)
        results.append(result)
    return results

def add_dns_records_from_multiple_files(file_paths):
    all_results = []
    for file_path in file_paths:
        print(f"Processing file: {file_path}")
        results = add_dns_records(file_path)
        all_results.extend(results)
    return all_results


file_paths = ["dns1.txt", "dns2.txt", "dns3.txt"]
results = add_dns_records_from_multiple_files(file_paths)
for result in results:
    print(result)
