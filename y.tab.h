/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_YY_Y_TAB_H_INCLUDED
# define YY_YY_Y_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    INT_VALUE = 258,               /* INT_VALUE  */
    IDENTIFIER = 259,              /* IDENTIFIER  */
    get = 260,                     /* get  */
    player = 261,                  /* player  */
    integer_token = 262,           /* integer_token  */
    buff = 263,                    /* buff  */
    nerf = 264,                    /* nerf  */
    or = 265,                      /* or  */
    routeA = 266,                  /* routeA  */
    routeB = 267,                  /* routeB  */
    outclassed = 268,              /* outclassed  */
    outclass = 269,                /* outclass  */
    tied = 270,                    /* tied  */
    grind = 271,                   /* grind  */
    combo = 272,                   /* combo  */
    press = 273,                   /* press  */
    display = 274,                 /* display  */
    start_bracket = 275,           /* start_bracket  */
    end_bracket = 276,             /* end_bracket  */
    start_parentheses = 277,       /* start_parentheses  */
    end_parentheses = 278,         /* end_parentheses  */
    semicolon = 279,               /* semicolon  */
    class = 280,                   /* class  */
    split = 281,                   /* split  */
    amplify = 282,                 /* amplify  */
    demolish = 283,                /* demolish  */
    team = 284,                    /* team  */
    colon = 285                    /* colon  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif
/* Token kinds.  */
#define YYEMPTY -2
#define YYEOF 0
#define YYerror 256
#define YYUNDEF 257
#define INT_VALUE 258
#define IDENTIFIER 259
#define get 260
#define player 261
#define integer_token 262
#define buff 263
#define nerf 264
#define or 265
#define routeA 266
#define routeB 267
#define outclassed 268
#define outclass 269
#define tied 270
#define grind 271
#define combo 272
#define press 273
#define display 274
#define start_bracket 275
#define end_bracket 276
#define start_parentheses 277
#define end_parentheses 278
#define semicolon 279
#define class 280
#define split 281
#define amplify 282
#define demolish 283
#define team 284
#define colon 285

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;


int yyparse (void);


#endif /* !YY_YY_Y_TAB_H_INCLUDED  */
