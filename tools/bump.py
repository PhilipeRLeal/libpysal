"""
Update version numbers in a release branch
"""
##################################################
# Update these values before running this script #
##################################################
MAJOR = 1
MINOR = 11
MICRO = 0
year = '2016'
day = '13'
month = '1'
NEXT = '1.12.0dev'
#################################################

version = "{}.{}.{}".format(MAJOR, MINOR, MICRO)
num = {"MAJOR": MAJOR, "MINOR": MINOR, "MICRO": MICRO}

with open('../pysal/version.py') as v_file:
    lines = v_file.readlines()
    v_line = lines[1]
    d_line = lines[2]
    v_line = v_line.split()
    v_line[-1] = '"' + version + '"'
    v_line = (" ").join(v_line)+"\n"
    di = d_line.index('datetime')
    s0 = d_line[di:].strip()
    s1 = s0[:]
    s1 = s1.split()
    s1[0] = s1[0][:-5]+year+","
    s1[1] = month+","
    s1[2] = day+")"
    s1 = " ".join(s1)
    d_line = d_line.replace(s0, s1)
    lines[1] = v_line
    lines[2] = d_line

with open("../pysal/version.py", 'w') as v_file:
    v_file.write("".join(lines))

with open("../setup.py") as s_file:
    lines = s_file.readlines()
    for i, line in enumerate(lines):
        if line[:5] in num:
            v = num[line[:5]]
            line = "{} = {}\n".format(line[:5], v)
            lines[i] = line

with open("../setup.py", 'w') as s_file:
    s_file.write("".join(lines))

with open("../doc/source/conf.py") as c_file:
    lines = c_file.readlines()
    for i, line in enumerate(lines):
        tok = line[:9]
        if tok == 'version =':
            lines[i] = "version = {}".format(version)
            print lines[i]
        elif tok == 'release =':
            lines[i] = "release = {}".format(version)
            print lines[i]

with open("../doc/source/conf.py", 'w') as c_file:
    c_file.write("".join(lines))

with open("../doc/source/index.rst") as i_file:
    lines = i_file.readlines()
    for i, line in enumerate(lines):
        if line[:13] == '    - `Stable':
            a = '    - `Stable {}'.format(version)
            b = '(Released {}-{}-{})'.format(year, month, day)
            lines[i] = '{} {} <users/installation.html>`_'.format(a, b)
        if line[:13] == '    - `Develo':
            a = '    - `Development {}'.format(NEXT)
            lines[i] = '{}  <http://github.com/pysal/pysal/>`_'.format(a)

with open("../doc/source/index.rst", 'w') as i_file:
    i_file.write("".join(lines))
