import os
import tkinter as tk
from tkinter import filedialog, messagebox
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame


# ======== INIT ========
root = tk.Tk()
root.title("MUSIC PLAYER")
root.geometry("500x350")

# ===== VARIABLES =====
folder = ""
music_files = []
current_index = -1
paused = False
corrupted_files = set()

# ===== PYGAME INIT =====
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=2048)

# ===== MENUBAR =====
menubar = tk.Menu(root)
root.config(menu=menubar)

def loadMusic():
    global folder, music_files, corrupted_files, current_index
    folder = filedialog.askdirectory()
    if not folder:
        return
    
    music_files = []
    corrupted_files = set()
    current_index = -1
    songList.delete(0, tk.END)
    
    for file in os.listdir(folder):
        if file.lower().endswith((".mp3", ".wav", ".ogg", ".webm", ".m4a")):
            music_files.append(file)
            songList.insert(tk.END, file)
    
    if music_files:
        status_label.config(text=f"✅ Loaded {len(music_files)} songs", fg="green")
    else:
        status_label.config(text="❌ No music found", fg="red")

organiseMenu = tk.Menu(menubar, tearoff=False)
organiseMenu.add_command(label="Select Folder", command=loadMusic)
menubar.add_cascade(label="Organise", menu=organiseMenu)

# ===== SONG LIST =====
songList = tk.Listbox(root, bg="black", fg="white", width=80, height=12)
songList.pack(pady=10)

# ===== STATUS LABEL =====
status_label = tk.Label(root, text="Select a folder to load music", fg="gray", bg="black")
status_label.pack(pady=5)

# ===== BUTTONS =====
script_dir = os.path.dirname(os.path.abspath(__file__))
imgs_folder = os.path.join(script_dir, "imgs")

try:
    PlayBtnImg = tk.PhotoImage(file=os.path.join(imgs_folder, "play.png"))
    nextBtnImg = tk.PhotoImage(file=os.path.join(imgs_folder, "next.png"))
    PauseBtnImg = tk.PhotoImage(file=os.path.join(imgs_folder, "pause.png"))
    PreviousBtnImg = tk.PhotoImage(file=os.path.join(imgs_folder, "previous.png"))
except:
    print("Warning: Button images not found, using text buttons")
    PlayBtnImg = None

control_frame = tk.Frame(root)
control_frame.pack()

if PlayBtnImg:
    PlayBtn = tk.Button(control_frame, image=PlayBtnImg, borderwidth=0)
    nextBtn = tk.Button(control_frame, image=nextBtnImg, borderwidth=0)
    PauseBtn = tk.Button(control_frame, image=PauseBtnImg, borderwidth=0)
    PreviousBtn = tk.Button(control_frame, image=PreviousBtnImg, borderwidth=0)
else:
    PlayBtn = tk.Button(control_frame, text="▶ PLAY", width=10)
    nextBtn = tk.Button(control_frame, text="⏭ NEXT", width=10)
    PauseBtn = tk.Button(control_frame, text="⏸ PAUSE", width=10)
    PreviousBtn = tk.Button(control_frame, text="⏮ PREV", width=10)

PreviousBtn.grid(row=0, column=0, padx=7, pady=10)
PauseBtn.grid(row=0, column=1, padx=7, pady=10)
PlayBtn.grid(row=0, column=2, padx=7, pady=10)
nextBtn.grid(row=0, column=3, padx=7, pady=10)


# ===== PLAY FUNCTIONS =====
def play_song():
    global current_index, paused
    
    if not music_files:
        status_label.config(text="⚠️ Load music first!", fg="orange")
        return
    
    selection = songList.curselection()
    if selection:
        current_index = selection[0]
    elif current_index == -1:
        current_index = 0
    
    # Try to play current song
    max_attempts = len(music_files)
    attempts = 0
    
    while attempts < max_attempts:
        selected_song = music_files[current_index]
        
        # Skip known corrupted
        if selected_song in corrupted_files:
            print(f"⏭️ Skipping corrupted: {selected_song}")
            current_index = (current_index + 1) % len(music_files)
            attempts += 1
            continue
        
        song_path = os.path.join(folder, selected_song)
        
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play()
            paused = False
            
            # Update UI
            for i in range(len(music_files)):
                if music_files[i] not in corrupted_files:
                    songList.itemconfig(i, {'bg': 'black', 'fg': 'white'})
            
            songList.selection_clear(0, tk.END)
            songList.selection_set(current_index)
            songList.see(current_index)
            songList.itemconfig(current_index, {'bg': 'green', 'fg': 'white'})
            
            status_label.config(text=f"🎵 Playing: {selected_song[:40]}", fg="lime")
            print(f"✅ Playing: {selected_song}")
            return True
            
        except Exception as e:
            print(f"❌ Cannot play: {selected_song} - {e}")
            corrupted_files.add(selected_song)
            songList.itemconfig(current_index, {'bg': 'red', 'fg': 'white'})
            
            # Try next song
            current_index = (current_index + 1) % len(music_files)
            attempts += 1
    
    # All files failed
    status_label.config(text="❌ All files corrupted!", fg="red")
    messagebox.showerror("Error", 
        "All music files are corrupted!\n\n" +
        "YT-DLP downloads can be corrupted.\n\n" +
        "FIX:\n" +
        "1. Re-download with: yt-dlp -x --audio-format mp3 [URL]\n" +
        "2. Or use different music files")
    return False


def pause_song():
    global paused
    if not pygame.mixer.music.get_busy() and not paused:
        status_label.config(text="⚠️ No music playing", fg="orange")
        return
    
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        status_label.config(text="▶️ Resumed", fg="lime")
    else:
        pygame.mixer.music.pause()
        paused = True
        status_label.config(text="⏸️ Paused", fg="yellow")


def next_song():
    global current_index
    if not music_files:
        return
    
    current_index = (current_index + 1) % len(music_files)
    play_song()


def previous_song():
    global current_index
    if not music_files:
        return
    
    current_index = (current_index - 1) % len(music_files)
    play_song()


# ===== BUTTON COMMANDS =====
PlayBtn.config(command=play_song)
PauseBtn.config(command=pause_song)
PreviousBtn.config(command=previous_song)
nextBtn.config(command=next_song)

# ===== AUTO-PLAY NEXT =====
def check_music_end():
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            print("🔄 Song ended, playing next...")
            next_song()
    root.after(100, check_music_end)

pygame.mixer.music.set_endevent(pygame.USEREVENT)

def main():
    check_music_end()
    root.mainloop()

if __name__ == "__main__":
    main()