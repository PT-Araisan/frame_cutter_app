import cv2
import os

updatelock = False
windowname = 'movie'
trackbarname_frame = 'frame'
trackbarname_speed = 'speed'
ESC_KEY = 0x1b
interval = 20  
playing = False

VALID_EXTENSIONS = {".mp4", ".avi", ".mov", ".mkv"}

while True:
    video_path = input("動画ファイルのパスを入力してください: ")
    _, ext = os.path.splitext(video_path)
    if ext.lower() not in VALID_EXTENSIONS:
        print(f"サポートされていない拡張子です。サポートされている形式: {', '.join(VALID_EXTENSIONS)}")
        continue
    if not os.path.isfile(video_path):
        print("指定されたファイルが存在しません。正しいパスを入力してください。")
        continue

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("動画ファイルを開けませんでした。別のファイルを試してください。")
        continue
    break

def onTrackbarSlide(pos):
    global updatelock
    updatelock = True
    cap.set(cv2.CAP_PROP_POS_FRAMES, pos)
    updatelock = False

def onSpeedTrackbar(pos):
    global interval
    interval = max(1, 100 - pos)  

def play_video():
    global updatelock, interval, playing

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    cv2.namedWindow(windowname, cv2.WINDOW_NORMAL)
    if frames > 0:
        cv2.createTrackbar(trackbarname_frame, windowname, 0, frames, onTrackbarSlide)

    cv2.createTrackbar(trackbarname_speed, windowname, 50, 100, onSpeedTrackbar)
    cv2.setWindowProperty(windowname, cv2.WND_PROP_TOPMOST, 1)

    while cap.isOpened():
        if updatelock:
            continue

        if playing:  
            ret, frame = cap.read()
            if not ret:
                break

            curpos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            cv2.setTrackbarPos(trackbarname_frame, windowname, curpos)
            cv2.imshow(windowname, frame)

        key = cv2.waitKey(interval) & 0xFF  

        if key == ESC_KEY:
            break
        elif key == 32:  # スペースキーで再生・一時停止
            playing = not playing
            print("再生中" if playing else "一時停止中")
        elif key == ord('d'):  # 'd' でフレームを進める
            curpos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            new_pos = min(curpos, frames - 1)  
            cap.set(cv2.CAP_PROP_POS_FRAMES, new_pos)
            cv2.setTrackbarPos(trackbarname_frame, windowname, new_pos)
            ret, frame = cap.read()
            if ret:
                cv2.imshow(windowname, frame)
        elif key == ord('a'):  # 'a' でフレームを戻す
            curpos = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            new_pos = max(curpos - 2, 0)  
            cap.set(cv2.CAP_PROP_POS_FRAMES, new_pos)
            cv2.setTrackbarPos(trackbarname_frame, windowname, new_pos)
            ret, frame = cap.read()
            if ret:
                cv2.imshow(windowname, frame)

    cap.release()
    cv2.destroyAllWindows()

    print("動画の範囲を切り取って保存しますか？ (yes / no)")
    response = input().strip().lower()  

    if response == 'yes':
        start_frame = int(input(f"開始フレームを入力 (0 ~ {frames - 1}): "))
        end_frame = int(input(f"終了フレームを入力 (開始フレーム ~ {frames - 1}): "))

        if start_frame < 0 or end_frame >= frames or start_frame >= end_frame:
            print("不正な入力です。処理を終了します。")
        else:
            save_clipped_video(start_frame, end_frame, fps)
    elif response == 'no':
        print("処理を終了します。")
    else:
        print("無効な入力です。処理を終了します。")

def save_clipped_video(start_frame, end_frame, fps):
    cap.open(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('clipped_video.mp4', fourcc, fps, (width, height))

    print(f"フレーム {start_frame} から {end_frame} を保存します...")
    for i in range(start_frame, end_frame):
        ret, frame = cap.read()
        if not ret:
            print(f"フレーム {i} の読み取りに失敗しました。")
            break
        out.write(frame)

    out.release()
    cap.release()
    print("保存が完了しました: clipped_video.mp4")

play_video()

