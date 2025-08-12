#Q1
def q1(num):
    print(num)
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1
        print(num)



#Q2
def process_and_query_matrix(rows=12, cols=12):
    def shift_right(a, b, c, d):
        return c, a, d, b

    def shift_left(a, b, c, d):
        return b, d, a, c

    def get_block(mat, start_row, start_col, size=2):
        return [mat[start_row + i][start_col:start_col + size] for i in range(size)]

    def set_block(mat, start_row, start_col, block):
        for i, row_data in enumerate(block):
            mat[start_row + i][start_col:start_col + len(row_data)] = row_data

    mat = [[r * cols + c + 1 for c in range(cols)] for r in range(rows)]

    new_mat = [[0] * cols for _ in range(rows)]

    for r in range(0, rows, 2):
        for c in range(0, cols, 2):
            A = mat[r][c]
            B = mat[r][c + 1]
            C = mat[r + 1][c]
            D = mat[r + 1][c + 1]

            if (c // 2) % 2 == 0:
                newA, newB, newC, newD = shift_right(A, B, C, D)
            else:
                newA, newB, newC, newD = shift_left(A, B, C, D)

            new_mat[r][c]     = newA
            new_mat[r][c + 1] = newB
            new_mat[r + 1][c] = newC
            new_mat[r + 1][c + 1] = newD

    block_size = 2

    for row in range(0, rows, 4):
        for col in range(0, cols, 4):
            A = get_block(new_mat, row, col, block_size)
            B = get_block(new_mat, row, col + 2, block_size)
            C = get_block(new_mat, row + 2, col, block_size)
            D = get_block(new_mat, row + 2, col + 2, block_size)

            set_block(new_mat, row, col, D)
            set_block(new_mat, row + 2, col + 2, A)
            set_block(new_mat, row, col + 2, C)
            set_block(new_mat, row + 2, col, B)

    def q2a():
        total = 0
        for row in new_mat:
            total += row[8]
        return total

    def q2b():
        for i in range(len(new_mat)):
            for j in range(len(new_mat[i])):
                if new_mat[i][j] == 89:
                    return i
        return None

    def q2c():
        m = 0
        for num in new_mat[7]:
            if num > m and num % 7 == 0:
                m = num
        return m

    for r in new_mat:
        print(r)

    return new_mat, q2a(), q2b(), q2c()

matrix, sum_row7, row_89, max_row6 = process_and_query_matrix()

print("Sum of collum 8:", sum_row7)
print("Row of value 89:", row_89)
print("Max value in row 7:", max_row6)
