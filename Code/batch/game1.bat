@echo off

rem Set up the game variables
set location=forest
set inventory=

:start

rem Display the current location and available options
echo You are in the %location%
echo What would you like to do?
echo 1. Look around
echo 2. Check inventory
echo 3. Quit

rem Get the player's choice
set /p choice=

rem Process the player's choice
if %choice%==1 (
  rem Look around
  echo You see a path leading north and a cave to the east.
) else if %choice%==2 (
  rem Check inventory
  if "%inventory%"=="" (
    echo Your inventory is empty.
  ) else (
    echo Your inventory contains: %inventory%
  )
) else if %choice%==3 (
  rem Quit the game
  goto :end
) else (
  rem Invalid choice
  echo Invalid choice. Please try again.
  goto :start
)

:end

rem End the game
echo Goodbye!