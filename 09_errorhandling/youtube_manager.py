import json

def list_all_video(videos):
    print("\n")
    print("*" * 150)
    for index , video in enumerate(videos, start = 1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")
    print("\n")
    print("*" * 150)


def  add_video(videos):
    name = input("enter video name : ")
    time = input("enter the viodeo time: ")
    videos.append({'name' : name , 'time' : time})
    print("video added successfully !")
    save_data_helper(videos)

def update_video(videos):
    list_all_video(videos)
    index = int(input("enter the video no to update: "))
    if 1 <= index <= len(videos):
        name = input("enter the new video name : ")
        time = input("enter the new video time: ")
        videos[index - 1] = {'name': name, 'time' : time}
        print(index ,"successfully updated !") 
        save_data_helper(videos)
    else:
        print("invalid index selected !")

def deleat_video(videos):
    list_all_video(videos)
    index = int(input("enter the video no to be deleated : "))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        print(index ,"successfully deleated !")
        save_data_helper(videos)
    else:
        print("invalid index selected !")

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open("youtube.txt",'w') as file:
        json.dump(videos, file)

def main():
    videos = load_data()

    while True:
        print("\n youtube manager | enter your choice ")
        print("1. List of all youtube video ")
        print("2. add a youtube video ")
        print("3. update a youtube video details ")
        print("4. deleat a youtube video ")
        print("5.exit the app")
        choice = input("enter your choice : ")
        # print(videos)

        match choice: 
            case '1':
                list_all_video(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                deleat_video(videos)
            case '5':
                break
            case _:
                print("invalid choice !")


if __name__ == "__main__":
    main()

