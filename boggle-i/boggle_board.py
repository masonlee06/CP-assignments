import random



class BoggleBoard:
  
  dice = [
        "AQBEGN",
        "ELRTKY",
        "AOVTQW",
        "ABYJOC",
        '',
        "EHRTVW",
        "CIMOTU",
        "DISTTY",
        "EIOSST",
        '',
        "DELRVY",
        "OUWXAP",
        "HIMNQU",
        "EEINSU",
        ',',
        "EEGHNW",
        "AFFKPS",
        "HLNNRZ",
        "QGEXSH"
    ]

  def __init__(self):
    self.board = ['_', '_', '_', '_', '\n', '_', '_', '_', '_', '\n', '_', '_', '_', '_', '\n', '_', '_', '_', '_']
  
  def __str__(self):
    return ''.join(self.board)
  


  def shake(self):
    i=0
    while i < 19:
      if self.board[i] == '_' or self.board[i].isalpha():
        self.board[i] = random.choice(BoggleBoard.dice[i])
        self.board[i] += '  '
        if self.board[i] == 'Q  ':
          self.board[i] = 'Qu '
      i+=1

# board = BoggleBoard()

# board.shake()

# print(board)
