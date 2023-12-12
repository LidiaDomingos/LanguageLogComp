%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "playcode.tab.h"
char* yyval;
%}

%option yylineno
%option noyywrap


%%

[ \t]                       ; /* Ignora espaços em branco e tabulações */

"player"                    { yyval = strdup(yytext); return player; }

"get"                       { yyval = strdup(yytext); return get; }
"class"                     { yyval = strdup(yytext); return class; }

"buff"                      { yyval = strdup(yytext); return buff; }
"nerf"                      { yyval = strdup(yytext); return nerf; }
"amplify"                   { yyval = strdup(yytext); return amplify; }
"split"                     { yyval = strdup(yytext); return split; }

"team"                      { yyval = strdup(yytext); return team; }
"or"                        { yyval = strdup(yytext); return or; }
"combo"                     { yyval = strdup(yytext); return combo; }
"demolish"                  { yyval = strdup(yytext); return demolish; }

"tied"                      { yyval = strdup(yytext); return tied; }
"outclass"                  { yyval = strdup(yytext); return outclass; }
"outclassed"                { yyval = strdup(yytext); return outclassed; }

"grind"                     { yyval = strdup(yytext); return grind; }
"routeA"                    { yyval = strdup(yytext); return routeA; }
"routeB"                    { yyval = strdup(yytext); return routeB; }

"press"                     { yyval = strdup(yytext); return press; }
"display"                   { yyval = strdup(yytext); return display; }

"int"                       { yyval = strdup(yytext); return type; }
"string"                    { yyval = strdup(yytext); return type; }

";"                         { yyval = strdup(yytext); return semicolon; }
"("                         { yyval = strdup(yytext); return start_parentheses; }
")"                         { yyval = strdup(yytext); return end_parentheses; }
"{"                         { yyval = strdup(yytext); return start_bracket; }
"}"                         { yyval = strdup(yytext); return end_bracket; }

[0-9]+                      { yyval = strdup(yytext); return DIGIT; }
[a-zA-Z_][a-zA-Z0-9_]*      { yyval = strdup(yytext); return IDENTIFIER; }
\"([^\\\"]|\\.)*\"          { yyval = strdup(yytext); return STRING; }

\n                          { yyval = strdup(yytext); return enter; }
"//".*                      ; 
"\\\n"                      ; 

.                           { yyval = strdup(yytext); printf("%s",yyval); }
%%
