# You should re-use and modify your old BoggleBoard class to support the new requirements
import random
class BoggleBoard:
        

            dice = [
            "SEPQAL",
            "CIMOTU",
            "DISTTY",
            "EIOSST",
            '',
            "AQBEGN",
            "IGBWPX",
            "AOVTQW",
            "ABYJOC",
            '',
            "DELRVY",
            "OUWXAP",
            "URENOW",
            "EEINSU",
            ',',
            "EEGHNW",
            "AFFKPS",
            "HLNNRZ",
            "YGNMQW"
            ]

            def __init__(self):
                  self.board = ['_', '_', '_', '_', '\n', '_', '_', '_', '_', '\n', '_', '_', '_', '_', '\n', '_', '_', '_', '_']
                  self.row1 = []
                  self.row2 = []
                  self.row3 = []
                  self.row4 = []
                  
      
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
                  self.row1.append(self.board[0: 4])
                  self.row2.append(self.board[5: 9])
                  self.row3.append(self.board[10: 14])
                  self.row4.append(self.board[15: 20])


            def include_word(self, word):
                  row1 = ''.join(self.row1[0]).replace(' ', '')
                  row2 = ''.join(self.row2[0]).replace(' ', '')
                  row3 = ''.join(self.row3[0]).replace(' ', '')
                  row4 = ''.join(self.row4[0]).replace(' ', '')
                  col1 = f"{row1[0]}{row2[0]}{row3[0]}{row4[0]}"
                  col2 = f"{row1[1]}{row2[1]}{row3[1]}{row4[1]}"
                  col3 = f"{row1[2]}{row2[2]}{row3[2]}{row4[2]}"
                  col4 = f"{row1[3]}{row2[3]}{row3[3]}{row4[3]}"
                  diag1 = f"{row1[0]}{row2[1]}{row3[2]}{row4[3]}"
                  diag2 = f"{row4[0]}{row3[1]}{row2[2]}{row1[3]}"
                  all_words = [row1, row2, row3, row4, col1, col2, col3, col4, diag1, diag2]
                  user_word = word.upper()
                  rev_word = user_word[::-1]
                  for item in all_words:
                        if user_word == item or rev_word == item:
                                return True
                  else:
                        return False
                 


# board = BoggleBoard()

# board.shake()
# print(board)
# print(board.row1)
# print(board.include_word('aaaa'))


