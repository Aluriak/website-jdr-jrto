#!/usr/bin/zsh
while true ; do vim -p src/start.twee ; tweego src -o explo.html ; firefox explo.html ; echo "<press enter to edit>" ; read ; done
