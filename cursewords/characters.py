vline = "│"
hline = "─"

lhblock = "▌"
rhblock = "▐"
fullblock = "█"

# Corner characters keyed by a bitmap indicating whether the left, top, right,
# and bottom sides respectively need a line coming out of them. Not all
# possible values are represented since we never need a "corner" with only one
# line. As a special case, 0 is a block because it means we're in the middle of
# a filled area.
corner = {
    0b0000: fullblock,
    0b0011: "┌",
    0b0101: vline,
    0b0110: "└",
    0b0111: "├",
    0b1001: "┐",
    0b1010: hline,
    0b1011: "┬",
    0b1100: "┘",
    0b1101: "┤",
    0b1110: "┴",
    0b1111: "┼",
}

small_nums = str.maketrans('1234567890',
                           '₁₂₃₄₅₆₇₈₉₀')
encircle = str.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZ ',
                         'ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ◯')
