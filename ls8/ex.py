
# save the address to jump to 
# 10000100 # SAVE
# 0 # R0
# address to jump to (index of subroutine) 
# 8 (because see below)
# print 99
# PRINT_NUM
# 01100011 # 99
# call our subroutine to print tim
# CALL needs register 
# 01011001 # CALL 
# 0 # R0

# halt
# HALT
# 00000010

# subroutine
# 00000001 #PRINT_TIM 
# 00000001 #PRINT_TIM 
# 00011010 #RET

# see below:
memory = [
    SAVE
    0,
    8 # IDX OF SUBROUTINE
    PRINT_NUM,
    99,
    call,
    0,
    HALT,
    PRINT_TIM,
    PRINT_TIM,
    RET
]
# ram for all commands
# stack frame for each function
# register to return values


ADD = 0b10101010 #ADD, for ex
MUL = 0b11110000 #Mult for ex

class Foo:

    def __init__(self):
        # Set up the branch table
        self.branchtable = {}
        self.branchtable[ADD] = self.handle_add
        self.branchtable[MUL] = self.handle_mul

    def handle_add(self, a):
        print("add: " + a)

    def handle_mul(self, a):
        print("mul: " + a)

    def run(self):
        # Example calls into the branch table
        IR = ADD
        self.branchtable[IR]("foo")

        IR = MUL
        self.branchtable[IR]("bar")

c = Foo()
c.run()