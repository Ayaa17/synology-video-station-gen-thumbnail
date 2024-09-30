# 使用官方 Python 映像
FROM python:3.9-slim

# 設定工作目錄
WORKDIR /app

# 複製當前目錄內容到容器中的 /app 目錄
COPY . /app

# 安裝必要的 Python 套件
RUN pip install imageio[ffmpeg]

# 設定容器啟動時執行的命令
CMD ["python", "extract_frame.py"]