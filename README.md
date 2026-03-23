# QR Code Scanner

A simple Python script to scan QR codes using your device camera  

## Features

- Scan QR codes in real-time using your camera
- Optional ASCII visualization of QR codes in the console
- Works with any available camera (default: camera index 0)

For easier access, you can place the script in a directory included in your system `PATH`.
This allows you to run it from anywhere like a command:

```bash
$ qrscan
```

## Requirements

- Python 3.x
- OpenCV (`cv2`)

Install OpenCV with:

```bash
$ pip install opencv-python
````

## Optional Features

### ASCII QR Code Display

You can display the detected QR code as ASCII art in the console.

```bash
$ qrscan -d
```

You can also specify your own character. Default is `■`.

```bash
$ qrscan -d #
```
