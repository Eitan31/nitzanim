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



#Q3
class Product:
    def __init__(self, name, price, on_sell):
        self.name = name
        self.price = price
        self.on_sell = on_sell

    def __str__(self):
        if self.on_sell:
            sell = "The product is on sell!"
        else:
            sell = "The product is not on sell!"
        return f"Product name: {self.name}, Price: {self.price}, {sell}"

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

    def check_if_on_sell(self):
        return self.on_sell

    def set_price(self, price):
        if price > 0:
            self.price = price
            return "Price updated!"
        return "Price not updated!, Please use only positive numbers."

    def set_name(self, name):
        if name != "":
            self.name = name
            return "Name updated!"
        return "Name not updated!, Name can't be empty!"

    def make_discount(self):
        if not self.on_sell:
            self.on_sell = True
            return "The product is now on sell"
        return "The product is already on sell!"

    def no_discount(self):
        if self.on_sell:
            self.on_sell = False
            return "The product is no longer on sell"
        return "The product is not on sell already"

#Q4


BUDGET = 80000
PAINTINGS = [
['Mona Lisa', 5341, 67],
['Starry night', 8908, 27],
['A girl with a pearl earring', 5914, 13],
['This Kiss', 3922, 20],
['Las Meninas', 5046, 61],
['birth of venus', 5576, 44],
['Guernica', 5627, 43],
['Arrangement in gray and black', 6680, 46],
['the night watch', 4361, 75],
['The Last Supper', 4907, 13],
['Sunrise impression', 3580, 68],
['Freedom leads the people', 5657, 20],
['The gypsy woman', 3862, 60],
['The sailors\' feast', 5332, 27],
['Night hawks', 4420, 44],
['The jellyfish raft', 7026, 71],
['the swing', 9594, 73],
['June flames', 9340, 69],
['son of man', 9847, 38],
['A storm in the Sea of Galilee', 7555, 56]
]



def q4a(paintings, budget, index=0):
    if index == len(paintings) or budget<= 0:
        return  0, []

    name, price, people = paintings[index]

    not_taking, not_list = q4a(paintings, budget, index + 1)

    take, take_list = 0, []
    if price <= budget:
        take, take_list = q4a(paintings, budget - price, index + 1)
        take += people

    if take > not_taking:
        return take, [name] + take_list
    return not_taking, not_list


max_people, chosen_list = q4a(PAINTINGS, BUDGET)

print("Max people:", max_people)
print("paintings:")
for painting in chosen_list:
    print("-", painting)

def q4b():
    return sum(p[2] for p in PAINTINGS)
print(q4b())

def q4c(paintings, names):
    total = 0
    for name in names:
        for paint in paintings:
            if name == paint[0]:
                total += paint[1]
                break
    return BUDGET - total
print(q4c(PAINTINGS, chosen_list))
