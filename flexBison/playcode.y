%{
#include <stdio.h>
int yylex();
void yyerror(const char *s);
%}


%union {
    char* str_value;
    int int_value;
}

%token player
%token get
%token class

%token buff
%token nerf
%token amplify
%token split

%token team
%token or
%token combo
%token demolish

%token tied
%token outclass
%token outclassed

%token grind
%token routeA
%token routeB

%token press
%token display

%token type

%token semicolon
%token start_parentheses
%token end_parentheses
%token start_bracket
%token end_bracket

%token DIGIT
%token IDENTIFIER
%token STRING

%token enter

%start GAME

%%

GAME: ROUND enter | GAME ROUND enter;

PLAY: start_bracket enter AUXROUND end_bracket | start_bracket enter end_bracket ;

ROUND:  DISPLAY | CHECK | GRIND | CLASSPLAYER | INVENTORY;

AUXROUND: ROUND | AUXROUND ROUND;

INVENTORY: PLAYER get BOOLEXPRESSION;

DISPLAY: display start_parentheses BOOLEXPRESSION end_parentheses;

CHECKAUX: routeB PLAY | /* empty */;

CHECK: routeA start_parentheses BOOLEXPRESSION end_parentheses PLAY CHECKAUX;

GRIND: grind INVENTORY semicolon BOOLEXPRESSION semicolon INVENTORY PLAY;

CLASSPLAYERAUX: get BOOLEXPRESSION | /* empty */;

CLASSPLAYER: player PLAYER class type CLASSPLAYERAUX;

BOOLEXPRESSION: BOOLTERM | BOOLEXPRESSION or BOOLTERM;

BOOLTERM: RELEXPRESSION | BOOLTERM combo RELEXPRESSION;

RELEXPRESSIONAUX: outclassed | outclass | tied;

RELEXPRESSION: EXPRESSION | RELEXPRESSION RELEXPRESSIONAUX EXPRESSION;

EXPRESSIONAUX: buff | nerf | team;

EXPRESSION: TERM | EXPRESSION EXPRESSIONAUX TERM;

TERMARUX: amplify | split;

TERM: FACTOR | TERM TERMARUX FACTOR;

FACTORAUX: buff | nerf | demolish;

FACTOR: INT | STRING | PLAYER | FACTORAUX FACTOR | start_parentheses BOOLEXPRESSION end_parentheses | PRESS;

PRESS: press start_parentheses end_parentheses;

INT: DIGIT;

PLAYER: IDENTIFIER;

%%

void yyerror(const char *s) {
    extern int yylineno;
    extern char *yytext;

    printf("\nError in (%s): symbol \"%s\" (linha %d)\n", s, yytext, yylineno);
}

int main() {
    yyparse();
    return 0;
}