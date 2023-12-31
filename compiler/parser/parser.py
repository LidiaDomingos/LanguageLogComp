from nodes.nodes import UnOp, Assign, BinOp, Block, For, Identifier, If, IntVal, NoOp, Print, Program, Scanln, StrVal, VarDec
from prepro.prepro import PrePro
from symboltable.symboltable import SymbolTable
from tokenizer.tokenizer import Tokenizer


class Parser():

    tokenizer: Tokenizer

    @staticmethod
    def parseRLExpression():
        node = Parser().parseExpression()
        while (Parser().tokenizer.next.type == "EQUAL" or Parser().tokenizer.next.type == "GREATER_THAN" or Parser().tokenizer.next.type == "LESS_THAN"):

            if (Parser().tokenizer.next.type == "EQUAL"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseExpression()
                node = BinOp("==", [node, node2])

            if (Parser().tokenizer.next.type == "GREATER_THAN"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseExpression()
                node = BinOp(">", [node, node2])

            elif (Parser().tokenizer.next.type == "LESS_THAN"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseExpression()
                node = BinOp("<", [node, node2])
        return node
    
    @staticmethod
    def parseBoolTerm():
        node = Parser().parseRLExpression()
        while (Parser().tokenizer.next.type == "AND"):

            if (Parser().tokenizer.next.type == "AND"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseRLExpression()
                node = BinOp("&&", [node, node2])
        return node
    
    @staticmethod
    def parseBoolExpression():
        
        node = Parser().parseBoolTerm()
        while (Parser().tokenizer.next.type == "OR"):

            if (Parser().tokenizer.next.type == "OR"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseBoolTerm()
                node = BinOp("||", [node, node2])

        return node
    
    @staticmethod
    def parseInventory():

        identifier = Identifier(Parser().tokenizer.next.value)
        Parser().tokenizer.selectNext()
        if (Parser().tokenizer.next.type == "ASSIGN"):
            Parser().tokenizer.selectNext()
            
            expression = Parser().parseBoolExpression()
            statement = Assign(identifier, expression)
            
        else:
            raise SyntaxError("Check if everything is correct!")
       
        return statement
    
    @staticmethod
    def parseRound():

        node = NoOp()

        if (Parser().tokenizer.next.type == "ENTER"):
            node = NoOp()
            Parser().tokenizer.selectNext()
            return node

        if (Parser().tokenizer.next.type == "IDENTIFIER"):
            node = Parser().parseInventory()
            return node
        
        if (Parser().tokenizer.next.type == "VAR"):
            Parser().tokenizer.selectNext()
            if (Parser().tokenizer.next.type == "IDENTIFIER"):
                identifier = Identifier(Parser().tokenizer.next.value)
                Parser().tokenizer.selectNext()
                if (Parser().tokenizer.next.type == "CLASS"):
                    Parser().tokenizer.selectNext()
                    if (Parser().tokenizer.next.type == "TYPE"):
                        type = Parser().tokenizer.next.value
                        node = VarDec(type, [identifier])
                        Parser().tokenizer.selectNext()
                        if (Parser().tokenizer.next.type == "ASSIGN"):
                            Parser().tokenizer.selectNext()
                            result = Parser().parseBoolExpression()
                            node = VarDec(type, [identifier, result])
                            
                        return node
                    else:
                        raise TypeError("Must have an type (int | string) in player's class!")
                else:
                        raise TypeError("The player needs an class!")
            else:
                    raise TypeError("The player needs an name!")
        
        elif (Parser().tokenizer.next.type == "PRINTLN"):
            Parser().tokenizer.selectNext()
            if (Parser().tokenizer.next.type == "START_PARENTHESES"):
                Parser().tokenizer.selectNext()
                node = Print(Parser().parseBoolExpression())
                if (Parser().tokenizer.next.type != "END_PARENTHESES"):
                    raise SyntaxError("Must have a () after a display")
                Parser().tokenizer.selectNext()
                return node
            else:
                raise SyntaxError("Must have a () after a display")
            
        elif (Parser().tokenizer.next.type == "IF"):
            Parser().tokenizer.selectNext()

            expression = Parser().parseBoolExpression()

            if_block = Parser().parsePlay()

            if (Parser().tokenizer.next.type == "ELSE"):
                Parser().tokenizer.selectNext()
                else_block = Parser().parsePlay()
                node = If("IF", [expression, if_block, else_block])

            else:
                node = If("IF", [expression, if_block])
            return node

            
        elif (Parser().tokenizer.next.type == "FOR"):
            Parser().tokenizer.selectNext()
            if (Parser().tokenizer.next.type == "GRIND"):
                Parser().tokenizer.selectNext()
                if (Parser().tokenizer.next.type == "START_PARENTHESES"):
                    Parser().tokenizer.selectNext()
                    init = Parser().parseInventory()
                    if (Parser().tokenizer.next.type == "SEMICOLON"):
                        Parser().tokenizer.selectNext()
                        condition = Parser().parseBoolExpression()
                        if (Parser().tokenizer.next.type == "SEMICOLON"):
                            Parser().tokenizer.selectNext()
                            increment = Parser().parseInventory()
                            if (Parser().tokenizer.next.type == "END_PARENTHESES"):
                                Parser().tokenizer.selectNext()
                                block = Parser().parsePlay()
                                node = For("FOR", [init, condition, increment, block])
                                return node
                            else:
                                raise SyntaxError("The syntax to for is (example): while grinding (a get 0; a outclassed n; a get a buff 1)")
                        else:
                            raise SyntaxError("The syntax to for is (example): while grinding (a get 0; a outclassed n; a get a buff 1)")
                    else:
                        raise SyntaxError("The syntax to for is (example): while grinding (a get 0; a outclassed n; a get a buff 1)")
                else:
                    raise SyntaxError("The syntax to for is (example): while grinding (a get 0; a outclassed n; a get a buff 1)")
            else:
                raise SyntaxError("The syntax to for is (example): while grinding (a get 0; a outclassed n; a get a buff 1)")

        elif (Parser().tokenizer.next.type == "ASSIGN"):
            raise SyntaxError("To a player get atributes, must have an name before!")
        


    @staticmethod
    def parsePlay():
        node = Block()
        if (Parser().tokenizer.next.type == "START_CURLY_BRACKET"):
            Parser().tokenizer.selectNext()
            if (Parser().tokenizer.next.type == "ENTER"):
                Parser().tokenizer.selectNext()
                statement = Parser().parseRound()
                node.append_statement(statement)
                Parser().tokenizer.selectNext()

            if (Parser().tokenizer.next.type == "END_CURLY_BRACKET"):
                Parser().tokenizer.selectNext()
                return statement
            else:
                raise SyntaxError("Must have an end curly bracket (}) to a play!")

                
    @staticmethod
    def parseTerm():
        node = Parser().parseFactor()
        while (Parser().tokenizer.next.type == "TIMES" or Parser().tokenizer.next.type == "DIVISION"):

            if (Parser().tokenizer.next.type == "TIMES"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseFactor()
                node = BinOp("*", [node, node2])

            elif (Parser().tokenizer.next.type == "DIVISION"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseFactor()
                node = BinOp("/", [node, node2])

        return node

    @staticmethod
    def parseExpression():
        node = Parser().parseTerm()
        while (Parser().tokenizer.next.type == "PLUS" or Parser().tokenizer.next.type == "MINUS" or Parser().tokenizer.next.type == "CONCAT"):
            if (Parser().tokenizer.next.type == "PLUS"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseTerm()
                node = BinOp("+", [node, node2])

            elif (Parser().tokenizer.next.type == "MINUS"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseTerm()
                node = BinOp("-", [node, node2])

            elif (Parser().tokenizer.next.type == "CONCAT"):
                Parser().tokenizer.selectNext()
                node2 = Parser().parseTerm()
                node = BinOp(".", [node, node2])

        return node

    @staticmethod
    def parseFactor():        
        if (Parser().tokenizer.next.type == "INT"):
            node = IntVal(Parser().tokenizer.next.value)
            Parser().tokenizer.selectNext()
            return node
        
        elif (Parser().tokenizer.next.type == "STR"):
            node = StrVal(Parser().tokenizer.next.value)
            Parser().tokenizer.selectNext()
            return node
        
        elif (Parser().tokenizer.next.type == "IDENTIFIER"):
            node = Identifier(Parser().tokenizer.next.value)
            Parser().tokenizer.selectNext()
            return node

        elif (Parser().tokenizer.next.type == "MINUS"):
            Parser().tokenizer.selectNext()
            nodeFactor = Parser().parseFactor()
            node = UnOp("-", [nodeFactor])
        
            return node
        
        elif (Parser().tokenizer.next.type == "PLUS"):
            Parser().tokenizer.selectNext()
            nodeFactor = Parser().parseFactor()
            node = UnOp("+", [nodeFactor])

            return node
        
        elif (Parser().tokenizer.next.type == "NOT"):
            Parser().tokenizer.selectNext()
            nodeFactor = Parser().parseFactor()
            node = UnOp("!", [nodeFactor])

            return node
        
        elif (Parser().tokenizer.next.type == "START_PARENTHESES"):
            Parser().tokenizer.selectNext()
            node = Parser().parseBoolExpression()
            
            if (Parser().tokenizer.next.type != "END_PARENTHESES"):
                raise SyntaxError("It must have an end parentheses!")
            
            Parser().tokenizer.selectNext()
            
            return node
        
        elif (Parser().tokenizer.next.type == "SCANLN"):
            Parser().tokenizer.selectNext()
            if (Parser().tokenizer.next.type == "START_PARENTHESES"):
                node = Scanln("SCANLN")
                Parser().tokenizer.selectNext()

                if (Parser().tokenizer.next.type != "END_PARENTHESES"):
                    raise SyntaxError("It must have an end parentheses!")

                Parser().tokenizer.selectNext()
                return node

        else:
            raise SyntaxError("Something is wrong!")

    @staticmethod
    def game():
        node = Program()
        while(Parser().tokenizer.next.type != "EOF"):
            state = Parser().parseRound()
            if (Parser().tokenizer.next.type == "ENTER"):
                Parser().tokenizer.selectNext()
            else:
                raise SyntaxError("There is something wrong")
            node.appendProgram(state)
        Parser().tokenizer.selectNext()
        return node
    
    @classmethod
    def run(cls, source: str):
        str = PrePro().filter(source)
        symbolTable = SymbolTable()
        cls.tokenizer = Tokenizer(str)
        cls.tokenizer.selectNext()
        result = Parser().game()

        if (Parser().tokenizer.next.type == "EOF"):
            return result.Evaluate(symbolTable)
        else:
            raise SyntaxError(
                "Check if everything is correct! Did not arrive in EOF type")
