'''
this code will decode a RTO13-ed file
'''

import codecs

def decode_rot13(input_file, output_file):
    try:
        # Open the input file and read its contents
        with open(input_file, 'r') as infile:
            encoded_text = infile.read()
        
        # Decode the ROT-13 encoded text
        decoded_text = codecs.decode(encoded_text, 'rot_13')
        
        # Write the decoded text to the output file
        with open(output_file, 'w') as outfile:
            outfile.write(decoded_text)
        
        print(f"Decoding complete. Decoded text written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'C:/Users/Admin/Desktop/ifile.txt'  # Replace with your input file name
output_file = 'C:/Users/Admin/Desktop/ofile.txt'  # Replace with your desired output file name
decode_rot13(input_file, output_file)
