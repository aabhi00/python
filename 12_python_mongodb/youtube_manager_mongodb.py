from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://youtubepy:Abhi01@cluster0.4qpsngm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") #
#not a good idea to include id and password in code file

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)
def add_video(name,time):
      video_collection.insert_one({"name": name, "time": time})

def list_video():
      for video in video_collection.find():
            print(f"id : {video["_id"]}, Name: {video['name']} and TIme : {video['time']} ")

def update_video(video_id,new_name,new_time):
      video_collection.update_one(
            {'_id': ObjectId(video_id)},
            {"$set": {"name":new_name, "time" : new_time}}
      )
def deleat_video(video_id):
      video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n youtube manager")
        print("1. List of all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. exit the app")
        choice = input("enter your choice: ")
    
        match choice:
            case '1':
                    list_video()
            case '2':
                    name = input("enter the video name: ")
                    time = input("enter the video duration: ")
                    add_video(name,time)
            case '3':
                    video_id =input("enter the video id to update: ")
                    name = input("enter the update video name: ")
                    time = input("enter the update video duration: ")
                    update_video(video_id,name,time)
            case '4':
                    video_id = input("enter the video id to delete: ")
                    deleat_video(video_id)
            case '5':
                    break
            case _:
                    print("invalid choice !")


if __name__ == "__main__":
    main()