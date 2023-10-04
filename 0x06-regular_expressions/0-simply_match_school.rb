#!/usr/bin/env ruby

# Checks if an argument is provided
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <text>"
  exit(1)
end

# Defines the regular expression pattern
pattern = /School/

# Extracts the argument
text = ARGV[0]

# Checks if the pattern matches the text
if text.match?(pattern)
  puts text
else
  puts ""
end
