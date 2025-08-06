# Asteroids

This is my Asteroids game for the Boot.dev Asteroids game course.


## WSL <-> Windows configuration

## Works for some; didn't work for me

#### On Windows

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
3. Open a Terminal
    - type command: wsl --update

### On WSL

1. edit ~/.bashrc to set DISPLAY variable
    - export DISPLAY=0 (for left screen; 1 for right screen, in multiscreen setup)
2. to test, install X11 tools
    - sudo apt install x11-apps -y
    -run: xeyes