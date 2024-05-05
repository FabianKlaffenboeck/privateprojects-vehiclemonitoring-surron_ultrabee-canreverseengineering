def read_asc_files(filenames):
    data_points_asc = []

    for fileName in filenames:
        with open(fileName) as f:
            content = f.readlines()
            for line in content:
                data_points_asc.append({
                    "lineId": len(data_points_asc),
                    "Id": line[15:25].strip(),
                    "dlc": line[38:39],
                    "msg": line[40:64],
                    "time": line[:12],
                })

    return add_line_notation(clean_up_data_points(data_points_asc))


def clean_up_data_points(data_points_asc):
    tmp_cleaned = []

    for e in data_points_asc:

        noWeirdChar = not (':' in e['Id']) | (':' in e['dlc']) | ('.' in e['dlc'])
        stringNotEmpty = (e["Id"] != '') & (e["Id"] != ' ') & (e["dlc"] != '') & (e["dlc"] != ' ')

        if stringNotEmpty & noWeirdChar:
            tmp_cleaned.append(e)

    return tmp_cleaned


def add_line_notation(data_points_asc):
    for pos in range(len(data_points_asc)):
        data_points_asc[pos]["lineId"] = pos

    return data_points_asc
