# Automated Reports
## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
cli/__init__.py             0      0   100%
core/__init__.py            0      0   100%
core/board.py             111     34    69%   29, 36, 42, 48, 51, 53, 87, 94, 98, 103-109, 113-130, 134-144, 154, 189
core/checker.py             9      0   100%
core/dice.py               17      0   100%
core/game.py               45      8    82%   46-48, 83, 88-93
core/player.py             23      0   100%
pygame_ui/__init__.py       0      0   100%
tests/__init__.py           0      0   100%
tests/test_board.py       166      1    99%   236
tests/test_checker.py      13      1    92%   17
tests/test_cli.py          31      1    97%   44
tests/test_dice.py         48      1    98%   61
tests/test_game.py         73      1    99%   112
tests/test_player.py       44      2    95%   43, 54
-----------------------------------------------------
TOTAL                     580     49    92%

```
## Pylint Report
```text
************* Module core.checker
core/checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/checker.py:1:0: R0903: Too few public methods (1/2) (too-few-public-methods)
************* Module core.game
core/game.py:87:0: C0303: Trailing whitespace (trailing-whitespace)
core/game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.board
core/board.py:55:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:174:0: C0303: Trailing whitespace (trailing-whitespace)
core/board.py:196:0: C0304: Final newline missing (missing-final-newline)
core/board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
core/board.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:15:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:27:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
core/board.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:102:8: R1705: Unnecessary "elif" after "return", remove the leading "el" from "elif" (no-else-return)
core/board.py:78:4: R0911: Too many return statements (8/6) (too-many-return-statements)
core/board.py:78:4: R0912: Too many branches (15/12) (too-many-branches)
core/board.py:150:4: C0116: Missing function or method docstring (missing-function-docstring)
core/board.py:151:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
************* Module core.player
core/player.py:14:0: C0303: Trailing whitespace (trailing-whitespace)
core/player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module core.dice
core/dice.py:20:0: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:35:36: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:36:31: C0303: Trailing whitespace (trailing-whitespace)
core/dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
************* Module pygame_ui.game_window
pygame_ui/game_window.py:87:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:93:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:102:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:108:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:120:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:129:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:138:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:142:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:146:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:150:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:153:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:155:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:160:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:164:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:171:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:178:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:180:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:185:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:189:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:193:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:201:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:212:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:217:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:222:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:228:0: C0303: Trailing whitespace (trailing-whitespace)
pygame_ui/game_window.py:357:0: C0304: Final newline missing (missing-final-newline)
pygame_ui/game_window.py:1:0: C0114: Missing module docstring (missing-module-docstring)
pygame_ui/game_window.py:2:0: C0410: Multiple imports on one line (sys, os) (multiple-imports)
pygame_ui/game_window.py:6:0: C0413: Import "from core.board import Board" should be placed at the top of the module (wrong-import-position)
pygame_ui/game_window.py:7:0: C0413: Import "from core.dice import Dice" should be placed at the top of the module (wrong-import-position)
pygame_ui/game_window.py:8:0: C0413: Import "from core.player import Player" should be placed at the top of the module (wrong-import-position)
pygame_ui/game_window.py:9:0: C0413: Import "from core.game import BackgammonGame" should be placed at the top of the module (wrong-import-position)
pygame_ui/game_window.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:13:4: W0621: Redefining name 'n1' from outer scope (line 352) (redefined-outer-name)
pygame_ui/game_window.py:14:4: W0621: Redefining name 'n2' from outer scope (line 352) (redefined-outer-name)
pygame_ui/game_window.py:18:0: C0115: Missing class docstring (missing-class-docstring)
pygame_ui/game_window.py:35:8: C0103: Attribute name "WOOD" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:36:8: C0103: Attribute name "WHITE" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:37:8: C0103: Attribute name "BLACK" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:38:8: C0103: Attribute name "RED" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:39:8: C0103: Attribute name "BLUE" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:40:8: C0103: Attribute name "GREY" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:41:8: C0103: Attribute name "DARK" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:42:8: C0103: Attribute name "GOLD" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:43:8: C0103: Attribute name "FONT" doesn't conform to snake_case naming style (invalid-name)
pygame_ui/game_window.py:18:0: R0902: Too many instance attributes (21/7) (too-many-instance-attributes)
pygame_ui/game_window.py:19:37: W0621: Redefining name 'screen' from outer scope (line 354) (redefined-outer-name)
pygame_ui/game_window.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:99:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:116:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:116:4: R0914: Too many local variables (38/15) (too-many-locals)
pygame_ui/game_window.py:116:4: R0915: Too many statements (74/50) (too-many-statements)
pygame_ui/game_window.py:230:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:240:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
pygame_ui/game_window.py:247:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:252:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:261:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:261:4: R0912: Too many branches (17/12) (too-many-branches)
pygame_ui/game_window.py:261:4: R0915: Too many statements (51/50) (too-many-statements)
pygame_ui/game_window.py:329:4: C0116: Missing function or method docstring (missing-function-docstring)
pygame_ui/game_window.py:334:33: E1101: Module 'pygame' has no 'QUIT' member (no-member)
pygame_ui/game_window.py:336:20: E1101: Module 'pygame' has no 'quit' member (no-member)
pygame_ui/game_window.py:338:33: E1101: Module 'pygame' has no 'KEYDOWN' member (no-member)
pygame_ui/game_window.py:338:65: E1101: Module 'pygame' has no 'K_SPACE' member (no-member)
pygame_ui/game_window.py:341:33: E1101: Module 'pygame' has no 'MOUSEBUTTONDOWN' member (no-member)
pygame_ui/game_window.py:353:4: E1101: Module 'pygame' has no 'init' member (no-member)
pygame_ui/game_window.py:2:0: C0411: standard import "sys" should be placed before third party import "pygame" (wrong-import-order)
pygame_ui/game_window.py:2:0: C0411: standard import "os" should be placed before third party import "pygame" (wrong-import-order)
************* Module cli.CLI
cli/CLI.py:1:0: C0114: Missing module docstring (missing-module-docstring)
cli/CLI.py:1:0: C0103: Module name "CLI" doesn't conform to snake_case naming style (invalid-name)
cli/CLI.py:1:0: C0410: Multiple imports on one line (sys, os) (multiple-imports)
cli/CLI.py:4:0: C0413: Import "from core.board import Board" should be placed at the top of the module (wrong-import-position)
cli/CLI.py:5:0: C0413: Import "from core.dice import Dice" should be placed at the top of the module (wrong-import-position)
cli/CLI.py:6:0: C0413: Import "from core.player import Player" should be placed at the top of the module (wrong-import-position)
cli/CLI.py:7:0: C0413: Import "from core.game import BackgammonGame" should be placed at the top of the module (wrong-import-position)
cli/CLI.py:21:21: W0613: Unused argument 'color' (unused-argument)
cli/CLI.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
cli/CLI.py:36:0: R0914: Too many local variables (17/15) (too-many-locals)
cli/CLI.py:45:4: W0612: Unused variable 'game' (unused-variable)
************* Module tests.test_cli
tests/test_cli.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_cli.py:7:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_cli.py:5:0: W0611: Unused import cli (unused-import)
************* Module tests.test_checker
tests/test_checker.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_checker.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_checker.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_checker.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_player
tests/test_player.py:38:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_player.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_player.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_player.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:12:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:30:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:34:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:39:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_player.py:47:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_game
tests/test_game.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_game.py:8:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_game.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_game.py:25:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_game.py:40:8: W0612: Unused variable 'roll' (unused-variable)
tests/test_game.py:58:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_game.py:72:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_game.py:74:8: W0612: Unused variable 'roll1' (unused-variable)
tests/test_game.py:75:8: W0612: Unused variable 'roll2' (unused-variable)
tests/test_game.py:93:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_dice
tests/test_dice.py:38:38: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:43:36: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:44:0: C0303: Trailing whitespace (trailing-whitespace)
tests/test_dice.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_dice.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_dice.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:10:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:17:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:23:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:35:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:40:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:45:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:49:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_dice.py:54:4: C0116: Missing function or method docstring (missing-function-docstring)
************* Module tests.test_board
tests/test_board.py:1:0: C0114: Missing module docstring (missing-module-docstring)
tests/test_board.py:4:0: C0115: Missing class docstring (missing-class-docstring)
tests/test_board.py:6:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:11:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:16:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:21:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:28:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:46:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:51:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:71:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:76:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:85:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:90:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:94:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:106:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:114:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:134:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:137:8: W0612: Unused variable 'ok' (unused-variable)
tests/test_board.py:146:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:168:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:181:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:198:15: W0718: Catching too general exception Exception (broad-exception-caught)
tests/test_board.py:210:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:222:4: C0116: Missing function or method docstring (missing-function-docstring)
tests/test_board.py:4:0: R0904: Too many public methods (22/20) (too-many-public-methods)

-----------------------------------
Your code has been rated at 7.78/10


```
