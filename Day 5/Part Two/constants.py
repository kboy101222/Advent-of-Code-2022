# RegEx Search constants

# Line Type Searches
NEW_LINE = "^(\n)$"
BOX_LINE = "^((\s{3}|\[[a-zA-Z]\])\s{1})[^\n]+"
NUMS_LINE = "\s[1-9]\s"
INST_LINE = "^(move )\d+( from )\d+( to )\d+$"

# Box line searches
BOXES = "(\s{3}|\[[A-Z]\])(\s{1}|\n|$)"

# Instruction Line searches
INST_NUMS = "\d"