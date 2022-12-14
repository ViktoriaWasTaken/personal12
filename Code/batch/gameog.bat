@echo off
title game 1
color 0c
:main
echo Tell me your name
set /p input=what is your name?
echo welcome %input%
cls
echo you hear a chute open you fall and hit the ground everything goes dark....
echo ...
echo ...
echo ...
echo open your eyes?
echo 1. yes
echo 2. no
set /p input=
cls
if %input% == 1 set start=you find yourself in a dark room with no defining feature besides 2 doors
pause
 
echo %start%
echo choose a door
echo 1. wood
echo 2. stone
set /p input=
cls
if %input% == 1 set choice1=you enter the wooden door and before you lays a dark misty woodland path you hear a faint howl
if %input% == 2 set choice2=you enter the stone door and bofore you lays a dark damp cave it smells of mold
pause
 
echo %choice1%
echo 1. press onward
echo 2. return
set /p input=
cls
if %input% == 1 set choice1-1= you follow the woodland path and find a clearing you feel as though your being watched
if %input% == 2 set choiceR= you return to the dark room its just a boring as you remember
pause
 
echo %choice2%
echo 1. press onward
echo 2. return
set /p input=
cls
if %input% == 1 set choice2-1= you make your treak through the cave and find yourself before a large opening with no visable features there is a single rope that decends into the darkess
if %input% == 2 set choiceR= you return to the dark room its just a boring as you remember
pause
 
echo %choice2-1%
echo 1. descend
echo 2. return
set /p input=
cls
if %input% == 1 set Choice1-2
if %input% == 2 set choiceR= you return to the dark room its just a boring as you remember
pause
 
echo %choice1-1%
cls
if %input% == return set choiceR= you return to the dark room its just a boring as you remember
pause
 
echo %choiceR%
echo choose a door
echo 1. wood
echo 2. stone
set /p input=
cls
if %input% == 1 set choice1=you enter the wooden door and before you lays a dark misty woodland path you hear a faint howl
if %input% == 2 set choice2=you enter the stone door and before you lays a dark damp cave it smells of mold
pause
