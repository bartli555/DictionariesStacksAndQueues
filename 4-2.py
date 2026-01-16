import queue

# creates a queue of files to print
files_to_print = queue.Queue()

while True:
   print('1. Add file to print')
   print('2. Print file')
   print('0. Quit')
   menu = input('Select an option: ')
   
   # Opcja 1: Dodawanie pliku do kolejki
   if menu == '1':
      file_name = input('Enter file name to print: ')
      # add new file to the end of the queue
      files_to_print.put(file_name) 
      print(f"File '{file_name}' added to print queue.\n")

   # Opcja 2: Drukowanie (pobieranie z kolejki)
   elif menu == '2':
      # Sprawdzamy, czy kolejka nie jest pusta
      if not files_to_print.empty():
         # Pobieramy pierwszy element z kolejki
         file_to_print = files_to_print.get()
         print(f'File {file_to_print} is currently being printed. Please wait!\n')
      else:
         print("The print queue is empty. Nothing to print.\n")

   # Opcja 0: Wyjście
   elif menu == '0':
      break
      
   else:
      print("Invalid option. Please try again.\n")