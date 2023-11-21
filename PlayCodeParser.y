%{
#include <stdio.h>  
#include <stdlib.h>
void yyerror(const char *s);
extern int yylex(void);
extern char *yytext; 
%}


%token INT_VALUE
%token IDENTIFIER
%token get player integer_token buff nerf or routeA routeB outclassed outclass tied grind combo press display start_bracket end_bracket start_parentheses end_parentheses semicolon class split amplify demolish team colon

%%

GAME: /* empty */ | ROUND colon;

PLAY: start_bracket ROUND end_bracket;

INVENTORY: PLAYER get BOOLEXPRESSION;

ROUND:  /* empty */ | DISPLAY | CHECK | GRIND | CLASSPLAYER | INVENTORY;

DISPLAY: display start_parentheses BOOLEXPRESSION end_parentheses;

CHECKAUX: routeB ROUND | /* empty */;

CHECK: routeA start_parentheses BOOLEXPRESSION end_parentheses ROUND CHECKAUX;

GRIND: grind INVENTORY semicolon BOOLEXPRESSION semicolon INVENTORY PLAY;

CLASSPLAYERAUX: get BOOLEXPRESSION | /* empty */;

CLASSPLAYER: player PLAYER class integer_token CLASSPLAYERAUX;

BOOLEXPRESSION: BOOLTERM | BOOLTERM or;

BOOLTERM: RELEXPRESSION | RELEXPRESSION combo;

RELEXPRESSIONAUX : outclassed | outclass | tied;

RELEXPRESSION: EXPRESSION | RELEXPRESSIONAUX EXPRESSION;

EXPRESSIONAUX: buff | nerf | team;

EXPRESSION: TERM | EXPRESSIONAUX TERM;

TERMARUX: amplify | split;

TERM: FACTOR | TERMARUX FACTOR;

FACTORAUX: buff | nerf | demolish;

FACTOR: INT | PLAYER | FACTORAUX FACTOR | start_parentheses BOOLEXPRESSION end_parentheses | PRESS;

PRESS: press start_parentheses end_parentheses;

INT: INT_VALUE;

PLAYER: IDENTIFIER;

%%

void yyerror(const char *s) {
    extern int yylval;   // Token value
    fprintf(stderr, "Error near token '%s': %s\n", yytext, s);
}

int main(void) {
    extern int yy_flex_debug;
    yy_flex_debug = 1;
    if (yyparse()) {
        printf("Error in parsing!\n");
        return 1;
    }
    return 0;
}