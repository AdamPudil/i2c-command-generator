import json 

def load_json(filename = "data.json"):
    with open(filename, "r") as myFile:
        data = myFile.read()
    return json.loads(data)


def json_to_h(json):
    string = ''
    for command in json:
        name = command['name']
        code = command['code']
        if(code >= 255 or code <= 0):
            print(f"error: code out of range (8 bit) (0 - 255); code: {code}; name: {name}")
        else:
            string += f"#define {name} {hex(code)} \n"
    return string

def json_to_py_enum():
    pass
#todo

if __name__ == '__main__':
    data = load_json("test.json")
    h_string = json_to_h(data)
    print(h_string)
    with open("i2c_commands.h", "w") as f:
        f.write(h_string)
