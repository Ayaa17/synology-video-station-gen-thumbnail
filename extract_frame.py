import os
import imageio


def extract_key_frame(video_path, output_image_path, frame_number=100):
    try:
        # 讀取影片
        video = imageio.get_reader(video_path, 'ffmpeg')

        # 抓取指定影格
        frame = video.get_data(frame_number)

        # 儲存影格為圖像
        imageio.imwrite(output_image_path, frame)
        print(f"影格已儲存為 {output_image_path}")
    except Exception as e:
        print(f"無法處理 {video_path}: {e}")


def find_videos_and_extract_frames(root_dir):
    video_extensions = ('.mp4', '.avi', '.mov', '.mkv')  # 可以根據需要擴展副檔名

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(video_extensions):
                video_path = os.path.join(dirpath, filename)
                output_image_path = os.path.join(dirpath, f"{os.path.splitext(filename)[0]}.jpg")
                extract_key_frame(video_path, output_image_path)


if __name__ == "__main__":
    root_dir = '../video/'  # 替換成你要遍歷的根目錄
    find_videos_and_extract_frames(root_dir)
