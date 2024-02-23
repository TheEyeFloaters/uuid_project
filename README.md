# Video Frame Extraction Tool

This script is designed to extract frames from video files and save them as individual images with unique identifiers. It utilizes OpenCV for video processing and UUID module to generate unique filenames for the extracted frames.

## Usage

### Prerequisites
- Python 3.x
- OpenCV (`cv2`), UUID, and OS modules

### Instructions
1. Ensure you have Python installed on your system.
2. Install the required modules using pip:
    ```
    pip install opencv-python-headless
    ```
3. Place your video files in the `Video Files/` directory.
4. Run the script.
    ```bash
    python frame_extractor.py
    ```
5. Extracted frames will be saved in the `frames/` directory.

## Script Explanation

### `save_frames_with_uuid(input_file, output_directory)`
- Function to extract frames from a video file.
- Parameters:
  - `input_file`: Path to the input video file.
  - `output_directory`: Directory to save the extracted frames.
- It reads the video file, extracts frames at every 5th frame, generates a unique filename for each frame, and saves the frames as JPEG images in the specified output directory.

### Frame Extraction Loop
- The script iterates over each file in the `Video Files/` directory.
- If the file has a `.mp4` or `.avi` extension, it calls the `save_frames_with_uuid` function to extract frames from the video.

## File Structure
- `frame_extractor.py`: Main script for extracting frames.
- `Video Files/`: Directory containing input video files.
- `frames/`: Directory to save the extracted frames.

