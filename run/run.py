import os
import json

urls = ["https://www.dropbox.com/s/z55j1usmg9nz2gt/The_Chimney_Sweeper.jpg",
"https://www.dropbox.com/s/rfkd5vtosri5lvz/The_Little_Boy_Lost.jpeg",
"https://www.dropbox.com/s/e4vxub2pnwvrtjx/The_Human_Abstract.jpeg",
"https://www.dropbox.com/s/u5zhg7mgl3cv815/The_Angel.jpg",
"https://www.dropbox.com/s/2kfzgzxlu1mwrzu/A_Poison_Tree.jpg",
"https://www.dropbox.com/s/8qjn2re3lmls5w7/The_Cloud_and_the_Pebble.jpg",
"https://www.dropbox.com/s/j8wy40c2p1a0dkx/The_Fly.jpg",
]
with open("text.json") as f:
    texts = json.load(f)


def run_code(i,j):
    if len(os.listdir(f"{i}/{j}"))!=0:
        print("이미 존재함.")
        return 0
    text = texts[str(i)][j]
    # os.system(f"cd {i}/{j}")
    command = f"cd {i}/{j};imagine " + f'"{text}"' + f" --start_image_path ../../{i}.jpg --batch_size 512 --iterations 32 --learning_rate 5e-06"
    if len(text.split(" "))<56:
        os.system(command)
    else:
        print("more than 77 words. story mode on.")
        command += " --create_story"
        os.system(command)

if __name__ == "__main__":
    for i in range(7):
        if not os.path.exists(str(i+1)+".jpg"):
            os.system("wget "+urls[i]+" -O "+str(i+1)+".jpg")

    ### mkdir
    for i in range(1,8):
        for j in ["W", "X", "Y", "Z"]:
            print(i,j)
            dir = os.path.join(str(i),j)
            if not os.path.exists(dir):
                os.makedirs(dir)
            run_code(i,j)


    # os.system('imagine')

    # import subprocess
    # process = subprocess.Popen(['echo', 'More output'],
    #                      stdout=subprocess.PIPE, 
    #                      stderr=subprocess.PIPE)
    # stdout, stderr = process.communicate()
    # stdout, stderr
