import webbrowser

class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False

    def open_video(self):
        webbrowser.open(self.link)
        self.seen = True
###########  INPUT VIDEO ###########
def input_video():
    title = input("Enter title: ") + "\n"
    link = input("Enter link: ") + "\n"
    video = Video(title, link)
    return video

########### INPUT VIDEOS ###########
def input_videos():
    videos = []
    total_video = int(input("Enter how many videos: "))
    for i in range(total_video):
        print("Enter video", i+1)
        video = input_video()
        videos.append(video)
    return videos

########## WRITE VIDEO TO TEXT ##########
def write_video_to_text(video, file):
    file.write(video.title)
    file.write(video.link)

########## WRITE VIDEOS TO TEXT ##########
def write_videos_to_text(videos, file):
    total = len(videos)
    file.write(str(total) + "\n")
    for i in range(total):
        write_video_to_text(videos[i], file)

######### READ VIDEO FROM TEXT ##########
def read_video_from_text(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video

######### READ VIDEOS FROM TEXT ##########
def read_videos_from_text(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        video = read_video_from_text(file)
        videos.append(video)
    return videos

########### OUTPUT VIDEO ###########
def print_video(video):
    print("     + Video title: ", video.title, end="")
    print("     + Video link: ", video.link, end="")
    
########### OUTPUT VIDEOS ###########
def print_videos(videos):
    for i in range(len(videos)):
        print("Video number %d: "  %(i+1) )
        print_video(videos[i])

########### INPUT PLAYLIST ###########
def input_playlist():
    playlist_name = input("Enter Playlist name: ") + "\n"
    playlist_description = input("Enter Playlist description: ") + "\n"
    playlist_rating = input("Enter playlist rating (1-5): ") + "\n"
    videos = input_videos()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, videos)
    return playlist

########### WRITE PLAYLIST TO TEXT ###########
def write_playlist_to_text(playlist):
    with open("data.txt", "w") as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
        write_videos_to_text(playlist.videos, file)

########### READ PLAYLIST FROM TEXT###########
def read_playlist_from_text():
    with open("data.txt", "r") as file:
        playlist_name = file.readline()
        playlist_description = file.readline()
        playlist_rating = file.readline()
        videos = read_videos_from_text(file)
        playlist = Playlist(playlist_name, playlist_description, playlist_rating, videos)
    return playlist

########### PRINT PLAYLIST ###########
def print_playlist(playlist):
    print("====================")
    print("Name playlist: ", playlist.name, end="")
    print("Description playlist: ", playlist.description, end="")
    print("Rating playlist: ", playlist.rating, end="")
    print_videos(playlist.videos)

################# SHOW MENU #################
def show_menu():
    print("\n")
    print("|===============MENU==============|")
    print("|=================================|")
    print("|                                 |")
    print("|   Option 1: Create playlist.    |")
    print("|   Option 2: Show playlist.      |")
    print("|   Option 3: Play a playlist.    |")
    print("|   Option 4: Add a playlist.     |")
    print("|   Option 5: Update a playlist.  |")
    print("|   Option 6: Delete a video      |")
    print("|   Option 7: Save and Exit.      |")
    print("|                                 |")
    print("|=============NGOCSON=============|")
    print("\n")

################ SELECT IN RANGE ##################
def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:  #isdigit kiem tra xem choice co phai la so hay khong
        choice = input(prompt)
    choice = int(choice)
    return choice

############### PLAY TO PLAYLIST ################
def play_list(playlist):
    total_videos = len(playlist.videos)
    print_videos(playlist.videos)
    choice = select_in_range("Select a video (1," + str(total_videos) + "): ", 1, total_videos)
    print("Open video: " + playlist.videos[choice-1].title + " - " + playlist.videos[choice-1].link, end="")
    playlist.videos[choice-1].open_video()

#################### ADD VIDEO ##################
def add_videos(playlist):
    print("Enter new video information: ")
    new_video_title = input("Enter new video title: ") + "\n"
    new_video_link = input("Enter new video link: ") + "\n"
    new_video = Video(new_video_title, new_video_link)
    playlist.videos.append(new_video)
    return playlist
################### UPDATE PLAYLIST ###############
def update_playlist(playlist):
    print("Update playlist?")
    print("1. Name.")
    print("2. Description")
    print("3. Rating")
    choice_update = select_in_range("Enter what you want to update (1-3): ", 1, 3)
    if choice_update == 1:
        new_playlist_name = input("Enter new name for playlist: ") + "\n"
        playlist.name = new_playlist_name
        print("\nUpdate successfully.\n")
        return playlist
    elif choice_update == 2:
        new_playlist_description = input("Enter new description for playlist: ") + "\n"
        playlist.description = new_playlist_description
        print("\nUpdate successfully.\n")
        return playlist
    elif choice_update == 3:
        new_playlist_rating = str(select_in_range("Enter new rating for playlist (1,5): ", 1, 5)) +  "\n"
        playlist.rating = new_playlist_rating
        print("\nUpdate successfully.\n")
        return playlist
################### DELETE VIDEO ################
def delete_video(playlist):
    print_videos(playlist.videos)
    choice_video = select_in_range("Enter video you want to delete: ",1, len(playlist.videos))
    # Cách 1:
    del playlist.videos[choice_video-1]
    # Cách 2:
    new_playlist = []
    for i in range(len(playlist.videos)):
        if i == choice_video - 1:
            continue
        new_playlist.append(playlist.videos[i])
        playlist.videos = new_playlist

    print("Delete successfully !")
    return playlist

    # Update name
    # Update description
    # Update rating

def main():
    try:
        playlist = read_playlist_from_text()
        print("Load data sucessfully!!!")
    except:
        print("Welcome first user !!!")
    while True:
        show_menu()
        # choice = int(input("Select an option (1-7): "))
        choice = select_in_range("Select an option (1-7): ", 1, 7)
        if choice == 1:
            playlist = input_playlist()
            input("\nPress Enter to continute...\n")
        elif choice == 2:
            print_playlist(playlist)
            input("\nPress Enter to continute...\n")
        elif choice == 3:
            play_list(playlist)
            input("\nPress Enter to continute...\n")
        elif choice == 4:
            playlist = add_videos(playlist)
            input("\nPress Enter to continute...\n")
        elif choice == 5:
            update_playlist(playlist)
            input("\nPress Enter to continute...\n")
        elif choice == 6:
            delete_video(playlist)
            input("\nPress Enter to continute...\n")
        elif choice == 7:
            write_playlist_to_text(playlist)
            break
        else:
            print("Exist")
            break
        
main()