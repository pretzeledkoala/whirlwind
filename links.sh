#!/bin/bash

echo "where would you like to go? we have the following options set up for you :)"
echo "github, detexify, quiver, mathquill"

# DISPLAY OPTIONS HERE

read -p "Select an option: " choice

case "$choice" in
"github")
        open "https://github.com/"
        ;;
"detexify")
        open "https://detexify.kirelabs.org/classify.html"
        ;;
"quiver")
        open "https://q.uiver.app/"
        ;;
"mathquill")
        open "https://codepen.io/hydrosquall/full/EyOLdM/"
        ;;
*)
        echo "Invalid option"
        ;;
esac
