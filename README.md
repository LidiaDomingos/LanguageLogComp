# PlayCode :video_game:
---
##### *A perfect programming language for those who love gaming and feel more comfortable understanding sentences with gamer slang, having a little more fun!*
---

The **PlayCode** language is tailored for individuals passionate about gaming. It provides a coding environment where sentences are expressed using gamer jargon, creating a more intuitive experience for those familiar with gaming terminology.

---
## EBNF 

```plaintext
GAME            =    (λ | ROUND);
PLAY            =    ("{", ROUND, "}");
INVENTORY       =    (PLAYER, "get", BOOLEXPRESSION);
ROUND           =    ((λ | DISPLAY | CHECK | GRIND | CLASSPLAYER | INVENTORY), ":");
DISPLAY         =    ("display", "(", BOOLEXPRESSION, ")");
CHECK           =    ("routeA", "(", BOOLEXPRESSION ,")", ROUND, (("routeB", ROUND) | λ ));
GRIND           =    ("grind", INVENTORY, ";", BOOLEXPRESSION ,";", INVENTORY, PLAY);
CLASSPLAYER     =    ("player", PLAYER, "class", ("str" | "int"), (λ | {"get" , BOOLEXPRESSION}));
BOOLEXPRESSION  =    (BOOLTERM | {BOOLTERM, "or"});
BOOLTERM        =    (RELEXPRESSION | (RELEXPRESSION, "combo"));
RELEXPRESSION   =    (EXPRESSION, {("outclassed" | "outclass" | "tied"), EXPRESSION });
EXPRESSION      =    (TERM, {("buff" | "nerf" | "team"), TERM});
TERM            =    (FACTOR, {("amplify" | "split"), FACTOR });
FACTOR          =    (INT | STRING | PLAYER | {("buff" | "nerf" | "demolish"), FACTOR} | ("(", BOOLEXPRESSION, ")") | PRESS);
PRESS           =    ("press", "(", ")");
INT             =    (DIGIT, { DIGIT });
STRING          =    (""", (LETTER | DIGIT), """);
LETTER          =    ( a | ... | z | A | ... | Z ) ;
DIGIT           =    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);
PLAYER          =    (LETTER, { LETTER | DIGIT | "_" });
```

The syntax is designed to be intuitive for gamers, allowing them to express code using familiar gaming terms. The grammar includes elements like `GAME`, `PLAY`, `INVENTORY`, `ROUND`, `DISPLAY`, `CHECK`, `GRIND`, `CLASSPLAYER`, `BOOLEXPRESSION`, `BOOLTERM`, `RELEXPRESSION`, `EXPRESSION`, `TERM`, `FACTOR`, `PRESS`, `INT`, `STRING`, `LETTER`, `DIGIT`, and `PLAYER`, each with its own unique functionality.

---
## Examples

#### Declaring variables

```plaintext
player x class int:         
x get 1:                   # x = 1
player y class str:
y get "Hello World":       # y = 1
```

#### Making operations

```plaintext
player x class int:
x get 3:                            # x = 3 
player y class int:
y get 2:                            # y = 2

player z class int get x buff y:    # z = x + y = 5
z get x nerf y:                     # z = x - y = 1
z get x amplify y:                  # z = x * y = 6
z get x split y:                    # z = x / y = 1 
```