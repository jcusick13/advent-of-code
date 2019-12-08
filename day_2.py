def int_computer(intcode):
    """Computes final values by walking through list of
    provided elements in `intcode`.

    intcode : list of integers
        Instructions for the computer

    Returns : list of integers
        The final set of intcode values after
        encountering termination instruction
    """
    for i in range(0, len(intcode), 4):
        # Check for program termination
        instruction = intcode[i]
        if instruction == 99:
            return intcode

        # Collect program instructions
        noun_idx = intcode[i + 1]
        verb_idx = intcode[i + 2]
        noun = intcode[noun_idx]
        verb = intcode[verb_idx]
        loc = intcode[i + 3]

        if instruction == 1:
            intcode[loc] = noun + verb
        elif instruction == 2:
            intcode[loc] = noun * verb
        else:
            raise ValueError("Instruction must be 1, 2, or 99.")
    return intcode


def part_one(file):
    with open(file) as f:
        lines = f.readlines()
    value = [int(x.strip()) for x in lines[0].split(",")]

    # Reset values to 1202 alarm state
    value[1] = 12
    value[2] = 2
    print(int_computer(value))


def part_two(file):
    with open(file) as f:
        lines = f.readlines()
    orig_value = [int(x.strip()) for x in lines[0].split(",")]

    for noun in range(100):
        for verb in range(100):
            value = orig_value.copy()
            value[1] = noun
            value[2] = verb

            result = int_computer(value)
            if result[0] == 19690720:
                print(f"Noun: {noun}, Verb: {verb}, Soln: {100 * noun + verb}")
                return
    print("Unable to find solution")


if __name__ == "__main__":
    part_two("inputs/day_2.txt")
