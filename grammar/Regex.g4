grammar Regex;

regex: alternation EOF;
alternation: concatenation ('|' concatenation)*;
concatenation: repetition+;
repetition: primary ('*' | '+' | '?')?;
primary: group | symbol;
group: '(' alternation ')';
symbol: CHAR;

CHAR: [ab];
STAR: '*';
PLUS: '+';
QUESTION: '?';
PIPE: '|';
WS: [ \t\r\n]+ -> skip;
