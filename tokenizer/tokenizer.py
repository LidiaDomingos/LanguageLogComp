class Token:

    def __init__(self, type: str, value: int or str):
        self.type = type
        self.value = value

class Tokenizer:

    def __init__(self, source: str):
        self.source = source
        self.position = -1
        self.next = Token
        self.token_type = ""
        self.isTheLast = False

    def selectNext(self):
        self.position = self.position + 1
        while (True):            
            if (self.position == (len(self.source))):
                self.position = self.position - 1
                self.isTheLast = True
                break
            elif (self.source[self.position] == " "):
                self.position = self.position + 1
            else:
                break

        if (self.isTheLast):
            self.token_type = "EOF"
            self.next = Token(type=self.token_type,
                              value="")

        elif (self.source[self.position] == "("):
            self.token_type = "START_PARENTHESES"
            self.next = Token(type=self.token_type,
                              value=self.source[self.position])

        elif (self.source[self.position] == ")"):
            self.token_type = "END_PARENTHESES"
            self.next = Token(type=self.token_type,
                              value=self.source[self.position])
            
        elif (self.source[self.position] == "{"):
            self.token_type = "START_CURLY_BRACKET"
            self.next = Token(type=self.token_type,
                              value=self.source[self.position])
        
        elif (self.source[self.position] == "}"):
            self.token_type = "END_CURLY_BRACKET"
            self.next = Token(type=self.token_type,
                              value=self.source[self.position])
        
        elif (self.source[self.position] == "\n"):
            self.token_type = "ENTER"
            self.next = Token(type=self.token_type,
                              value=self.source[self.position])
            
        elif (self.source[self.position] == ";"):
            self.token_type = "SEMICOLON"
            self.next = Token(type=self.token_type,
                              value=self.source[self.position])
        
        elif (self.source[self.position] == '"'):
            string = ''
            self.position = self.position + 1
            while (self.source[self.position] != '"'):
                string = string + str(self.source[self.position])
                self.position = self.position + 1
                if (self.position == (len(self.source))):
                    self.isTheLast = True
                    self.position = self.position - 1
                    break
            self.token_type = "STR"
            self.next = Token(type=self.token_type,
                              value=string)
            
        elif (self.source[self.position].isdigit()):
            self.token_type = "INT"
            number = ""
            while (self.source[self.position].isdigit()):
                number = number + self.source[self.position]
                self.position = self.position + 1
                if (self.position == (len(self.source))):
                    self.isTheLast = True
                    self.position = self.position - 1
                    break
            self.position = self.position - 1
            self.next = Token(type=self.token_type, value=int(number))

        elif (self.source[self.position].isalpha()):
            identifier = ""
            while (self.source[self.position].isalpha() or self.source[self.position].isdigit() or self.source[self.position] == "_"):
                identifier = identifier + str(self.source[self.position])
                self.position = self.position + 1
                if (self.position == (len(self.source))):
                    self.isTheLast = True
                    self.position = self.position - 1
                    break

            self.position = self.position - 1
            if (identifier == "display"):
                self.token_type = "PRINTLN"
                self.next = Token(type=self.token_type, value="Println")

            elif (identifier == "press"):
                self.token_type = "SCANLN"
                self.next = Token(type=self.token_type, value="Scanln")

            elif (identifier == "routeA"):
                self.token_type = "IF"
                self.next = Token(type=self.token_type, value="if")
            
            elif (identifier == "routeB"):
                self.token_type = "ELSE"
                self.next = Token(type=self.token_type, value="else")

            elif (identifier == "grind"):
                self.token_type = "FOR"
                self.next = Token(type=self.token_type, value="for")
            
            elif (identifier == "player"):
                self.token_type = "VAR"
                self.next = Token(type=self.token_type, value="player")

            elif (identifier == "get"):
                self.token_type = "ASSIGN"
                self.next = Token(type=self.token_type, value="=")

            elif (identifier == "buff"):
                self.token_type = "PLUS"
                self.next = Token(type=self.token_type, value="+")

            elif (identifier == "nerf"):
                self.token_type = "MINUS"
                self.next = Token(type=self.token_type, value="-")
            
            elif (identifier == "team"):
                self.token_type = "CONCAT"
                self.next = Token(type=self.token_type, value=".")

            elif (identifier == "amplify"):
                self.token_type = "TIMES"
                self.next = Token(type=self.token_type, value="*")

            elif (identifier == "split"):
                self.token_type = "DIVISION"
                self.next = Token(type=self.token_type, value="/")

            elif (identifier == "tied"):
                self.token_type = "EQUAL"
                self.next = Token(type=self.token_type, value="==")

            elif (identifier == "outclass"):
                self.token_type = "GREATER_THAN"
                self.next = Token(type=self.token_type, value=">")

            elif (identifier == "outclassed"):
                self.token_type = "LESS_THAN"
                self.next = Token(type=self.token_type, value="<")

            elif (identifier == "demolish"):
                self.token_type = "NOT"
                self.next = Token(type=self.token_type, value="!")

            elif (identifier == "or"):
                self.token_type = "OR"
                self.next = Token(type=self.token_type, value="||")

            elif (identifier == "combo"):
                self.token_type = "AND"
                self.next = Token(type=self.token_type, value="&&")

            elif (identifier == "class"):
                self.token_type = "CLASS"
                self.next = Token(type=self.token_type, value="class")
            
            elif (identifier == "int" or identifier == "string"):
                self.token_type = "TYPE"
                self.next = Token(type=self.token_type, value=identifier)
                
            else:
                self.token_type = "IDENTIFIER"
                self.next = Token(type=self.token_type, value=identifier)
        else:
            raise ValueError(
                "Contains invalid character! The possible ones are: {[0-9], buff, nerf, amplify, split, team, combo, or, demolish, grind, get, tied, class, player, (, ), {, } }")

