# Basic-Login-System
A basic login system

We create a dictionary for users of the login system then ask for a username (.strip() removes spaces at the end and start of a string). We establish 5 counters for upper/lowercase, special characters and numbers and when the check fails. The first check is a length check through the if statement that requires a minimum of 8 characters. Then a for loop using a copy of the string just in case of any changes. The checks then check if it is lower/uppercase, symbols or numbers, adding to their respective counters. Then if any of the counters are 0, we add to the fails counter for any failed checks. Then, based on the value of fails we determine if strong, medium or weak. We then ask if they want to test another password (if they want to strengthen it). Then, if not weak we add it to the username in the user dictionary. Then, this is where the login part happens when we ask for a user. If the username exists, we ask for a password with three attempts.

• Handles user input and validation (e.g., checking usernames, passwords, matching stored data).
• Demonstrates control flow, conditional logic, and basic data handling in Python.
• Shows understanding of program structure through functions or modules that manage authentication steps.
