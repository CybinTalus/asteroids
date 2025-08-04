# Asteroids

This is my Asteroids game for the Boot.dev Asteroids game course.


## WSL <-> Windows configuration

## Works for some; didn't work for me

#### On Windows

1. Install VcXsrv
2. Run XLaunch
    - Display Settings
        - Multiple Windows
    - Client Startup
        - Start no client
    - Extra Settings
        - Clipboard
            - Primary Selection
        - Native OpenGL
        - Disable Access Control

### On WSL

1. edit ~/.bashrc to set DISPLAY to your Windows IP, where VcXsrv is running, on display 0.screen 0
    - export DISPLAY=$(grep nameserver /etc/resolv.conf | awk '{print $2}')$:0.0

## Also didn't work for me for me

1. export XDG_RUNTIME_DIR=/home/<username>

## 

1. export LIBGL_ALWAYS_INDIRECT=1
