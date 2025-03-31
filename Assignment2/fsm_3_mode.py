class FSM:
    def __init__(self, states, alphabet, initial_state, accepting_states, transition_function):
        self.states = states
        self.alphabet = alphabet
        self.initial_state = initial_state
        self.accepting_states = accepting_states
        self.transition_function = transition_function
        self.current_state = initial_state

    def reset(self):
        self.current_state = self.initial_state

    def process(self, input_symbol):
        if input_symbol not in self.alphabet:
            raise ValueError(f"Invalid input symbol '{input_symbol}'. Must be one of {self.alphabet}.")

        next_state = self.transition_function[(self.current_state, input_symbol)]
        self.current_state = next_state

    def run(self, input_sequence):
        self.reset()
        for symbol in input_sequence:
            self.process(symbol)

        return self.current_state

    def is_accepted(self, input_sequence):
        final_state = self.run(input_sequence)
        return final_state in self.accepting_states


def mod_three():
    # Define configuration for Mod-Three
    states = ['S0', 'S1', 'S2']
    alphabet = ['0', '1']
    initial_state = 'S0'
    accepting_states = ['S0', 'S1', 'S2']
    transition_function = {
        ('S0', '0'): 'S0',
        ('S0', '1'): 'S1',
        ('S1', '0'): 'S2',
        ('S1', '1'): 'S0',
        ('S2', '0'): 'S1',
        ('S2', '1'): 'S2'
    }

    # Create FSM for Mod-Three
    mod_three_fsm = FSM(states, alphabet, initial_state, accepting_states, transition_function)

    # Test the FSM with some input strings
    input_string1 = '1101'
    final_state = mod_three_fsm.run(input_string1)
    remainder1 = int(final_state[1:])  # Get remainder from final state, 'S0' -> '0'

    input_string2 = '1110'
    final_state = mod_three_fsm.run(input_string2)
    remainder2 = int(final_state[1:])

    input_string3 = '1111'
    final_state = mod_three_fsm.run(input_string3)
    remainder3 = int(final_state[1:])

    print(f"Input : {input_string1} , Output: {remainder1}")
    print(f"Input : {input_string2} , Output: {remainder2}")
    print(f"Input : {input_string3} , Output: {remainder3}")


if __name__ == "__main__":
    mod_three()
