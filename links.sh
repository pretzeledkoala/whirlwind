#!/bin/bash

echo "where would you like to go? we have the following options set up for you :)"
echo "arxiv, detexify, functionswiki, latexocr, mathoverflow, mathquill, mathscinet, mathstackexchange, ncatlab, quiver, snippetmaker, tesseract"

# DISPLAY OPTIONS HERE

read -p "Select an option: " choice

case "$choice" in
"arxiv")
        open "https://arxiv.org/"
        ;;
"detexify")
        open "https://detexify.kirelabs.org/classify.html"
        ;;
"functionswiki")
        open "https://dlmf.nist.gov/"
        ;;
"latexocr")
        open "https://github.com/lukas-blecher/LaTeX-OCR"
        ;;
"mathoverflow")
        open "https://mathoverflow.net/"
        ;;
"mathquill")
        open "https://codepen.io/hydrosquall/full/EyOLdM/"
        ;;
"mathscinet")
        open "https://mathscinet.ams.org/mathscinet/publications-search"
        ;;
"mathstackexchange")
        open "https://math.stackexchange.com/"
        ;;
"ncatlab")
        open "https://ncatlab.org/nlab/show/HomePage"
        ;;
"quiver")
        open "https://q.uiver.app/"
        ;;
"snippetmaker")
        open "https://snippet-generator.app/?description=&tabtrigger=&snippet=&mode=vscode"
        ;;
"tesseract")
        open "https://lukas-blecher.github.io/LaTeX-OCR/"
        ;;
*)
        echo "Invalid option"
        ;;
esac
