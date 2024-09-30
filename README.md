# Synology Video Station - Generate Thumbnails

This repository provides a solution to generate thumbnails for video files in Synology Video Station. The script
traverses directories to find all video files and extracts key frames to be used as thumbnails.

## Features

- Extract key frames from videos as thumbnails.

## Requirements

- Docker
- Docker Compose

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ayaa17/synology-video-station-gen-thumbnail
    cd synology-video-station-gen-thumbnail
    ```

2. Build the Docker image:

    ```bash
    docker-compose build
    ```

## Usage

1. Edit the `extract_frame.py` file to set the root directory you want to traverse:

    ```python
    if __name__ == "__main__":
        root_dir = 'path/to/your/videos'  # Replace with your directory
        find_videos_and_extract_frames(root_dir)
    ```

2. Run the Docker container:

    ```bash
    docker-compose up
    ```

The script will traverse the specified directory, find all video files, and generate thumbnails by extracting key
frames.

## Contributing

Feel free to submit issues and pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
