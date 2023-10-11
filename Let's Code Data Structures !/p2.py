filename = input("Input the Filename: ")
separation = filename.split(".")
extension = repr(separation[-1])
print ("The extension of the file is : " + extension)