import requests
import json
import os
import argparse


def get_minifiles(mini_id, headers):
    """
    Fetches the file URLs for a given mini ID.

    Args:
    mini_id (int): ID of the mini for which file URLs need to be fetched.
    headers (dict): Authorization headers for API request.

    Returns:
    A list of dictionaries containing file names and their corresponding tier for the given mini ID.
    """
    url = f"https://api.printableheroes.com/api/minifiles/get?miniId={mini_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        minifiles = []
        for key in data:
            if int(key) <= TIER:
                for item in data[key]:
                    minifiles.append({'fileName': item["FileName"], 'tier': key})
        return minifiles
    else:
        return []


def get_mini_name(mini_id, headers):
    """
    Fetches the name of a given mini ID.

    Args:
    mini_id (int): ID of the mini for which name needs to be fetched.
    headers (dict): Authorization headers for API request.

    Returns:
    A string containing the name of the given mini ID.
    """
    url = f"https://api.printableheroes.com/api/minis/get?id={mini_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["Name"]
    else:
        return f"Mini ID {mini_id}"


def download_minifiles(mini_id, headers):
    """
    Downloads the files for a given mini ID.

    Args:
    mini_id (int): ID of the mini for which files need to be downloaded.
    headers (dict): Authorization headers for API request.
    """
    mini_name = get_mini_name(mini_id, headers)
    minifiles = get_minifiles(mini_id, headers)
    if minifiles:
        for minifile in minifiles:
            url = f"https://api.printableheroes.com/files?mini_id={mini_id}&tier={minifile['tier']}&file_name={minifile['fileName']}"
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                os.makedirs(os.path.join("downloaded_files", mini_name), exist_ok=True)
                try:
                    with open(os.path.join("downloaded_files", mini_name, minifile['fileName']), "wb") as f:
                        f.write(response.content)
                        print(f"File {minifile['fileName']} for mini ID {mini_id} downloaded successfully.")
                except:
                    print("Upsi")
            else:
                print(
                    f"Failed to download file {minifile['fileName']} for mini ID {mini_id}. Status code: {response.status_code}")
    else:
        print(f"No files found for mini ID {mini_id}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download files from PrintableHeroes API')
    parser.add_argument('-t', '--tier', type=int, required=True, help='the maximum tier of the files to download')
    parser.add_argument('-a', '--authorization', type=str, required=True, help='the authorization bearer')
    args = parser.parse_args()

    headers = {"Authorization": f"Bearer {args.authorization}"}
    # Set the tier of minifiles to download
    TIER = args.tier
    problematic = []
    # Replace the authorization bearer with your own
    headers = {"Authorization": f"Bearer {args.authorization}"}

    # Set the range of mini IDs to download
    MINI_RANGE = range(719, 790)



    # Download minifiles
    for mini_id in MINI_RANGE:
        download_minifiles(mini_id, headers)
