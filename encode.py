# Encode Python code into an image
def encode_image(input_image, output_image, python_code):
    with open(input_image, "rb") as image_file:
        image_data = image_file.read()

    with open(output_image, "wb") as output_file:
        output_file.write(image_data)
        output_file.write(b'\n# Hidden Python Code\n')
        output_file.write(python_code.encode())


# Enter your code here as a string
python_code = '''
def hidden_function():
    print("This is hidden code! ")
    
hidden_function()
'''

# Location where you want to save the encoded image
output_directory = 'C:\\Users\\Johnny Antony\\PycharmProjects\\pythonProject1\\watcher\\output_image.png'

encode_image('test.png', output_directory, python_code)