from datetime import datetime
import requests

def clean_automation_users_with_api():
    url = "https://zonia-stg.com/api/automation/test-users/cleanup"
    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'X-Automation-Cleanup-Key': 'x6qgUsY4sDhtFNSiS0KeOP8MHY0sGFYBVWJzcs2Ycic',
        }

    response = requests.request("POST", url, headers=headers, data=payload)

    if response.status_code == 200:
        deleted_users = response.json().get("deletedCount")
        cutoff_date = response.json().get("cutoff")
        dt = datetime.fromisoformat(cutoff_date.replace("Z", "+00:00"))
        formatted_date = dt.strftime("%d-%m-%Y")
        print(f"Successfully deleted {deleted_users} user(s) created before {formatted_date}.")
    else:
        print(f"Error deleting user(s)!. API returned {response.status_code} and {response.text}.")


