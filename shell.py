namespace = {}
def parse(arg):
  res = ""
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
  elif command == "?" and len(argv) == 3:
    if bool(int(argv[0])):
      return argv[1]
    else:
      return argv[2]
