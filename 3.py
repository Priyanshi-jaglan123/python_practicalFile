import pandas as pd
import os

def csv_inspector():
    print("===== Automated CSV File Inspector =====")

    # Take file name from user
    filename = input("Enter CSV/TSV file path: ")

    # Check whether file exists
    if not os.path.exists(filename):
        print("File not found!")
        return

    try:
        # Detect file type
        if filename.endswith(".tsv"):
            df = pd.read_csv(filename, sep="\t")
        else:
            df = pd.read_csv(filename)

        print("\n===== File Information =====")

        # Display number of rows and columns
        rows, columns = df.shape
        print("Number of Rows    :", rows)
        print("Number of Columns :", columns)

        # Display column names
        print("\nColumn Names:")
        print(list(df.columns))

        # Display data types
        print("\nData Types:")
        print(df.dtypes)

        # Display first 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Check missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Summary statistics
        print("\n===== Summary Statistics =====")
        print(df.describe())

        # Select numerical columns
        numeric_columns = df.select_dtypes(include="number").columns

        if len(numeric_columns) > 0:
            print("\nNumerical Columns:")
            print(list(numeric_columns))

            print("\nAverage Values:")
            print(df[numeric_columns].mean())

        # Ask user whether to filter data
        choice = input("\nDo you want to filter data? (yes/no): ")

        if choice.lower() == "yes":
            column = input("Enter column name: ")

            if column in df.columns:
                value = input("Enter value to filter: ")

                filtered_df = df[df[column].astype(str) == value]

                print("\n===== Filtered Data =====")
                print(filtered_df)

                # Export filtered data
                output_file = input(
                    "Enter output file name (example: filtered.csv): "
                )

                filtered_df.to_csv(output_file, index=False)

                print("Filtered data exported successfully!")

            else:
                print("Column not found!")

        # Export complete data
        export = input("\nDo you want to export the complete data? (yes/no): ")

        if export.lower() == "yes":
            output_file = input("Enter output file name: ")

            df.to_csv(output_file, index=False)

            print("Data exported successfully to:", output_file)

    except Exception as e:
        print("Error:", e)


# Run the program
csv_inspector()
