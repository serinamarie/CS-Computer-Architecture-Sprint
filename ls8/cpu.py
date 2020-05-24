"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""
   

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def load(self):
        """Load a program into memory."""

        if (len(sys.argv)) != 2:
            print('remember to pass the second file name')
            print('usage: python fileio.py <second_filename.py>')
            sys.exit()

        try: 
            with open(sys.argv[1]) as f:
                address = 0

                for line in f:
                    possible_binary = line[:line.find('#')]
                    # if no comment on line
                    if possible_binary == '':
                        continue # passes rest of loop
                    denary_int = int(possible_binary, 2)
                    self.ram[address] = denary_int
                    address += 1
                
        except FileNotFoundError:
            print(f'Error from {sys.argv[0]}: {sys.argv[1]} not found ')
            sys.exit()


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, address):
        return self.ram[address]
    
    def ram_write(self, address, data):
        self.ram[address] = data
        

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        IR = []
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        operand_a = self.ram_read(self.pc+1) 
        operand_b = self.ram_read(self.pc+2)
    
        running = True 

        while running:

            IR = self.ram[self.pc] # instruction register
            num_args = IR >> 6

            if IR == LDI: # LDI
                # set register at index to value
                self.reg[operand_a] = operand_b 
                # self.pc += 3 # increment

            elif IR == PRN: # print
                # get the address whose value we are printing out
                print(self.reg[operand_a])

                # self.pc += 2
                
            elif IR == HLT: # halt

                running = False
            
            else:
                print('Unknown command')
                running = False
            
            self.pc += 1 + num_args
        

        

if __name__ == '__main__':
    cpu = CPU()
    cpu.load()
    print(cpu.ram)
    # cpu.trace()
    # cpu.run()
    # import sys