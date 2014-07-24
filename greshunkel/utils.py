import re
# Heres a joke for you:
# Q: Whats the difference between interpolate and parse_variable?
# A: Militant confusion.

def parse_variable(variable_variables):
    split = variable_variables.strip().split("xXx")[1].strip()
    kill_splitter = split.split("=", 1)
    var_name = kill_splitter[0]
    value = kill_splitter[1]
    return (var_name, value)

def interpolate(line, file_meta, context):
    to_write = line
    to_write = to_write.strip()
    regex = re.compile("xXx (?P<variable>[a-zA-Z_0-9\$]+) xXx")
    split = regex.split(to_write)
    for item in regex.findall(to_write):
        value = ""
        if "=" in item:
            # We FoUnD a LiNe tHaT hAs a vArIaBlE iN iT
            varname = item.strip().split("=")[0]
            if file_meta['vars'].get(varname):
                var = file_meta['vars'][varname]
            else:
                var = ""
        else:
            var = context.get(item, '<h1>SOMETHINGWENTWRONG</h1>')
        split = [(x if x != item else var) for x in split]
    to_write = "".join(split)

    return to_write

