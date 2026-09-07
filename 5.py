import os
import sys

print("===== File Management and Directory Navigation Utility =====")

# 1. Display current working directory
current_dir = os.getcwd()
print("\nCurrent Working Directory:")
print(current_dir)

# 2. Display directory contents
print("\nContents of Current Directory:")
for item in os.listdir():
    print(item)

# 3. Navigate to a subdirectory
directory = input("\nEnter directory name to navigate (or press Enter to skip): ")

if directory:
    if os.path.isdir(directory):
        os.chdir(directory)
        print("Successfully navigated to:", os.getcwd())
    else:
        print("Directory does not exist.")

# 4. Create workspace folder
workspace = input("\nEnter workspace folder name: ")

if not os.path.exists(workspace):
    os.makedirs(workspace)
    print("Workspace created:", workspace)
else:
    print("Workspace already exists.")

# 5. List files with a particular extension
extension = input("\nEnter file extension to search (example: .txt): ")

print("\nFiles with", extension, "extension:")

found = False

for file in os.listdir():
    if os.path.isfile(file) and file.endswith(extension):
        print(file)
        found = True

if not found:
    print("No matching files found.")

# 6. Get log file name from command-line argument
if len(sys.argv) > 1:
    log_file = sys.argv[1]
else:
    log_file = "activity.log"

# 7. Create/write log file using context manager
with open(log_file, "a") as f:
    f.write("File management utility executed.\n")
    f.write("Current directory: " + os.getcwd() + "\n")

print("\nLog file created/updated:", log_file)

# 8. Read the log file using context manager
with open(log_file, "r") as f:
    print("\n===== Log File Contents =====")
    print(f.read())

print("\nProgram completed successfully.")