def merge_dicts(d1, d2):
    # your code goes here
    d3 = d1.copy()
    temp1 = list(d1.keys())
    temp2 = list(d2.keys())
    temp3 = []

    for com_key in temp2:
        if com_key in temp1:
            temp3.append(com_key)

    for key, value in d2.items():
        if key in temp3:
            d3[key] = d1[key] + value
        else:
            d3[key] = value
    return d3

def parse_input(input_string):
    input_string = input_string.strip('{}').strip()
    parsed_dict = {}
    if input_string:
        items = input_string.split(',')
        for item in items:
            key, value = item.split(':')
            key = key.strip().strip("'").strip('"')
            value = int(value.strip())
            parsed_dict[key] = value
    return parsed_dict

if __name__ == "__main__":
    dict1_input = input()
    dict2_input = input()

    dict1 = parse_input(dict1_input)
    dict2 = parse_input(dict2_input)

    merged_dict = merge_dicts(dict1, dict2)
    print("Merged Dictionary:", merged_dict)