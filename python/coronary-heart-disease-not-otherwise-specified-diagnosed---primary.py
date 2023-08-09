# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"10260","system":"med"},{"code":"11648","system":"med"},{"code":"1344","system":"med"},{"code":"15754","system":"med"},{"code":"1676","system":"med"},{"code":"1792","system":"med"},{"code":"18135","system":"med"},{"code":"18889","system":"med"},{"code":"20416","system":"med"},{"code":"21844","system":"med"},{"code":"22383","system":"med"},{"code":"23078","system":"med"},{"code":"240","system":"med"},{"code":"24783","system":"med"},{"code":"27951","system":"med"},{"code":"27977","system":"med"},{"code":"28138","system":"med"},{"code":"29421","system":"med"},{"code":"34633","system":"med"},{"code":"35713","system":"med"},{"code":"39693","system":"med"},{"code":"47637","system":"med"},{"code":"52517","system":"med"},{"code":"5413","system":"med"},{"code":"55137","system":"med"},{"code":"61072","system":"med"},{"code":"68401","system":"med"},{"code":"7320","system":"med"},{"code":"9413","system":"med"},{"code":"95550","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('coronary-heart-disease-not-otherwise-specified-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["coronary-heart-disease-not-otherwise-specified-diagnosed---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["coronary-heart-disease-not-otherwise-specified-diagnosed---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["coronary-heart-disease-not-otherwise-specified-diagnosed---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
