import pandas as pd

def convert_to_ris(csv_file, ris_file):
    
    df = pd.read_csv(csv_file)
    
    with open(ris_file, 'w', encoding='utf-8') as f:
        
        for row in df.iterrows(): # Iterate over each row in the dataframe
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

csv_file = 'filename' #Rename to correct file
ris_file = 'filename' #Rename output file
convert_to_ris(csv_file, ris_file)
