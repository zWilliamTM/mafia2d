

if __name__ == '__main__':
  stack = []
  stack.append({
    0: lambda : list(),
    1: 'Mundo'
  }[0]())

  print(stack.pop())

  pass
