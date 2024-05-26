# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"9783","system":"gprdproduct"},{"code":"7740","system":"gprdproduct"},{"code":"12110","system":"gprdproduct"},{"code":"32094","system":"gprdproduct"},{"code":"20066","system":"gprdproduct"},{"code":"15127","system":"gprdproduct"},{"code":"7136","system":"gprdproduct"},{"code":"923","system":"gprdproduct"},{"code":"41556","system":"gprdproduct"},{"code":"4540","system":"gprdproduct"},{"code":"37294","system":"gprdproduct"},{"code":"45916","system":"gprdproduct"},{"code":"18733","system":"gprdproduct"},{"code":"13363","system":"gprdproduct"},{"code":"11384","system":"gprdproduct"},{"code":"21873","system":"gprdproduct"},{"code":"4034","system":"gprdproduct"},{"code":"2002","system":"gprdproduct"},{"code":"31150","system":"gprdproduct"},{"code":"3997","system":"gprdproduct"},{"code":"10902","system":"gprdproduct"},{"code":"605","system":"gprdproduct"},{"code":"6437","system":"gprdproduct"},{"code":"1297","system":"gprdproduct"},{"code":"34825","system":"gprdproduct"},{"code":"31470","system":"gprdproduct"},{"code":"32166","system":"gprdproduct"},{"code":"31708","system":"gprdproduct"},{"code":"5416","system":"gprdproduct"},{"code":"13525","system":"gprdproduct"},{"code":"3517","system":"gprdproduct"},{"code":"11133","system":"gprdproduct"},{"code":"34449","system":"gprdproduct"},{"code":"12547","system":"gprdproduct"},{"code":"581","system":"gprdproduct"},{"code":"14738","system":"gprdproduct"},{"code":"46916","system":"gprdproduct"},{"code":"19055","system":"gprdproduct"},{"code":"7961","system":"gprdproduct"},{"code":"25505","system":"gprdproduct"},{"code":"34034","system":"gprdproduct"},{"code":"22923","system":"gprdproduct"},{"code":"9223","system":"gprdproduct"},{"code":"8836","system":"gprdproduct"},{"code":"11351","system":"gprdproduct"},{"code":"26219","system":"gprdproduct"},{"code":"8897","system":"gprdproduct"},{"code":"1288","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diuretics-500mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diuretics-500mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diuretics-500mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
