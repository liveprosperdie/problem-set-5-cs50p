def main():
      new_str=shorten(input("Input: "))
      print(new_str)


def shorten(word):
      word1=word
      for i in word:
            if i == "a" or i== "e" or i== "i" or i=="o" or i== "u" or i =="A" or i=="E" or i=="I" or i=="O" or i=="U":
                  word1=word1.replace(i,"")
      return word1
    

if __name__=="__main__":
      main()
