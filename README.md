# Asteroids

This is my Asteroids game for the Boot.dev Asteroids game course.


### WSL <-> Windows configuration

#### On Windows

##### **Note:** One time I forgot to launch VcXsrv and was still able to spawn the PyGame window. I think it was all due to the command wsl --update

1. Open a Terminal
    - type command: wsl --update

### On WSL

1. edit ~/.bashrc to set DISPLAY variable
    - export DISPLAY=0 (for left screen; 1 for right screen, in multiscreen setup)
2. to test, install X11 tools
    - sudo apt install x11-apps -y
    -run: xeyes

## If X11 app didn't run

### On Windows

1. Install VcXsrv
2. Run XLaunch with below settings
    - Display Settings
        - Multiple Windows
    - Client Startup
        - Start no client
    - Extra Settings
        - Clipboard
            - Primary Selection
        - Native OpenGL
        - Disable Access Control
