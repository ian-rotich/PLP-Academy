import 'dart:io';

void main() {
  // Prompt the user to enter a number
  stdout.write('Enter a number: ');

  // Read the input from the user
  String input = stdin.readLineSync()!;

  // Convert the input to an integer
  int number = int.parse(input);

  // Check the number and print the appropriate message
  if (number > 10) {
    print('Your number is greater than 10');
  } else if (number < 10) {
    print('Your number is less than 10');
  } else {
    print('Your number is equal to 10');
  }
}
