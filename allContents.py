#produce code below to get api call method using end point "https://tm.tapi.videoready.tv/homescreen/pub/api/v4/rail/seeAll?limit=1000&id=4203"
import requests
import json as json

content_list = []

def getContentInfo(contentId):
    url = "https://tm.tapi.videoready.tv/content-detail/pub/api/v1/vod/{}".format(contentId)
    x = requests.get(url)

    content_meta = x.json()['data']['meta']
    content_genre = x.json()['data']['meta']['genre'][0]
    content_detail_dict = x.json()['data']['detail']
    content_logo = content_meta.get('posterImage','')



    onecontent = {
        "content_id": str(contentId),
        "content_name": content_meta.get('title', ''),
        "content_license_url": content_detail_dict.get('dashWidewineLicenseUrl', ''),
        "content_url": content_detail_dict.get('dashWidewinePlayUrl', ''),
        "content_entitlements": content_detail_dict.get('entitlements', ''),
        "content_logo": content_logo,
        "content_genre": content_genre
    }
    content_list.append(onecontent)

def savecontentsToFile():
    print(len(content_list))
    with open("allContents.json", "w") as content_list_file:
        json.dump(content_list, content_list_file)
        content_list_file.close()


def processChunks(content_lists):
    for content in content_lists:
        print("Getting contentId:{}".format(content.get('id', '')))
        content_id = str(content.get('id', ''))
        getContentInfo(content_id)


def getAllContents():
    ids=[2700,2799,4313,4316,4390,4593,4390,4593,4397,4391,4203]
    for id in ids:
        url = "https://tm.tapi.videoready.tv/homescreen/pub/api/v4/rail/seeAll?limit=1000&id={}".format(id)
        x = requests.get(url)
        content_list = x.json()['data']['contentList']
        print("Total contents fetched:", len(content_list))
        print("Fetching content info..........")
        processChunks(content_list)
        print("Saving all to a file.... " + str(len(content_list)))
        savecontentsToFile()

if __name__ == '__main__':
    getAllContents()

