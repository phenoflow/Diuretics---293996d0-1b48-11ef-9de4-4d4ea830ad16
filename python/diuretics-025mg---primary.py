# David A Springate, Darren M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, 2024.

import sys, csv, re

codes = [{"code":"23134","system":"gprdproduct"},{"code":"40886","system":"gprdproduct"},{"code":"15135","system":"gprdproduct"},{"code":"13526","system":"gprdproduct"},{"code":"12054","system":"gprdproduct"},{"code":"23456","system":"gprdproduct"},{"code":"24190","system":"gprdproduct"},{"code":"58","system":"gprdproduct"},{"code":"34899","system":"gprdproduct"},{"code":"8602","system":"gprdproduct"},{"code":"19890","system":"gprdproduct"},{"code":"34124","system":"gprdproduct"},{"code":"39021","system":"gprdproduct"},{"code":"2612","system":"gprdproduct"},{"code":"21867","system":"gprdproduct"},{"code":"18973","system":"gprdproduct"},{"code":"23427","system":"gprdproduct"},{"code":"27946","system":"gprdproduct"},{"code":"1124","system":"gprdproduct"},{"code":"31820","system":"gprdproduct"},{"code":"3701","system":"gprdproduct"},{"code":"8673","system":"gprdproduct"},{"code":"43516","system":"gprdproduct"},{"code":"31670","system":"gprdproduct"},{"code":"34012","system":"gprdproduct"},{"code":"41572","system":"gprdproduct"},{"code":"46952","system":"gprdproduct"},{"code":"542","system":"gprdproduct"},{"code":"21423","system":"gprdproduct"},{"code":"1788","system":"gprdproduct"},{"code":"18287","system":"gprdproduct"},{"code":"24189","system":"gprdproduct"},{"code":"8521","system":"gprdproduct"},{"code":"33659","system":"gprdproduct"},{"code":"22912","system":"gprdproduct"},{"code":"2","system":"gprdproduct"},{"code":"38459","system":"gprdproduct"},{"code":"15457","system":"gprdproduct"},{"code":"12651","system":"gprdproduct"},{"code":"23131","system":"gprdproduct"},{"code":"33651","system":"gprdproduct"},{"code":"9178","system":"gprdproduct"},{"code":"21803","system":"gprdproduct"},{"code":"34367","system":"gprdproduct"},{"code":"924","system":"gprdproduct"},{"code":"46792","system":"gprdproduct"},{"code":"5727","system":"gprdproduct"},{"code":"20057","system":"gprdproduct"},{"code":"27520","system":"gprdproduct"},{"code":"21182","system":"gprdproduct"},{"code":"27689","system":"gprdproduct"},{"code":"4332","system":"gprdproduct"},{"code":"16786","system":"gprdproduct"},{"code":"41517","system":"gprdproduct"},{"code":"26256","system":"gprdproduct"},{"code":"46355","system":"gprdproduct"},{"code":"46687","system":"gprdproduct"},{"code":"40149","system":"gprdproduct"},{"code":"35196","system":"gprdproduct"},{"code":"34059","system":"gprdproduct"},{"code":"25382","system":"gprdproduct"},{"code":"33083","system":"gprdproduct"},{"code":"20093","system":"gprdproduct"},{"code":"14283","system":"gprdproduct"},{"code":"12517","system":"gprdproduct"},{"code":"11641","system":"gprdproduct"},{"code":"24632","system":"gprdproduct"},{"code":"35481","system":"gprdproduct"},{"code":"27256","system":"gprdproduct"},{"code":"18903","system":"gprdproduct"},{"code":"7351","system":"gprdproduct"},{"code":"8987","system":"gprdproduct"},{"code":"34803","system":"gprdproduct"},{"code":"19142","system":"gprdproduct"},{"code":"5721","system":"gprdproduct"},{"code":"47467","system":"gprdproduct"},{"code":"34602","system":"gprdproduct"},{"code":"26275","system":"gprdproduct"},{"code":"38889","system":"gprdproduct"},{"code":"11338","system":"gprdproduct"},{"code":"10323","system":"gprdproduct"},{"code":"27957","system":"gprdproduct"},{"code":"17143","system":"gprdproduct"},{"code":"29529","system":"gprdproduct"},{"code":"13871","system":"gprdproduct"},{"code":"29991","system":"gprdproduct"},{"code":"42906","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('diuretics-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["diuretics-025mg---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["diuretics-025mg---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["diuretics-025mg---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
