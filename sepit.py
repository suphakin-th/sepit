"""

Stack : python 3
Title : Seperate Q&A text to xlsx file
Author: BabylVoob
Date  : 2024-03-30

"""

import os
import pandas as pd

def modify_text(text):
    # Modify the text as per your requirements
    qa_pairs = text.split('\n\n')
    qa_list = []

    for pair in qa_pairs:
        # Split each pair into lines
        lines = pair.strip().split('\n')
        q, a = "", ""
        print(type(q), q, type(a), a)
        for line in lines:
            if line.startswith("Q:"):
                q = line.split(":", 1)[1].strip()
            elif line.startswith("A:"):
                a = line.split(":", 1)[1].strip()
        # Append to respective lists
        if any(q in e for e in qa_list):
            continue
        if q and a:
            qa_list.append([q, a])
    df = pd.DataFrame(qa_list, columns=['Question', 'Answer'])
    return df

def main():
    directory = os.getcwd()
    # Get a list of all files in the directory
    files = os.listdir(directory)

    # Filter out only text files
    text_files = [file for file in files if file.endswith('.txt')]
    
    if not text_files:
        print("No text files found in the directory.")
        return

    for file_name in text_files:
        try:
            # Read text from each text file
            with open(file_name, "r") as file:
                text = file.read()

            # Modify the text
            df = modify_text(text)
            print(df)
            # Export DataFrame to Excel file with the same name as the text file
            excel_file_name = os.path.splitext(file_name)[0] + "_modified.xlsx"
            excel_file_name = os.path.join('Data', excel_file_name)
            df.to_excel(excel_file_name, index=False)
            print(f"Modified text from '{file_name}' has been exported to '{excel_file_name}'.")
        except Exception as e:
            print(f"Error processing file '{file_name}': {str(e)}")

if __name__ == "__main__":
    main()
