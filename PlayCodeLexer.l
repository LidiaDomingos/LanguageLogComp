%{
#include "y.tab.h"
%}

%%
"{"     { return start_bracket; }
"}"     { return end_bracket; }
"get"   { return get; }
"class"   { return class; }
"player" { return player; }
"int"   { return integer_token; }
"buff"  { return buff; }
"nerf"  { return nerf; }
"("     { return start_parentheses; }
")"     { return end_parentheses; }
";"     { return semicolon; }
"or"    { return or; }
"routeA" { return routeA; }
"routeB" { return routeB; }
"outclassed" { return outclassed; }
"outclass" { return outclass; }
"tied"   { return tied; }
"grind"  { return grind; }
"combo"  { return combo; }
"team"  { return team; }
"amplify"  { return amplify; }
"split"  { return split; }
"demolish"  { return demolish; }
"press"  { return press; }
"display" { return display; }
[0-9]+   { return INT_VALUE; }
[a-zA-Z_][a-zA-Z_0-9]* { return IDENTIFIER; }
":"  { return colon; }
\n                              { /* handle new lines */ }
[ \t\r]+                        { /* ignore extra whitespace */ }
.                               { /* handle other characters */ }

%%

