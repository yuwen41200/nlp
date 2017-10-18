#!/bin/bash
java -Xmx8g -cp "/usr/local/Cellar/stanford-parser/3.8.0/libexec/*:" edu.stanford.nlp.parser.lexparser.LexicalizedParser -retainTMPSubcategories -outputFormat "wordsAndTags,penn,typedDependencies" edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz corpus.txt | tee parsed.txt
gzip --best --keep --verbose corpus.txt
gzip --best --keep --verbose parsed.txt
