class FileProcessorError(Exception):
    pass


class FileNotFoundErrorCustom(FileProcessorError):
    pass


class InvalidFileError(FileProcessorError):
    pass


def process_file(filename):
    try:
        if not filename.endswith(".txt"):
            raise InvalidFileError("Only .txt files are allowed.")

        try:
            file = open(filename, "r")
        except FileNotFoundError:
            raise FileNotFoundErrorCustom("File does not exist.")

        with file:
            content = file.read()

            if content.strip() == "":
                raise InvalidFileError("File is empty.")

            print("\nFile Content:")
            print(content)

    except FileProcessorError as e:
        print("Error:", e)

    else:
        print("\nFile processed successfully.")

    finally:
        print("File processing completed.")


filename = input("Enter text file name: ")
process_file(filename)