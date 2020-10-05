## Computer Architecture
### RAM - storing data and instructions the CPU runs
- fast compared to hard drives and SSDs
- like a giant array (address and value)
- hexadecimal bytes are 2 digits long in hex
### CPU executes instructions
- operates on words (64 bit, 8 byte)
- 8 bytes for a 64-bit CPU
- 4 bytes for a 32-bit CPU
- 1 byte for an 8-bit CPU

CPU Registers
- smaller array with CPU
- register is size of a CPU word

- what causes a CPU to decide what to do?
- CPU gets an instruction out of RAM

- address of currently-executing instruction is held in special place called the program counter (PC)

CPU decides how fast to retrieve data from RAM by its CPU clock, clock cycle rate is measured in Hz, KHz, MHz, or GHz

multiple cores share RAM but perform in parallel

- concurrency by timesharing

### System Bus
- how data is passed from CPU to RAM, and from CPU to peripherals
- address bus: carries address in RAM (or peripheral ID) we're interested in
- data bus: carries data to be transmitted to or from RAM or peripherals
- control bus: whether or not the CPU is talking to RAM or peripheral
- width of bus is typically number of bits a computer is advertised as having. A 64-bit CPU has a 64-bit wide data base, usually a 64-bit wide address bus
- the cache speeds up access to RAM by grabbing requested index as well as additional data (cache hit vs cache miss)

Number bases
byte/octet: 8 bits, max value: 225 (decimal), FF (hex), min value 0
nibble: 4 bits
decimal: base-10 numbering system
hexadecimal/hex: base-16 numbering system
binary: base-2 numbering system
octal: base-8 numbering system (rarely used)

octal trap
int x = 12 // decimal
int y = 012; // octal, decimal value 10

binary 
2^6, 2^5, 2^4, 2^3, 2^2, 2^1, 2^0
64   32   16    8    4    2    1



10011011
128 + 1 + 2 + 8 + 16
155

67 decimal
1000011


163
1010 0011
A3

10101010
128 + 42
170

C7 to binary

110 111

110111 to decimal 

56 in decimal

255
01111111
FF

ASCII encoding is a set of rules that allows us to translate certain characters into decimal numbers.

Count to 0x20 in hex
1, 2 3 4 5 6 7 8 9, a, b , c, d , e, f,10, 11, 12, 13,14... 19.. 1a, 1b, 1c, 1d, 1e, 1f, 20, 21, 22, 29.. 2a, 2f.. 30

What is 0x2F in binary?


Convert 0b11011 to decimal

What is 0b11100111 in hex?

What is 27 in binary?

Write a program that outputs a value in binary. Hint: >> and &

multibit numbers

Lecture 2
Different bitwise operations
- isolate the bits
    - number of operands: 0b10010101 >> 6 == 2 
    - if this is an ALU operation:
        - ADD is an ALU op. 10100000 >> 5 = 101
            - & it with 001 for a positive ALU = 001
            - concise: ((0b10100000 >> 5) & 001)

What is the stack? 
- stack data stored in ram
- stack pointer keeps track of address on top of stack
- typically stack grows down from higher memory address 
    - decrement address in stack and store 
    - pop from bottom of the stack??
- only so many registers, so we can push it on the stack and use it as temporary storage of variables
- storage of registers and cpu state during an interrupt
- how can you detect if stack is empty?
what happens if you pop from an empty stack?
what happens if you push too many items on the stack?
what info must be saved on the stack when the cpu is servicing the interrupt? why?

- pc needs to move to interrupt handler
    - interrupt vector table 