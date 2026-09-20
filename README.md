# Air Piano

An immersive, browser-based Air Piano. Play a virtual 2-octave piano in thin air using webcam hand tracking (powered by MediaPipe). 

Features:
- **Dual-hand support:** Both hands are tracked independently, allowing you to play chords and melodies just like a real piano.
- **Real piano layout:** Includes black and white keys mapped to a realistic layout. Use the top half of the piano zone for black keys, and the bottom half for white keys.
- **No GPU required:** Runs smoothly in the browser on a lightweight local Flask server.

## Demo

<img width="1917" height="916" alt="image" src="https://github.com/user-attachments/assets/befd6a10-e8c8-4c67-ace1-6ab525f01ba9" />
<img width="1917" height="916" alt="image" src="https://github.com/user-attachments/assets/ae9991be-a4d3-4bdc-b83c-5ad8eadbc81c" />



## Installation & Running

1. Install Python (3.11+ recommended).
2. Install the required dependencies:
   ```bash
   pip install Flask
   ```
3. Run the local web server:
   ```bash
   python server.py
   ```
4. Open your browser and navigate to `http://localhost:5000`.
5. Grant camera permissions, and start playing!
