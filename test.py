import os
from image_filter_library.filters import ImageFilterLibrary  # 클래스 import

# 이미지 경로 입력 루프
while True:
    image_path = input("Enter the path of the image: ").strip()
    image_path = os.path.abspath(image_path)

    if not os.path.exists(image_path):
        print("File does not exist. Please try again.")
        continue

    try:
        library = ImageFilterLibrary(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        continue

    break

# 감정 기반 필터 여부 확인
while True:
    use_emotion_filter = input("Do you want to apply an emotion-based filter? (yes/no): ").lower()
    if use_emotion_filter not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue

    if use_emotion_filter == "yes":
        print("Analyzing image for dominant emotion...")
        try:
            filtered_image = library.analyze_and_apply_filter()
            filtered_image.show()
            break
        except Exception as e:
            print(f"Error during analysis: {e}")
            print("분석에 실패했습니다. 프로그램이 종료됩니다.")
            exit()
    else:
        # 필터 이름 입력 및 적용
        while True:
            print("Available filters: blur, sharpen, brighten, darken")
            filter_name = input("Enter the filter you want to apply: ").lower()
            intensity = float(input("Enter filter intensity: ").strip())
            

            if library.apply_filter(filter_name,intensity) == False:
                
                continue
            
            else :
                filtered_image = library.apply_filter(filter_name,intensity)
                filtered_image.show()
                break
        break
    
            

# 필터링된 이미지 저장 루프
while True:
    save_directory = input("Enter the directory where you want to save the filtered image: ").strip()
    file_name = input("Enter the file name for the filtered image / 확장자를 입력하지 않으면 저장되지 않을수도 있습니다.(e.g., my_image.jpg): ").strip()

    if not file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
        print("Invalid or missing extension. Adding '.jpg' as default.")
        file_name += ".jpg"

    save_path = os.path.join(save_directory, file_name)

    try:
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
            print(f"Directory created: {save_directory}")

        library.save_image(save_path, image_to_save=filtered_image)
        print(f"Image saved successfully to {save_path}")
        break
    except IOError as e:
        print(f"Error saving file: {e}. Please try again.")


