AppImage binary for Electrum
============================

This assumes an Ubuntu 18.04 host, but it should not be too hard to adapt to another
similar system. The docker commands should be executed in the project's root
folder.

1. Install Docker

    ```
    $ sudo apt-get install docker.io
    ```
2. Start Docker

    ```
    $ sudo systemctl start docker
    ```

3. Build image

    ```
    $ sudo docker build --no-cache -t electrum-appimage-builder-img contrib/build-linux/appimage
    ```

4. Build binary

    ```
    $ sudo docker run -it \
        --name electrum-appimage-builder-cont \
        -v $PWD:/opt/electrum \
        --rm \
        --workdir /opt/electrum/contrib/build-linux/appimage \
        electrum-appimage-builder-img \
        ./build.sh
    ```

5. The generated binary is in `./dist`.


## FAQ

### How can I see what is included in the AppImage?
Execute the binary as follows: `./electrum*.AppImage --appimage-extract`
