import pandas as pd

def convert_to_ris(csv_file, ris_file):
    # Read CSV file into pandas DataFrame
    df = pd.read_csv(csv_file)

    # Open RIS file for writing
    with open(ris_file, 'w', encoding='utf-8') as f:
        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():
            # Write RIS tags to the file. Make sure the CSV uses the same column names as this function
            f.write('TY  - JOUR\n')
            f.write('TI  - ' + str(row['Item Title']) + '\n')
            f.write('AU  - ' + str(row['Authors']) + '\n')
            f.write('PY  - ' + str(row['Publication Year']) + '\n')
            f.write('JO  - ' + str(row['Publication Title']) + '\n')
            f.write('VL  - ' + str(row['Journal Volume']) + '\n')
            f.write('IS  - ' + str(row['Journal Issue']) + '\n')
            f.write('DO  - ' + str(row['Item DOI']) + '\n')
            f.write('UR  - ' + str(row['URL']) + '\n')
            f.write('ER  - \n\n')

    print("Conversion completed. RIS file saved as", ris_file)

csv_file = 'Springer_Engineering.csv' #Rename to correct file
ris_file = 'Springer_ENG.ris' #Rename output file
convert_to_ris(csv_file, ris_file)
