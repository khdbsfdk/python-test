import os
import shutil
from pathlib import Path

# 다운로드 폴더 경로
download_folder = r'C:\Users\PC\Downloads\files'

# 대상 폴더 경로
images_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
archive_folder = os.path.join(download_folder, 'Archive')
docs_folder = os.path.join(download_folder, 'docs')

# 대상 확장자 목록
image_extensions = ['.jpg', '.png']
data_extensions = ['.csv', '.xlsx', '.txt']
zip_extension = '.zip'
pdf_extension = '.pdf'

# 폴더가 없으면 생성
for folder in [images_folder, data_folder, archive_folder, docs_folder]:
    Path(folder).mkdir(parents=True, exist_ok=True)

# 파일 이동
for file_name in os.listdir(download_folder):
    file_path = os.path.join(download_folder, file_name)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(file_name)[1].lower()

        if file_extension in image_extensions:
            shutil.move(file_path, os.path.join(images_folder, file_name))
            print(f"이미지 파일 이동: {file_name}")

        elif file_extension in data_extensions:
            shutil.move(file_path, os.path.join(data_folder, file_name))
            print(f"데이터 파일 이동: {file_name}")

        elif file_extension == zip_extension:
            shutil.move(file_path, os.path.join(archive_folder, file_name))
            print(f"ZIP 파일 이동: {file_name}")

        elif file_extension == pdf_extension:
            shutil.move(file_path, os.path.join(docs_folder, file_name))
            print(f"PDF 파일 이동: {file_name}")

print("파일 이동이 완료되었습니다.")
