# LOG-PARSE

The script uses a regular expression to split each line of an input file into its component parts and store those parts in a list of dictionaries. The script uses helper functions to break out the unique applications captured and the logs related to the application for output. Input is taken in the form of a file argument. I have tested several different log files, such as output from journalctl, /var/log/messages directly, and a rotated /var/log/auth. Multi-line entries are not caught by the current regular expression.

I have opted to count message strings for uniqueness based on the entire contents of the string instead of just the first word. This fulfills the Advanced section of the Extra tasks, but I believe using something like fuzzy string matching would allow for more accurate message grouping based on purpose instead of just matching the strings for equivalence.

For the Intermediate section of the Extra tasks, I would add a capture group to my regular expression to catch the time tag of the log line separately and track the time to group logs into one hour chunks. For the output, iterate through each of the hour chunks, print a time code for the chunk and then use the functions I have already developed to process each chunk individually.
