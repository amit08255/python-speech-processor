# Python Simple Speech/Text Processor

## About the project

This project is very simple speech/text processor built with Python. It uses Google for converting recorded audio into text, and then that text can be parsed and used to execute tasks. The feedback to user can be provided using audio which is generated using *mimic1* library.

## Setup Instructions

For text to speech it uses [https://github.com/MycroftAI/mimic1](mimic1). You can provided binary zip (built in Arch Linux, just extract binary file to root directory) or you can build your own.

For speech to text it uses Google speech recognition using SpeechRecognition library.

* Install speech recognition library:
    ```sh
    pip3 install SpeechRecognition --user
    ```

* Install pyaudio library:
    ```sh
    pip3 install pyaudio --user
    ```

* Install pynput library:
    ```sh
    pip3 install pynput --user
    ```

* Install portaudio:

    **Arch Linux:** ```sudo pacman -S portaudio```

    **Debian:** ```sudo apt-get install portaudio```

* For playing sound, we need mpg123 player:
    1. Download source from - https://downloads.sourceforge.net/mpg123/mpg123-1.28.1.tar.bz2
    2. Build using commands (from inside mpg123 folder)
        ```sh
        ./configure --prefix=/usr && make
        make check
        sudo make install
        ```

* Building mimic1 binary in linux:
    * Setup dev libraries using below commands:

        **Debian:** ```sudo apt-get install gcc make pkg-config automake libtool libasound2-dev```

        **Fedora:** ```sudo dnf install gcc make pkgconfig automake libtool alsa-lib-devel```

        **Arch Linux:** ```sudo pacman -S --needed install gcc make pkg-config automake libtool alsa-lib```

    * Clone repository: ```git clone https://github.com/MycroftAI/mimic1.git```
    * Go to mimic1 directory: ```cd mimic1```
    * Build using command: ```./dependencies.sh --prefix="/usr/local"```
    * Generate build scripts: ```./autogen.sh```
    * Configure: ```./configure --prefix="/usr/local"```
    * Build: ```make```
    * Copy *mimic* binary after build finished into root directory of this project.

## Usage

* Start using command: ```python3 main.py```
* To start listening press - `Ctrl + Alt + Q`
