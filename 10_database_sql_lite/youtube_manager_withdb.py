import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )

''')

def list_video():
    cursor.execute("SELECT * FROM videos")
    print("* " * 79)
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)",(name , time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE id = ? ",(new_name, new_time, video_id))
    conn.commit()

def deleat_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_id,))
    conn.commit()


def main():
    while True:
        print("youtube manager app with DB")
        print("1. List all videos")
        print("2. add videos")
        print("3. Update videos")
        print("4. Deleat videos")
        print("5. Exit app")
        print("\n")

        choice = input("enter your choice : ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("enter the video name : ")
            time = input("enter the duration of the video : ")
            add_video(name, time)
            print("video adeed succesfully ! \n")
        elif choice == '3':
            list_video()
            video_id = input("enter the video ID to update : ")
            name = input("enter the video name : ")
            time = input("enter the duration of the video : ")
            update_video(video_id, name, time)
            print("video updated succesfully ! \n")
        elif choice == '4':
            list_video()
            video_id = input("enter the video ID to deleat :")
            deleat_video(video_id)
            print("video deleted succesfully !\n")
        elif choice == '5':
            break
        else:
            print("invalid choice ! \n")

    conn.close()

if __name__ == "__main__":
    main()