# Example 3: Filter out files with a specific extension

filenames = ["document.txt", "image.jpg", "code.py", "data.csv", "script.sh"]
target_extension = ".txt"
text_files = list(filter(lambda x: x.endswith(target_extension), filenames))
print(text_files)
