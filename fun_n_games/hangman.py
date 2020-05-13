import requests
import random
from os import system, name

class Hangman:
        
    def __init__(self):
        self.blanks = ""
        self.parts = {
            1:" 0",
            2:" |",
            3:"/|",
            4:"/|\\",
            5:"/",
            6:"/ \\"}
        
        self.part_order = ((1,0,0),(1,2.0),(1,3,0),(1,4,0),(1,4,5),(1,4,6))
        self.max_guess = len(self.parts)
        self.wrong_answers = 0
        self.correct = 0
        self.guessed = ""
        
        url ='https://random-word-api.herokuapp.com/word?number=1'
        resp = requests.get(url)
        if resp.status_code != 200:
            #Something wrong
            error = f"GET " + url + "{}".format(resp.status_code)
            raise Exception(error) 

        self.word = resp.json()[0]  
        
        self.blanks = "".ljust(len(self.word),"_")
     
    def print_spacer(self,bars): 
        x = 0;
        while x < bars:
            x += 1
            print("| ")
            
    def draw_part(self,part):
        trow = self.parts[part]
        tstr ="|    "
        for t in trow:
            tstr += t       
        print(tstr)
                    
        
    def draw_body(self):
        print("------")
        print("|     |")
 
        if self.wrong_answers == 0:
            self.print_spacer(3) 
            return;
        else:
            parts = self.part_order[self.wrong_answers -1]
            for bpart in parts:
                if bpart == 0:
                    self.print_spacer(1)
                else:
                    self.draw_part(bpart)
            

    def guess(self,letter):
        counter = -1
        tempblanks = ""
        found = False
        if letter == "hint":
            for x in range(0,len(self.blanks)):
                if self.blanks[x] == "_":
                    letter = self.word[x]
                    break
            
        if len(letter) > 1:
            raise Exception("Only single letter allowed")
        
        if letter in self.blanks:
            return True #already guessed
        
        for c in self.word:
            counter += 1
            if c == letter:
                tempblanks += c
                self.correct += 1
                found = True
            elif self.blanks[counter] != "_":
                tempblanks +=  self.blanks[counter]
            else:
                tempblanks += "_"                      
        self.blanks = tempblanks 
        return found  
          
    def print_blanks(self):
        pblanks = ""
        for c in self.blanks:
            pblanks += f"{c} "
        print(pblanks)
       

    def start_game(self):
        while self.wrong_answers <= self.max_guess:
            #print(self.word)
            self.draw_body()
            self.print_blanks()
            if len(self.guessed) > 0:
                print(f"Wrong Guesses:{self.guessed}")
            
            if self.correct == len(self.word):
                print("stay of execution")
                return;
                
            if self.wrong_answers == self.max_guess:
                print(f"executed\nThe Word was {self.word}")
                return 
            
            answer = input("Guess a Letter:")
                
            result = self.guess(answer)
            if not result:
                self.wrong_answers += 1
                if answer not in self.guessed:
                    self.guessed += answer
                
                
def main():
    hanger = Hangman()
    hanger.start_game()
      
if __name__ == "__main__":
    main()
                
