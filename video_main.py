import tello_video
from tello_control_ui import TelloUI


def main():
    drone = tello_video.Tello('192.168.10.1', 8889)
    vplayer = TelloUI(drone, "./img/")

    # start the Tkinter mainloop
    vplayer.root.mainloop()


if __name__ == "__main__":
    main()