RUN_SHELL = False
namespace = {}
def parse(arg):
  res = ""
  i = 0
  while i != len(arg):
    if arg[i] == '(':
      res += "shell(["
    elif arg[i] == ',':
      res += ","
    elif arg[i] == '"':
      res += "\""
    elif arg[i] == ')':
      res += "])"
    else:
      res += arg[i]
    i += 1
  return res

def shell(parenthed):
  global namespace
  command = parenthed[0]
  argv = parenthed[1:]
  
  if command == "+" and len(argv) == 1:
    return argv[0]
  elif command == "+" and len(argv) == 2:
    return str(int(argv[0])+int(argv[1]))
  elif command == "-" and len(argv) == 1:
    return str(-int(argv[0]))
  elif command == "-" and len(argv) == 2:
    return str(int(argv[0])-int(argv[1]))
  elif command == "*" and len(argv) == 1:
    return namespace[argv[0]]
  elif command == "*" and len(argv) == 2:
    return str(int(argv[0])*int(arg[0]))
  elif command == "/" and len(argv) == 2:
    return str(int(int(argv[0])/int(argv[0])))
  elif command == "%" and len(argv) == 1:
    return str(abs(int(argv[0])))
  elif command == "%" and len(argv) == 2:
    return str(int(argv[0])%int(argv[1]))
  elif command == "=" and len(argv) == 2:
    return str(int(argv[0]==argv[1]))
  elif command == "!=" and len(argv) == 2:
    return str(int(argv[0]!=argv[1]))
  elif command == ">" and len(argv) == 2:
    return str(int(int(argv[0])>int(argv[1])))
  elif command == ">=" and len(argv) == 2:
    return str(int(int(argv[0])>=int(argv[1])))
  elif command == "<" and len(argv) == 2:
    return str(int(int(argv[0])<int(argv[1])))
  elif command == "<=" and len(argv) == 2:
    return str(int(int(argv[0])<=int(argv[1])))
  elif command == "&" and len(argv) == 2:
    return str(int(argv[0])&int(argv[1]))
  elif command == "|" and len(argv) == 2:
    return str(int(argv[0])|int(argv[1]))
  elif command == "^" and len(argv) == 2:
    return str(int(argv[0])^int(argv[1]))
  elif command == "!" and len(argv) == 1:
    return str(int(not bool(int(argv[0]))))
  elif command == "~" and len(argv) == 1:
    return str(~int(argv[0]))
  elif command == "~" and len(argv) == 2:
    return argv[0]+argv[1]
  elif command == ":=" and len(argv) == 2:
    s = argv[1]
    namespace[argv[0]] = argv[1]
    return s
  elif command == "'" and len(argv) == 1:
    return chr(int(argv[0]))
  elif command == "@" and len(argv) == 1:
    return str(ord(argv[0]))
  elif command == "@" and len(argv) == 2:
    return argv[0].split("`")[int(argv[1])]
  elif command == "?" and len(argv) == 3:
    if bool(int(argv[0])):
      return argv[1]
    else:
      return argv[2]
  elif command == "if" and len(argv) == 2:
    if bool(int(argv[0])):
      return run(argv[1])
  elif command == "ifelse" and len(argv) == 3:
    if bool(int(argv[0])):
      return run(argv[1])
    else:
      return run(argv[2])
  elif command == "while" and len(argv) == 2:
    while True:
      s = run(argv[0])
      t = run(argv[1])
      if bool(int(s)):
        return t
  elif command == "do" and len(argv) == 1:
    return run(argv[0])
  elif command == "write" and len(argv) == 1:
    import sys
    sys.write(argv[0])
    return ""
  elif command == "writeln" and len(argv) == 1:
    print(argv[0])
    return ""
  elif command == " ":
    return "`".join(argv)
  elif command == "@:=" and len(argv) == 3:
    s = argv[0].split("`")
    s[int(argv[1])] = argv[2]
    return "`".join(s)
  elif command == "~~" and len(argv) == 2:
    return argv[0]+"`"+argv[1]
  elif command == "exit" and len(argv) == 0:
    import sys
    sys.exit()
  elif command == "#" and len(argv) == 1:
    return len(argv[0])
  elif command == "##" and len(argv) == 1:
    return len(argv[0].split("`"))
  elif command == "]" and len(argv) == 2:
    s = open(argv[1],"w")
    s.write(argv[0]+"\n")
    s.close()
    return argv[0]+"\n"
  elif command == "]." and len(argv) == 2:
    s = open(argv[1],"w")
    s.write(argv[0])
    s.close()
    return argv[0]
  elif command == "[" and len(argv) == 1:
    s = open(argv[0],"r")
    txt = s.read()
    s.close()
    return txt
  elif command == "]]" and len(argv) == 2:
    s = open(argv[1],"a")
    s.write(argv[0]+"\n")
    s.close()
    return argv[0]+"\n"
  elif command == "]]." and len(argv) == 2:
    s = open(argv[1],"a")
    s.write(argv[0])
    s.close()
    return argv[0]
def run(s):
  global namespace
  return eval(parse(s),{"namespace":namespace,"shell":shell,"parse":parse,"run":run})
def read_input():
  try:
    return raw_input()
  except:
    return input()
if RUN_SHELL:
  while True:
    s = read_input()
    print('"'+run(s)+'"')
