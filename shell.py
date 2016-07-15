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
  
  
