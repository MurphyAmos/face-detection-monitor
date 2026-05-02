# Face Recognition Screen Monitor

A real-time face doorbell detection and recognition system that captures your screen, identifies faces against a known database, and sends email alerts when a match is found at the door.

---

## Features

- **Live screen capture** — continuously monitors a defined region of your display
- **Face detection** — locates faces in each captured frame using `face_recognition`
- **Face matching** — compares detected faces against a library of known encodings
- **Email alerts** — sends notifications via [Mailtrap](https://mailtrap.io/) when a recognized face is found
- **Face logging** — saves cropped face images with timestamps for review

---

## Requirements

- Python 3.9
- [CMake](https://cmake.org/) (required by `dlib`)
- A C++ compiler (Visual Studio Build Tools on Windows, GCC/Clang on Linux/macOS)

### Python Dependencies

```bash
pip install -r requirements.txt
```
---

## Project Structure

```
project/
├── main.py                  # Main entry point
├── data/
│   ├── faceData/            # Saved cropped face images (auto-created)
│   └── encodings/           # Known face images, organized by person
│       ├── John/
│       │   └── john.jpg
│       └── Jane/
│           └── jane.jpg
```

> **Tip:** Each subfolder inside `encodings/` should be named after the person it represents. The folder name is used as the identity label during recognition.

---

## Configuration

Before running, adjust the screen capture bounding box in `pullNConfirm.py` to match the area you want to monitor:

```python
bounding_box = {'top': 200, 'left': 0, 'width': 900, 'height': 800}
```

To enable email alerts, fill in the Mailtrap section with your credentials and uncomment in `pullNConfirm.py`:

```python
mail = mt.Mail(
    sender=mt.Address(email="hello@demomailtrap.co", name="Mailtrap Test"),
    to=[mt.Address(email="your@email.com")],
    subject="Camera Alert!",
    text=f"{name} detected at {time.time()}",
    category="Face Monitor Alert",
)

client = mt.MailtrapClient(token="YOUR_MAILTRAP_TOKEN")
client.send(mail)
```

---

## Usage

1. **Populate the encodings folder** with images of known individuals, one subfolder per person.

2. **Run the script:**

```bash
py -3.9 main.py
```

3. The monitor will start capturing the screen. Match results are printed in real time:

```
Face comparison result: John
Face comparison result: No face found
```

4. Recognized faces are saved to `data/faceData/` with timestamps (e.g., `face_2024-06-01_14-32-05.jpg`).

---

## How It Works

1. **Encoding load** — on startup, the script walks `data/encodings/`, loads each image, and generates a 128-dimension face encoding per person.
2. **Screen capture** — `mss` grabs a screenshot of the configured bounding box every frame.
3. **Frame sampling** — face detection runs every 25 frames to reduce CPU load.
4. **Comparison** — when faces are found, their encodings are compared to the known list using Euclidean distance via `face_recognition.compare_faces()`.
5. **Alert** — a match triggers an email alert and clears the detection buffer for the next cycle.

---

## Notes
- This tool is mainly used to monitor my Google Nest Camera. You should change you bounding parameters as that is what it is meant to fit. 
- The accuracy depends heavily on the quality and variety of images in the `encodings/` folder. Multiple photos per person (different angles, lighting) improve results.
- The `face_recognition` library is built on top of [dlib](http://dlib.net/) and uses a ResNet model trained on a large dataset of faces.
- This tool is intended for personal, ethical use cases such as home monitoring or access control on your own property.

---

## License

MIT License. See `LICENSE` for details.
