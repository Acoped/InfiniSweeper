# "Pads" a matrix, inserts elements all around the matrix
def pad(m, padding):

    h = len(m)
    w = len(m[0])

    # Pad left and right
    for row in range(len(m)):
        m[row].insert(0, padding)
        m[row].insert(w + 1, padding)
    # Pad top and bottom
    list_padding = [padding] * (w + 2)
    m.insert(0, list_padding)
    m.insert(h + 1, list_padding)

    return m


# "Unpads" a matrix, removes elements all around the matrix
def un_pad(m):

    m = m[1:-1]
    h = len(m)
    for i in range(h):
        m[i] = m[i][1:-1]

    return m


# Changes all elements except 'dont_change' in a matrix 'm' to 'change_to'
def change_all_except(m, change_to, dont_change):

    h = len(m)
    w = len(m[0])

    for i in range(h):
        for j in range(w):
            cell = m[i][j]
            if cell != dont_change:
                m[i][j] = change_to

    return m


if __name__ == "__main__":
    test = [[4]]
    padded = pad(test, 8)
    print(padded)
    un_padded = un_pad(padded)
    print(un_padded)
