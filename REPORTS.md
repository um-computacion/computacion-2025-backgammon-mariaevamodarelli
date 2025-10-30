# Automated Reports
## Coverage Report
```text
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
cli/__init__.py             0      0   100%
core/__init__.py            0      0   100%
core/board.py              97     32    67%   26, 31, 37, 44-50, 83, 93-124, 131, 161
core/checker.py             9      0   100%
core/dice.py               17      0   100%
core/game.py               45      8    82%   46-48, 83, 88-93
core/player.py             23      0   100%
pygame_ui/__init__.py       0      0   100%
tests/__init__.py           0      0   100%
tests/test_board.py       132      1    99%   183
tests/test_checker.py      13      1    92%   17
tests/test_dice.py         48      1    98%   61
tests/test_game.py         62      1    98%   95
tests/test_player.py       44      2    95%   43, 54
-----------------------------------------------------
TOTAL                     490     46    91%

```
## Pylint Report
```text
************* Module main.py
main.py:1:0: F0001: No module named main.py (fatal)
************* Module test.py
test.py:1:0: F0001: No module named test.py (fatal)

```
