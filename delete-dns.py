import requests
from concurrent.futures import ThreadPoolExecutor

# ตั้งค่า API Token และ Zone ID ของคุณ
api_token = ''
zone_id = ''

# กำหนด URL สำหรับ API ของ Cloudflare เพื่อดึงรายการ DNS records
# กำหนด URL สำหรับ API ของ Cloudflare เพื่อดึงรายการ DNS records
list_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records"

# กำหนด headers สำหรับการเรียก API
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

def get_dns_records():
    """ดึงรายการ DNS records ทั้งหมด"""
    dns_records = []
    page = 1
    per_page = 100  # จำนวน records ต่อหน้า (maximum คือ 100 ตาม API ของ Cloudflare)
    while True:
        params = {
            'page': page,
            'per_page': per_page
        }
        response = requests.get(list_url, headers=headers, params=params)
        if response.status_code == 200:
            result = response.json()["result"]
            if not result:
                break
            dns_records.extend(result)
            page += 1
        else:
            print("มีข้อผิดพลาดในการดึงรายการ DNS records")
            print(response.status_code)
            print(response.json())
            break
    return dns_records

def delete_dns_record(record_id):
    """ลบ DNS record ตาม ID"""
    delete_url = f"https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}"
    delete_response = requests.delete(delete_url, headers=headers)
    if delete_response.status_code == 200:
        print(f"DNS record {record_id} ถูกลบเรียบร้อยแล้ว!")
    else:
        print(f"มีข้อผิดพลาดในการลบ DNS record {record_id}")
        print(delete_response.status_code)
        print(delete_response.json())

# ดึงรายการ DNS records ทั้งหมด
dns_records = get_dns_records()

# ลบ DNS records ที่ดึงมาแบบขนาน
if dns_records:
    with ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(lambda record: delete_dns_record(record['id']), dns_records)
else:
    print("ไม่มี DNS records ที่จะลบหรือไม่พบ DNS records")
