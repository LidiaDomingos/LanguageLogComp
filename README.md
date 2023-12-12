# PlayCode :video_game:
---
##### *A perfect programming language for those who love gaming and feel more comfortable understanding sentences with gamer slang, having a little more fun!*
---

The **PlayCode** language is tailored for individuals passionate about gaming. It provides a coding environment where sentences are expressed using gamer jargon, creating a more intuitive experience for those familiar with gaming terminology.

---
## EBNF 

```plaintext
GAME            =    {λ | ROUND};
PLAY            =    {"{", "\n", ROUND, "}"};
INVENTORY       =    (PLAYER, "get", BOOLEXPRESSION);
ROUND           =    (λ | DISPLAY | CHECK | GRIND | CLASSPLAYER | INVENTORY);
DISPLAY         =    ("display", "(", BOOLEXPRESSION, ")");
CHECK           =    ("routeA", "(", BOOLEXPRESSION ,")", PLAY, (("routeB", PLAY) | λ ));
GRIND           =    ("while", "grinding", "(", INVENTORY, ";", BOOLEXPRESSION, ";", INVENTORY, ")", PLAY);
CLASSPLAYER     =    ("player", PLAYER, "class", "int", (λ | {"get" , BOOLEXPRESSION}));
BOOLEXPRESSION  =    (BOOLTERM | { "or", BOOLTERM});
BOOLTERM        =    (RELEXPRESSION | ("combo", RELEXPRESSION));
RELEXPRESSION   =    (EXPRESSION, {("outclassed" | "outclass" | "tied"), EXPRESSION });
EXPRESSION      =    (TERM, {("buff" | "nerf" | "team"), TERM});
TERM            =    (FACTOR, {("amplify" | "split"), FACTOR });
FACTOR          =    (INT | STRING | PLAYER | {("buff" | "nerf" | "demolish"), FACTOR} | ("(", BOOLEXPRESSION, ")") | PRESS);
PRESS           =    ("press", "(", ")");
INT             =    (DIGIT, { DIGIT });
STRING          =    ('"', {λ | LETTER | DIGIT | SPECIAL}, '"')
SPECIAL         =    ( @ | # | $ | % | & | _ | : | , | . | ? | ! | ? | - | ~ ) ;
LETTER          =    ( a | ... | z | A | ... | Z ) ;
DIGIT           =    (0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9);
PLAYER          =    (LETTER, { LETTER | DIGIT | "_" });
```

The syntax is designed to be intuitive for gamers, allowing them to express code using familiar gaming terms. The grammar includes elements like `GAME`, `PLAY`, `INVENTORY`, `ROUND`, `DISPLAY`, `CHECK`, `GRIND`, `CLASSPLAYER` and `PLAYER`, each with its own unique functionality.

---
## Examples

#### Declaring variables

```c
player x class int         
x get 1                   // x = 1
player y class string         
x get "good game!"        // x = 1
```

#### Making operations

- Simple Operations (+, -, *, /):

```c
player x class int
x get 3                            // x = 3 
player y class int
y get 2                            // y = 2

player z class int get x buff y    // z = x + y = 5
z get x nerf y                     // z = x - y = 1
z get x amplify y                  // z = x * y = 6
z get x split y                    // z = x / y = 1 
```

- Interactions with users (output/input in cmd):

```c
player luigi class string get "luigi has lost! :c"
display(luigi)

player mario class int
mario get press()
display(mario)

```

- Conditions (if/else):
```c
player mario class int get 2
player luigi class int get 3

routeA (luigi outclass mario){
    mario get 5
} routeB {
    display("luigi was outclassed by mario")
}
```

- Simple Loop (goes 1 to 10):
```c
player mario class int

while grinding(mario get 1; mario outclassed 11; mario get mario buff 1){
    display(mario)
} 
```


